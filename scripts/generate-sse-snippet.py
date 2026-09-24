#!/usr/bin/env python3
# vim: set sw=4 sts=4 et tw=120 :

# Copyright (c) 2026 Danny van Dyk
#
# This file is part of the EOS project. EOS is free software;
# you can redistribute it and/or modify it under the terms of the GNU General
# Public License version 2, as published by the Free Software Foundation.
#
# EOS is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA

"""Generate the parameter-database YAML snippet for a transition's SSE
form-factor coefficients.

For every SSE coefficient that was fitted for a given transition, the script
emits a database entry with

    central : the weighted posterior mean
    min/max : mean -/+ N * sigma   (N is configurable, default: 5)
    latex   : taken verbatim from the existing EOS parameter database
    unit    : taken verbatim from the existing EOS parameter database

The list of coefficients, the posterior samples and their importance weights are
read from the analysis data directory produced by ``eos-analysis``
(``<base>/data/<transition>/{mode-default,samples}``).

The resulting snippet can be pasted directly into
``eos/parameters/hadronic-matrix-elements.yaml``.

Example
-------
    ./generate-sse-snippet.py B-to-pi
    ./generate-sse-snippet.py --sigma 3 Bc-to-Jpsi > /tmp/bc.yaml
"""

import argparse
import os
import sys

import numpy as np
import yaml

import eos

DEFAULT_BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))


def weighted_moments(samples, weights):
    """Return the (weighted mean, weighted standard deviation) per column."""
    w    = np.asarray(weights, dtype=float)
    w   /= w.sum()
    mean = np.average(samples, axis=0, weights=w)
    var  = np.average((samples - mean) ** 2, axis=0, weights=w)
    return mean, np.sqrt(var)


def available_transitions(base):
    datadir = os.path.join(base, 'data')
    if not os.path.isdir(datadir):
        return []
    return sorted(
        t for t in os.listdir(datadir)
        if os.path.exists(os.path.join(datadir, t, 'mode-default', 'description.yaml'))
    )


def snippet_for(transition, base, sigma, params):
    """Build the YAML snippet (as a string) for a single transition."""
    datadir  = os.path.join(base, 'data', transition)
    modefile = os.path.join(datadir, 'mode-default', 'description.yaml')
    smpldir  = os.path.join(datadir, 'samples')

    if not os.path.exists(modefile):
        raise FileNotFoundError(f"no mode-default/description.yaml for '{transition}' (looked in {datadir})")

    with open(modefile) as f:
        mode = yaml.safe_load(f)
    names = [p['name'] for p in mode['parameters']]

    samples = np.load(os.path.join(smpldir, 'samples.npy'))
    weights = np.load(os.path.join(smpldir, 'weights.npy'))
    mean, std = weighted_moments(samples, weights)

    lines = []
    for name, mu, sg in zip(names, mean, std):
        # metadata (latex, unit) come from the existing parameter database
        p     = params[name]
        latex = p.latex()
        unit  = str(p.unit())
        lines.append(f"      '{name}' :")
        lines.append(f"          central: {mu:.5f}")
        lines.append(f"          min:     {mu - sigma * sg:.5f}")
        lines.append(f"          max:     {mu + sigma * sg:.5f}")
        lines.append(f"          latex:    '{latex}'")
        lines.append(f"          unit:     '{unit}'")
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Generate the SSE parameter-database YAML snippet for one or more transitions.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('transitions', nargs='*', metavar='TRANSITION',
        help="data sub-directory name(s), e.g. 'B-to-pi', 'Bc-to-Jpsi'; if none are given, the available transitions are listed")
    parser.add_argument('-n', '--sigma', type=float, default=5.0,
        help='half-width of the min/max interval in units of the posterior standard deviation')
    parser.add_argument('-b', '--base', default=DEFAULT_BASE,
        help='BASE_DIRECTORY of the analysis (containing the data/ folder)')
    args = parser.parse_args()

    known = available_transitions(args.base)

    if not args.transitions:
        print('available transitions:', file=sys.stderr)
        for t in known:
            print(f'  {t}', file=sys.stderr)
        return 0

    params = eos.Parameters.Defaults()

    rc = 0
    for i, transition in enumerate(args.transitions):
        if len(args.transitions) > 1:
            if i:
                print()
            print(f'      # {transition}')
        try:
            print(snippet_for(transition, args.base, args.sigma, params))
        except FileNotFoundError as e:
            print(f'error: {e}', file=sys.stderr)
            if known:
                print('available transitions: ' + ', '.join(known), file=sys.stderr)
            rc = 1
    return rc


if __name__ == '__main__':
    sys.exit(main())
