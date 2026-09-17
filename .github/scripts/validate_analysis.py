#!/usr/bin/env python3
"""Validate a single EOS analysis file and record the errors found.

Runs inside the EOS container, with the working directory set to the checked-out data set so that
the deep validation phase resolves relative data paths as it would for a user. The result is
written as JSON, since ``eos-analysis validate`` exits 0 whether or not it finds anything.

``eos.validate`` returns one ``eos.Diagnostic`` per finding, carrying a severity and, where EOS can
resolve one, the line of the analysis file it refers to. Only the errors are reported: warnings
(an unused prior, say, or a constraint file that has not been produced yet) are expected for
released data sets and must not raise an alarm. This requires EOS 1.1 or later; up to 1.0.21
``eos.validate`` returned nothing and knew no severities.
"""

import argparse
import contextlib
import io
import json
import sys
import traceback


def errors_from(diagnostics) -> list[dict]:
    """Return one {'line', 'message'} per error. 'line' is None where EOS resolved no position."""
    from eos.diagnostic import Severity

    return [
        {'line': d.line, 'message': f'{d.location()}: {d.message}'}
        for d in diagnostics if d.severity is Severity.ERROR
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('analysis_file', help='the analysis file to validate, relative to the working directory')
    parser.add_argument('--output', required=True, help='the JSON file to write the result to')
    args = parser.parse_args()

    import eos

    result = {'analysis_file': args.analysis_file, 'version': eos.__version__, 'errors': [], 'log': ''}

    # eos.validate() prints as it goes; capture that so only the filtered errors are reported.
    printed = io.StringIO()
    try:
        with contextlib.redirect_stdout(printed):
            diagnostics = eos.validate(analysis_file=args.analysis_file)
        result['errors'] = errors_from(diagnostics)
    except Exception:
        result['errors'] = [{'line': None,
                             'message': f'Validation aborted with an unhandled exception:\n{traceback.format_exc()}'}]
    result['log'] = printed.getvalue()

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)

    print(f'{args.analysis_file}: EOS v{result["version"]}, {len(result["errors"])} error(s)', file=sys.stderr)

    return 0


if __name__ == '__main__':
    sys.exit(main())
