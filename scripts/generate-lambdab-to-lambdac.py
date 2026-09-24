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

"""Generate the Lambda_b -> Lambda_c blocks of ``analysis.yaml``.

EOS ships a single Lambda_b -> Lambda_c form-factor constraint, DKMR:2017A, and it
constrains the DKMR2017 z-expansion coefficients as pseudo-observables. Such a
constraint carries no dependence on the SSE coefficients and therefore cannot drive
the fit. This script converts it into synthetic form-factor values -- the shape the
Lambda_b -> Lambda, Lambda_c -> Lambda and Lambda_c -> N constraints already have --
by propagating the DKMR2017 mean and covariance through the (linear) z expansion.

The grid holds one point per free DKMR2017 coefficient, so the pushforward covariance
stays regular and the synthetic data carry the full DKMR:2017A information.

It also reports the mode and covariance of the resulting SSE fit, from which the
prior ranges below are read off as mean +- 6 sigma.
"""

import numpy as np
import warnings
import yaml

warnings.filterwarnings('ignore')
import eos  # noqa: E402

CONSTRAINT = 'Lambda_b->Lambda_c::f_perp+long+time^V+A+T+T5@DKMR:2017A'
SYNTHETIC  = 'Lambda_b->Lambda_c::f_time+long+perp^V+A+T+T5@DKMR:2017A'

# form factor -> number of free DKMR2017 coefficients; f_perp^A and f_perp^T5 have their
# leading coefficient fixed by the equation of motion at q^2 = q^2_max
FFS = [
    ('f_long^V',  2), ('f_time^V',  2), ('f_perp^V',  2),
    ('f_long^A',  2), ('f_time^A',  2), ('f_perp^A',  1),
    ('f_long^T',  2), ('f_perp^T',  2),
    ('f_long^T5', 2), ('f_perp^T5', 1),
]
Q2LO, Q2HI = 1.0, 10.0

SSE = [
    'alpha^(0,V)_0',  'alpha^(0,V)_1',  'alpha^(perp,V)_0', 'alpha^(perp,V)_1', 'alpha^(t,V)_1',
    'alpha^(0,A)_0',  'alpha^(0,A)_1',  'alpha^(perp,A)_1', 'alpha^(t,A)_1',
    'alpha^(0,T)_0',  'alpha^(0,T)_1',  'alpha^(perp,T)_1',
    'alpha^(0,T5)_1', 'alpha^(perp,T5)_0', 'alpha^(perp,T5)_1',
]


def grid():
    return [(ff, q2) for ff, n in FFS for q2 in ([Q2LO, Q2HI] if n == 2 else [Q2HI])]


def observables(parameters, tag):
    return [
        eos.Observable.make(f'Lambda_b->Lambda_c::{ff}(q2)', parameters,
                            eos.Kinematics(q2=q2), eos.Options(**{'form-factors': tag}))
        for ff, q2 in grid()
    ]


def jacobian(parameters, obs, pars, values):
    evaluate = lambda: np.array([o.evaluate() for o in obs])
    J = np.zeros((len(obs), len(pars)))
    for j, (par, value) in enumerate(zip(pars, values)):
        h = 1.0e-4 * max(1.0, abs(value))
        par.set(value + h); fp = evaluate()
        par.set(value - h); fm = evaluate()
        par.set(value)
        J[:, j] = (fp - fm) / (2.0 * h)
    return J


def main():
    entry = yaml.safe_load(eos.Constraints()[CONSTRAINT].serialize())
    mu, Sigma = np.array(entry['means']), np.array(entry['covariance'])

    parameters = eos.Parameters.Defaults()
    pars = [parameters[n] for n in entry['observables']]
    for par, value in zip(pars, mu):
        par.set(value)

    obs = observables(parameters, 'DKMR2017')
    y   = np.array([o.evaluate() for o in obs])
    J   = jacobian(parameters, obs, pars, mu)
    C   = 0.5 * (J @ Sigma @ J.T + (J @ Sigma @ J.T).T)

    eigenvalues = np.linalg.eigvalsh(C)
    assert eigenvalues.min() > 0.0, 'pushforward covariance is not positive definite'
    print(f'# synthetic data: {len(y)} values, covariance condition number {eigenvalues.max() / eigenvalues.min():.3g}')

    # linear least-squares fit of the SSE coefficients to the synthetic data
    sse = [parameters[f'Lambda_b->Lambda_c::{n}@SSE'] for n in SSE]
    for par in sse:
        par.set(0.0)
    obs_sse = observables(parameters, 'SSE')
    f0 = np.array([o.evaluate() for o in obs_sse])
    D  = np.zeros((len(y), len(sse)))
    for j, par in enumerate(sse):
        par.set(1.0); D[:, j] = np.array([o.evaluate() for o in obs_sse]) - f0; par.set(0.0)

    Cinv  = np.linalg.inv(C)
    cov   = np.linalg.inv(D.T @ Cinv @ D)
    alpha = cov @ (D.T @ Cinv @ (y - f0))
    residuals = y - f0 - D @ alpha
    print(f'# SSE fit: chi^2 = {residuals @ Cinv @ residuals:.3f} for {len(y) - len(sse)} dof')

    print(f'\n# --- likelihoods: manual constraint {SYNTHETIC}')
    print(f"      '{SYNTHETIC}':")
    print("        type: 'MultivariateGaussian(Covariance)'")
    print('        observables: [ ' + ', '.join(f"'Lambda_b->Lambda_c::{ff}(q2)'" for ff, _ in grid()) + ' ]')
    print('        kinematics:  [ ' + ', '.join(f'{{ q2: {q2:5.1f} }}' for _, q2 in grid()) + ' ]')
    print('        options:     [ ' + ', '.join("{}" for _ in grid()) + ' ]')
    print('        means:       [ ' + ', '.join(f'{v:+.9f}' for v in y) + ' ]')
    print('        covariance: [ ' + ',\n                      '.join(
        '[ ' + ', '.join(f'{v:+.12e}' for v in row) + ' ]' for row in C) + ' ]')

    print('\n# --- priors')
    sigma = np.sqrt(np.diag(cov))
    for name, m, s in zip(SSE, alpha, sigma):
        lo, hi = m - 6.0 * s, m + 6.0 * s
        if name.endswith('_1'):
            lo, hi = max(lo, -12.0), min(hi, +12.0)
        entry = f"      - {{ 'parameter': 'Lambda_b->Lambda_c::{name}@SSE',"
        print(f"{entry:<68}" + f" 'min': {lo:8.2f}, 'max': {hi:8.2f}, 'type': 'uniform' }}")


if __name__ == '__main__':
    main()
