#!/usr/bin/env python3
"""Turn the record in .github/analyses.yaml into a job matrix, one row per analysis file.

A data set's key is also the name of the branch carrying it. Branches that do not exist are
reported as workflow warnings and dropped, so that a data set awaiting its branch does not block
validation of every other data set.

A data set contributes no row if it is marked 'skip', or if it records no analysis file at all --
an empty entry, describing a data set that carries none.
"""

import argparse
import json
import os
import subprocess
import sys

import yaml

KNOWN_KEYS = {'analysis_files', 'skip'}


def branch_exists(remote: str, branch: str) -> bool:
    result = subprocess.run(
        ['git', 'ls-remote', '--exit-code', '--heads', remote, f'refs/heads/{branch}'],
        stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True
    )
    if result.returncode not in (0, 2):
        raise RuntimeError(f'git ls-remote failed for branch \'{branch}\': {result.stderr.strip()}')

    return result.returncode == 0


def emit(name: str, value: str) -> None:
    github_output = os.environ.get('GITHUB_OUTPUT')
    if github_output is None:
        print(f'{name}={value}')
        return

    with open(github_output, 'a', encoding='utf-8') as f:
        f.write(f'{name}={value}\n')


def summarize(lines: list[str]) -> None:
    github_step_summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if github_step_summary is None:
        print('\n'.join(lines), file=sys.stderr)
        return

    with open(github_step_summary, 'a', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', help='the YAML file recording the analysis files of each data set')
    parser.add_argument('--remote', default='origin', help='the remote whose branches are checked out')
    args = parser.parse_args()

    with open(args.record, encoding='utf-8') as f:
        record = yaml.safe_load(f) or {}

    include = []
    excluded = {'skipped': [], 'no analysis file': [], 'no branch': []}
    for data_set, description in sorted(record.items()):
        description = description or {}
        if (unknown := description.keys() - KNOWN_KEYS):
            raise ValueError(f'data set \'{data_set}\' records unknown key(s): {", ".join(sorted(unknown))}')

        if description.get('skip'):
            excluded['skipped'].append(data_set)
            continue

        analysis_files = description.get('analysis_files') or []
        if not analysis_files:
            excluded['no analysis file'].append(data_set)
            continue

        if not branch_exists(args.remote, data_set):
            excluded['no branch'].append(data_set)
            print(f'::warning title=Missing branch::Data set {data_set} is recorded in '
                  f'{args.record} but has no branch \'{data_set}\'; it will not be validated.')
            continue

        include.extend(
            {'data_set': data_set, 'branch': data_set, 'analysis_file': analysis_file}
            for analysis_file in analysis_files
        )

    emit('matrix', json.dumps({'include': include}))
    emit('empty', 'true' if not include else 'false')

    summary = ['## Analysis files to validate', '', '| Data set | Analysis file |', '| --- | --- |']
    summary += [f'| `{row["data_set"]}` | `{row["analysis_file"]}` |' for row in include] or ['| _none_ | |']
    summary += [
        f'\nNot validated ({reason}): {", ".join(f"`{d}`" for d in data_sets)}.'
        for reason, data_sets in excluded.items() if data_sets
    ]
    summarize(summary)

    return 0


if __name__ == '__main__':
    sys.exit(main())
