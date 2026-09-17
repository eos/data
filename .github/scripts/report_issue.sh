#!/usr/bin/env bash
#
# Report the outcome recorded by validate_analysis.py: open an issue for the errors found, or
# update the body of the issue already open for this data set and analysis file. Issues are never
# closed automatically; a human decides when a report has been dealt with.
#
# Where EOS reports the line an error refers to, the error is also emitted as a workflow
# annotation, and linked from the issue body. The annotation names a file that does not exist on
# the branch this workflow runs from, so it is listed in the run rather than bound to the source;
# the links in the issue body are pinned to the data set's own commit and do resolve.

set -euo pipefail

: "${DATA_SET:?}" "${ANALYSIS_FILE:?}" "${BRANCH:?}" "${RESULT_FILE:?}" "${GH_REPO:?}" "${GH_TOKEN:?}"
: "${LABEL:=validation}"
: "${SERVER_URL:=https://github.com}"
: "${MAX_LINKS:=20}"

count=$(jq '.errors | length' "${RESULT_FILE}")
version=$(jq -r '.version' "${RESULT_FILE}")

if [[ "${count}" -eq 0 ]]; then
    echo "::notice title=Validated::${DATA_SET}: ${ANALYSIS_FILE} validates cleanly with EOS v${version}."
    exit 0
fi

title="EOS-DATA-${DATA_SET}: Validation failed for analysis file \`${ANALYSIS_FILE}\`"
blob="${SERVER_URL}/${GH_REPO}/blob/${COMMIT:-${BRANCH}}/${ANALYSIS_FILE}"

# One annotation per error, so the Actions UI lists them with their position.
jq -r --arg file "${ANALYSIS_FILE}" --arg set "${DATA_SET}" '
    .errors[]
    | "::error file=\($file)\(if .line then ",line=\(.line)" else "" end),title=EOS-DATA-\($set)::"
      + (.message | gsub("%";"%25") | gsub("\n";"%0A") | gsub("\r";"%0D"))
' "${RESULT_FILE}"

body=$(mktemp)
{
    printf 'One or more issues were found when validating `%s` with EOS v%s.\n\n' "${ANALYSIS_FILE}" "${version}"
    printf '```\n'
    jq -r '.errors[] | (if .line then "line \(.line): " else "" end) + .message' "${RESULT_FILE}"
    printf '```\n\n'

    located=$(jq '[.errors[] | select(.line)] | length' "${RESULT_FILE}")
    if [[ "${located}" -gt 0 ]]; then
        printf '### Locations\n\n'
        # Consecutive lines are collapsed into ranges, since one fault usually spans a whole block.
        jq -r --arg blob "${blob}" --arg file "${ANALYSIS_FILE}" --argjson max "${MAX_LINKS}" '
            [.errors[] | select(.line) | .line] | unique
            | reduce .[] as $l ([];
                if (length > 0 and .[-1][1] == $l - 1) then .[:-1] + [[.[-1][0], $l]] else . + [[$l, $l]] end)
            | (.[:$max] | .[] | if .[0] == .[1]
                  then "- [`\($file):\(.[0])`](\($blob)#L\(.[0]))"
                  else "- [`\($file):\(.[0])-\(.[1])`](\($blob)#L\(.[0])-L\(.[1]))" end),
              (if length > $max then "- … and \(length - $max) further ranges" else empty end)
        ' "${RESULT_FILE}"
        printf '\n'
    fi

    printf -- '---\nBranch `%s` at %s, checked by [this workflow run](%s).\n' \
        "${BRANCH}" "${COMMIT:-unknown commit}" "${RUN_URL:-}"
} > "${body}"

# Match on the exact title: one issue per data set and analysis file.
number=$(gh issue list --repo "${GH_REPO}" --state open --label "${LABEL}" --limit 200 --json number,title \
    | jq -r --arg title "${title}" 'map(select(.title == $title)) | .[0].number // empty')

if [[ -n "${number}" ]]; then
    gh issue edit "${number}" --repo "${GH_REPO}" --body-file "${body}"
    echo "${DATA_SET}: ${ANALYSIS_FILE} reported ${count} error(s); updated issue #${number}."
else
    gh issue create --repo "${GH_REPO}" --title "${title}" --label "${LABEL}" --body-file "${body}"
    echo "${DATA_SET}: ${ANALYSIS_FILE} reported ${count} error(s); opened a new issue."
fi
