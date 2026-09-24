---
title: 'Determination of SSE form factor parameters for EOS v1.1'
id: '2026-05'
authors:
  - name: 'C. Bolognani'
    affiliation: 'Technische Universität Dortmund'
    email: 'carolina.bolognani@cern.ch'
  - name: 'N. Gubernari'
    affiliation: 'University of Bonn'
    email: 'nicogubernari@gmail.com'
  - name: 'F. Herren'
    affiliation: 'University of Zurich'
    email: 'florian.s.herren@gmail.com'
  - name: 'M. Kirk'
    affiliation: 'Institute for Particle Physics Phenomenology, Durham University'
    email: 'matthew.j.kirk@durham.ac.uk'
  - name: 'M. Reboud'
    affiliation: 'Laboratoire de Physique des 2 Infinis Irène Joliot-Curie'
    email: 'merilreboud@gmail.com'
  - name: 'D. van Dyk'
    affiliation: 'Institute for Particle Physics Phenomenology, Durham University'
    email: 'danny.van.dyk@gmail.com'
---

# Overview

This report was generated with EOS v1.0.21 from the analysis file
`analysis.yaml`.
It documents the determination of the `SSE` form-factor coefficients for
26 posteriors, grouped by
transition type. For each posterior it lists the local $p$ values of the individual
constraints (and the global $p$ value where the fit is over-constrained), together
with the posterior-predicted form factors overlaid on the input constraints.


# Pseudoscalar to pseudoscalar ($P \to P$)

## Posterior `B-to-D`


This posterior varies 5 `SSE` coefficients.
It is constrained by:

- `B->D::f_++f_0@FNAL+MILC:2015B`
- `B->D::f_++f_0@HPQCD:2015A`

> **Note.** No (lattice or LCSR) tensor form-factor data are available for this
> transition. The tensor coefficients are therefore not varied and retain their
> database default values; the tensor form factors below are not determined by this fit.

### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B->D::f_++f_0@FNAL+MILC:2015B` | 86.3% |
| `B->D::f_++f_0@HPQCD:2015A` | 74.2% |
| **total** ($\chi^2$ / d.o.f. $= 5.96$ / 7) | **54.5%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `B-to-D` (`B-to-D-f0`).](../figures/B-to-D-f0.pdf)

![Posterior-predicted form factor for `B-to-D` (`B-to-D-fp`).](../figures/B-to-D-fp.pdf)

```{=latex}
\clearpage
```

## Posterior `B-to-K`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `B->K::f_0+f_++f_T@FNAL+MILC:2015D`
- `B->K::f_0+f_++f_T@HPQCD:2013A`
- `B->K::f_0+f_++f_T@HPQCD:2022A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B->K::f_0+f_++f_T@FNAL+MILC:2015D` | 100.0% |
| `B->K::f_0+f_++f_T@HPQCD:2013A` | 75.9% |
| `B->K::f_0+f_++f_T@HPQCD:2022A` | 98.5% |
| **total** ($\chi^2$ / d.o.f. $= 8.56$ / 18) | **96.9%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `B-to-K` (`B-to-K-f0`).](../figures/B-to-K-f0.pdf)

![Posterior-predicted form factor for `B-to-K` (`B-to-K-fp`).](../figures/B-to-K-fp.pdf)

![Posterior-predicted form factor for `B-to-K` (`B-to-K-fT`).](../figures/B-to-K-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `B-to-eta`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `B->eta::f_0+f_++f_T@MR:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B->eta::f_0+f_++f_T@MR:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.00$ / 3) | **100.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `B-to-eta` (`B-to-eta-f0`).](../figures/B-to-eta-f0.pdf)

![Posterior-predicted form factor for `B-to-eta` (`B-to-eta-fp`).](../figures/B-to-eta-fp.pdf)

![Posterior-predicted form factor for `B-to-eta` (`B-to-eta-fT`).](../figures/B-to-eta-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `B-to-etaprime`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `B->eta_prime::f_0+f_++f_T@MR:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B->eta_prime::f_0+f_++f_T@MR:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.00$ / 3) | **100.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `B-to-etaprime` (`B-to-etaprime-f0`).](../figures/B-to-etaprime-f0.pdf)

![Posterior-predicted form factor for `B-to-etaprime` (`B-to-etaprime-fp`).](../figures/B-to-etaprime-fp.pdf)

![Posterior-predicted form factor for `B-to-etaprime` (`B-to-etaprime-fT`).](../figures/B-to-etaprime-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `B-to-pi`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `B->pi::f_++f_0+f_T@FNAL+MILC:2015C`
- `B->pi::f_++f_0@RBC+UKQCD:2015A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B->pi::f_++f_0+f_T@FNAL+MILC:2015C` | 99.7% |
| `B->pi::f_++f_0@RBC+UKQCD:2015A` | 57.7% |
| **total** ($\chi^2$ / d.o.f. $= 7.06$ / 9) | **63.1%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `B-to-pi` (`B-to-pi-f0`).](../figures/B-to-pi-f0.pdf)

![Posterior-predicted form factor for `B-to-pi` (`B-to-pi-fp`).](../figures/B-to-pi-fp.pdf)

![Posterior-predicted form factor for `B-to-pi` (`B-to-pi-fT`).](../figures/B-to-pi-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `Bs-to-Ds`


This posterior varies 5 `SSE` coefficients.
It is constrained by:

- `B_s->D_s::f_++f_0@HPQCD:2019A`

> **Note.** No (lattice or LCSR) tensor form-factor data are available for this
> transition. The tensor coefficients are therefore not varied and retain their
> database default values; the tensor form factors below are not determined by this fit.

### Goodness of fit

The table lists the local $p$ value of each constraint. The fit is saturated
(the number of data points equals the number of coefficients, d.o.f. $= 0$), so no
global $p$ value is defined.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B_s->D_s::f_++f_0@HPQCD:2019A` | 100.0% |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Bs-to-Ds` (`Bs-to-Ds-f0`).](../figures/Bs-to-Ds-f0.pdf)

![Posterior-predicted form factor for `Bs-to-Ds` (`Bs-to-Ds-fp`).](../figures/Bs-to-Ds-fp.pdf)

```{=latex}
\clearpage
```

## Posterior `Bs-to-K`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `B_s->K::f_++f_0@FNAL+MILC:2019A;rescale-factor=11.311`
- `B_s->K::f_++f_0@HPQCD:2014A;rescale-factor=11.311`
- `B_s->K::f_++f_0@RBC+UKQCD:2023A;rescale-factor=11.311`
- `B_s->K::FormFactors[f_+,f_0,f_T]@GvDV:2020A`

> **Note.** The lattice inputs for this transition are mutually inconsistent. Their
> covariances have been rescaled by the PDG factor $\mathcal{S}^2 = 11.311$
> (scale factor $\mathcal{S} = 3.36$),
> as indicated by the `;rescale-factor` option on the constraints above.

### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B_s->K::FormFactors[f_+,f_0,f_T]@GvDV:2020A` | 100.0% |
| `B_s->K::f_++f_0@FNAL+MILC:2019A` | 7.5% |
| `B_s->K::f_++f_0@HPQCD:2014A` | 99.4% |
| `B_s->K::f_++f_0@RBC+UKQCD:2023A` | 54.4% |
| **total** ($\chi^2$ / d.o.f. $= 19.69$ / 25) | **76.3%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Bs-to-K` (`Bs-to-K-f0`).](../figures/Bs-to-K-f0.pdf)

![Posterior-predicted form factor for `Bs-to-K` (`Bs-to-K-fp`).](../figures/Bs-to-K-fp.pdf)

![Posterior-predicted form factor for `Bs-to-K` (`Bs-to-K-fT`).](../figures/Bs-to-K-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `Bs-to-eta`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `B_s->eta::f_0+f_++f_T@MR:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B_s->eta::f_0+f_++f_T@MR:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.00$ / 3) | **100.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Bs-to-eta` (`Bs-to-eta-f0`).](../figures/Bs-to-eta-f0.pdf)

![Posterior-predicted form factor for `Bs-to-eta` (`Bs-to-eta-fp`).](../figures/Bs-to-eta-fp.pdf)

![Posterior-predicted form factor for `Bs-to-eta` (`Bs-to-eta-fT`).](../figures/Bs-to-eta-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `Bs-to-etaprime`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `B_s->eta_prime::f_0+f_++f_T@MR:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B_s->eta_prime::f_0+f_++f_T@MR:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.00$ / 3) | **100.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Bs-to-etaprime` (`Bs-to-etaprime-f0`).](../figures/Bs-to-etaprime-f0.pdf)

![Posterior-predicted form factor for `Bs-to-etaprime` (`Bs-to-etaprime-fp`).](../figures/Bs-to-etaprime-fp.pdf)

![Posterior-predicted form factor for `Bs-to-etaprime` (`Bs-to-etaprime-fT`).](../figures/Bs-to-etaprime-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `D-to-K`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `D->K::f_++f_0@ETM:2017B;rescale-factor=3.241`
- `D->K::f_T@ETM:2018A;rescale-factor=3.241`
- `D->K::f_0+f_++f_T@HPQCD:2022A;rescale-factor=3.241`
- `D->K::f_++f_0@FNALMILC:2022A;rescale-factor=3.241`

> **Note.** The lattice inputs for this transition are mutually inconsistent. Their
> covariances have been rescaled by the PDG factor $\mathcal{S}^2 = 3.241$
> (scale factor $\mathcal{S} = 1.80$),
> as indicated by the `;rescale-factor` option on the constraints above.

### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `D->K::f_++f_0@ETM:2017B` | 8.8% |
| `D->K::f_++f_0@FNALMILC:2022A` | 99.8% |
| `D->K::f_0+f_++f_T@HPQCD:2022A` | 53.7% |
| `D->K::f_T@ETM:2018A` | 8.3% |
| **total** ($\chi^2$ / d.o.f. $= 21.00$ / 13) | **7.3%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `D-to-K` (`D-to-K-f0`).](../figures/D-to-K-f0.pdf)

![Posterior-predicted form factor for `D-to-K` (`D-to-K-fp`).](../figures/D-to-K-fp.pdf)

![Posterior-predicted form factor for `D-to-K` (`D-to-K-fT`).](../figures/D-to-K-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `D-to-eta`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `D->eta::f_0+f_++f_T@MR:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `D->eta::f_0+f_++f_T@MR:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.02$ / 3) | **99.9%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `D-to-eta` (`D-to-eta-f0`).](../figures/D-to-eta-f0.pdf)

![Posterior-predicted form factor for `D-to-eta` (`D-to-eta-fp`).](../figures/D-to-eta-fp.pdf)

![Posterior-predicted form factor for `D-to-eta` (`D-to-eta-fT`).](../figures/D-to-eta-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `D-to-etaprime`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `D->eta_prime::f_0+f_++f_T@MR:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `D->eta_prime::f_0+f_++f_T@MR:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.02$ / 3) | **99.9%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `D-to-etaprime` (`D-to-etaprime-f0`).](../figures/D-to-etaprime-f0.pdf)

![Posterior-predicted form factor for `D-to-etaprime` (`D-to-etaprime-fp`).](../figures/D-to-etaprime-fp.pdf)

![Posterior-predicted form factor for `D-to-etaprime` (`D-to-etaprime-fT`).](../figures/D-to-etaprime-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `Ds-to-eta`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `D_s->eta::f_0+f_++f_T@MR:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `D_s->eta::f_0+f_++f_T@MR:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.07$ / 3) | **99.5%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Ds-to-eta` (`Ds-to-eta-f0`).](../figures/Ds-to-eta-f0.pdf)

![Posterior-predicted form factor for `Ds-to-eta` (`Ds-to-eta-fp`).](../figures/Ds-to-eta-fp.pdf)

![Posterior-predicted form factor for `Ds-to-eta` (`Ds-to-eta-fT`).](../figures/Ds-to-eta-fT.pdf)

```{=latex}
\clearpage
```

## Posterior `Ds-to-etaprime`


This posterior varies 8 `SSE` coefficients.
It is constrained by:

- `D_s->eta_prime::f_0+f_++f_T@MR:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `D_s->eta_prime::f_0+f_++f_T@MR:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.14$ / 3) | **98.7%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Ds-to-etaprime` (`Ds-to-etaprime-f0`).](../figures/Ds-to-etaprime-f0.pdf)

![Posterior-predicted form factor for `Ds-to-etaprime` (`Ds-to-etaprime-fp`).](../figures/Ds-to-etaprime-fp.pdf)

![Posterior-predicted form factor for `Ds-to-etaprime` (`Ds-to-etaprime-fT`).](../figures/Ds-to-etaprime-fT.pdf)

```{=latex}
\clearpage
```

# Pseudoscalar to vector ($P \to V$)

## Posterior `B-to-Dstar`


This posterior varies 17 `SSE` coefficients.
It is constrained by:

- `B->D^*::FormFactors@HPQCD:2023A`
- `B->D^*::FormFactors@FNAL+MILC:2021A`
- `B->D^*::FormFactors@JLQCD:2023A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B->D^*::FormFactors@FNAL+MILC:2021A` | 72.5% |
| `B->D^*::FormFactors@HPQCD:2023A` | 100.0% |
| `B->D^*::FormFactors@JLQCD:2023A` | 89.2% |
| **total** ($\chi^2$ / d.o.f. $= 20.76$ / 31) | **91.8%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `B-to-Dstar` (`B-to-Dstar-A0`).](../figures/B-to-Dstar-A0.pdf)

![Posterior-predicted form factor for `B-to-Dstar` (`B-to-Dstar-A1`).](../figures/B-to-Dstar-A1.pdf)

![Posterior-predicted form factor for `B-to-Dstar` (`B-to-Dstar-A12`).](../figures/B-to-Dstar-A12.pdf)

![Posterior-predicted form factor for `B-to-Dstar` (`B-to-Dstar-T1`).](../figures/B-to-Dstar-T1.pdf)

![Posterior-predicted form factor for `B-to-Dstar` (`B-to-Dstar-T2`).](../figures/B-to-Dstar-T2.pdf)

![Posterior-predicted form factor for `B-to-Dstar` (`B-to-Dstar-T23`).](../figures/B-to-Dstar-T23.pdf)

![Posterior-predicted form factor for `B-to-Dstar` (`B-to-Dstar-V`).](../figures/B-to-Dstar-V.pdf)

```{=latex}
\clearpage
```

## Posterior `B-to-Kstar`


This posterior varies 17 `SSE` coefficients.
It is constrained by:

- `B->K^*::A_1@HPQCD:2013B`
- `B->K^*::A_12@HPQCD:2013B`
- `B->K^*::V@HPQCD:2013B`
- `B->K^*::FormFactors[A_0,A_1,A_2,V,T_1,T_2,T_23]@GKvD:2018A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B->K^*::A_12@HPQCD:2013B` | 83.7% |
| `B->K^*::A_1@HPQCD:2013B` | 85.8% |
| `B->K^*::FormFactors[A_0,A_1,A_2,V,T_1,T_2,T_23]@GKvD:2018A` | 100.0% |
| `B->K^*::V@HPQCD:2013B` | 99.5% |
| **total** ($\chi^2$ / d.o.f. $= 1.69$ / 22) | **100.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `B-to-Kstar` (`B-to-Kstar-A0`).](../figures/B-to-Kstar-A0.pdf)

![Posterior-predicted form factor for `B-to-Kstar` (`B-to-Kstar-A1`).](../figures/B-to-Kstar-A1.pdf)

![Posterior-predicted form factor for `B-to-Kstar` (`B-to-Kstar-A12`).](../figures/B-to-Kstar-A12.pdf)

![Posterior-predicted form factor for `B-to-Kstar` (`B-to-Kstar-A2`).](../figures/B-to-Kstar-A2.pdf)

![Posterior-predicted form factor for `B-to-Kstar` (`B-to-Kstar-T1`).](../figures/B-to-Kstar-T1.pdf)

![Posterior-predicted form factor for `B-to-Kstar` (`B-to-Kstar-T2`).](../figures/B-to-Kstar-T2.pdf)

![Posterior-predicted form factor for `B-to-Kstar` (`B-to-Kstar-T23`).](../figures/B-to-Kstar-T23.pdf)

![Posterior-predicted form factor for `B-to-Kstar` (`B-to-Kstar-V`).](../figures/B-to-Kstar-V.pdf)

```{=latex}
\clearpage
```

## Posterior `B-to-rho`


This posterior varies 17 `SSE` coefficients.
It is constrained by:

- `B->rho::FormFactors[A_0,A_1,A_2,V,T_1,T_2,T_23]@GKvD:2018A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B->rho::FormFactors[A_0,A_1,A_2,V,T_1,T_2,T_23]@GKvD:2018A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.01$ / 16) | **100.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `B-to-rho` (`B-to-rho-A0`).](../figures/B-to-rho-A0.pdf)

![Posterior-predicted form factor for `B-to-rho` (`B-to-rho-A1`).](../figures/B-to-rho-A1.pdf)

![Posterior-predicted form factor for `B-to-rho` (`B-to-rho-A2`).](../figures/B-to-rho-A2.pdf)

![Posterior-predicted form factor for `B-to-rho` (`B-to-rho-T1`).](../figures/B-to-rho-T1.pdf)

![Posterior-predicted form factor for `B-to-rho` (`B-to-rho-T2`).](../figures/B-to-rho-T2.pdf)

![Posterior-predicted form factor for `B-to-rho` (`B-to-rho-T23`).](../figures/B-to-rho-T23.pdf)

![Posterior-predicted form factor for `B-to-rho` (`B-to-rho-V`).](../figures/B-to-rho-V.pdf)

```{=latex}
\clearpage
```

## Posterior `Bc-to-Jpsi`


This posterior varies 17 `SSE` coefficients.
It is constrained by:

- `B_c->J/psi::FormFactors@HPQCD:2025A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B_c->J/psi::FormFactors@HPQCD:2025A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 4.78$ / 7) | **68.7%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Bc-to-Jpsi` (`Bc-to-Jpsi-A0`).](../figures/Bc-to-Jpsi-A0.pdf)

![Posterior-predicted form factor for `Bc-to-Jpsi` (`Bc-to-Jpsi-A1`).](../figures/Bc-to-Jpsi-A1.pdf)

![Posterior-predicted form factor for `Bc-to-Jpsi` (`Bc-to-Jpsi-A12`).](../figures/Bc-to-Jpsi-A12.pdf)

![Posterior-predicted form factor for `Bc-to-Jpsi` (`Bc-to-Jpsi-T1`).](../figures/Bc-to-Jpsi-T1.pdf)

![Posterior-predicted form factor for `Bc-to-Jpsi` (`Bc-to-Jpsi-T2`).](../figures/Bc-to-Jpsi-T2.pdf)

![Posterior-predicted form factor for `Bc-to-Jpsi` (`Bc-to-Jpsi-T23`).](../figures/Bc-to-Jpsi-T23.pdf)

![Posterior-predicted form factor for `Bc-to-Jpsi` (`Bc-to-Jpsi-V`).](../figures/Bc-to-Jpsi-V.pdf)

```{=latex}
\clearpage
```

## Posterior `Bs-to-Dsstar`


This posterior varies 17 `SSE` coefficients.
It is constrained by:

- `B_s->D_s^*::FormFactors@HPQCD:2023A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B_s->D_s^*::FormFactors@HPQCD:2023A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 3.19$ / 7) | **86.7%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Bs-to-Dsstar` (`Bs-to-Dsstar-A0`).](../figures/Bs-to-Dsstar-A0.pdf)

![Posterior-predicted form factor for `Bs-to-Dsstar` (`Bs-to-Dsstar-A1`).](../figures/Bs-to-Dsstar-A1.pdf)

![Posterior-predicted form factor for `Bs-to-Dsstar` (`Bs-to-Dsstar-A12`).](../figures/Bs-to-Dsstar-A12.pdf)

![Posterior-predicted form factor for `Bs-to-Dsstar` (`Bs-to-Dsstar-T1`).](../figures/Bs-to-Dsstar-T1.pdf)

![Posterior-predicted form factor for `Bs-to-Dsstar` (`Bs-to-Dsstar-T2`).](../figures/Bs-to-Dsstar-T2.pdf)

![Posterior-predicted form factor for `Bs-to-Dsstar` (`Bs-to-Dsstar-T23`).](../figures/Bs-to-Dsstar-T23.pdf)

![Posterior-predicted form factor for `Bs-to-Dsstar` (`Bs-to-Dsstar-V`).](../figures/Bs-to-Dsstar-V.pdf)

```{=latex}
\clearpage
```

## Posterior `Bs-to-Kstar`


This posterior varies 17 `SSE` coefficients.
It is constrained by:

- `B_s->K^*::A_1@HPQCD:2013B`
- `B_s->K^*::A_12@HPQCD:2013B`
- `B_s->K^*::V@HPQCD:2013B`
- `B_s->K^*::FormFactors[A_0,A_1,A_2,V,T_1,T_2,T_23]@GvDV:2020A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B_s->K^*::A_12@HPQCD:2013B` | 96.0% |
| `B_s->K^*::A_1@HPQCD:2013B` | 63.3% |
| `B_s->K^*::FormFactors[A_0,A_1,A_2,V,T_1,T_2,T_23]@GvDV:2020A` | 100.0% |
| `B_s->K^*::V@HPQCD:2013B` | 29.5% |
| **total** ($\chi^2$ / d.o.f. $= 5.40$ / 22) | **100.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Bs-to-Kstar` (`Bs-to-Kstar-A0`).](../figures/Bs-to-Kstar-A0.pdf)

![Posterior-predicted form factor for `Bs-to-Kstar` (`Bs-to-Kstar-A1`).](../figures/Bs-to-Kstar-A1.pdf)

![Posterior-predicted form factor for `Bs-to-Kstar` (`Bs-to-Kstar-A12`).](../figures/Bs-to-Kstar-A12.pdf)

![Posterior-predicted form factor for `Bs-to-Kstar` (`Bs-to-Kstar-A2`).](../figures/Bs-to-Kstar-A2.pdf)

![Posterior-predicted form factor for `Bs-to-Kstar` (`Bs-to-Kstar-T1`).](../figures/Bs-to-Kstar-T1.pdf)

![Posterior-predicted form factor for `Bs-to-Kstar` (`Bs-to-Kstar-T2`).](../figures/Bs-to-Kstar-T2.pdf)

![Posterior-predicted form factor for `Bs-to-Kstar` (`Bs-to-Kstar-T23`).](../figures/Bs-to-Kstar-T23.pdf)

![Posterior-predicted form factor for `Bs-to-Kstar` (`Bs-to-Kstar-V`).](../figures/Bs-to-Kstar-V.pdf)

```{=latex}
\clearpage
```

## Posterior `Bs-to-phi`


This posterior varies 17 `SSE` coefficients.
It is constrained by:

- `B_s->phi::V+A_0+A_1+A_12@HLMW:2015A`
- `B_s->phi::T_1+T_2+T_23@HLMW:2015A`
- `B_s->phi::FormFactors[A_0,A_1,A_2,V,T_1,T_2,T_23]@GvDV:2020A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `B_s->phi::FormFactors[A_0,A_1,A_2,V,T_1,T_2,T_23]@GvDV:2020A` | 100.0% |
| `B_s->phi::T_1+T_2+T_23@HLMW:2015A` | 100.0% |
| `B_s->phi::V+A_0+A_1+A_12@HLMW:2015A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.91$ / 30) | **100.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Bs-to-phi` (`Bs-to-phi-A0`).](../figures/Bs-to-phi-A0.pdf)

![Posterior-predicted form factor for `Bs-to-phi` (`Bs-to-phi-A1`).](../figures/Bs-to-phi-A1.pdf)

![Posterior-predicted form factor for `Bs-to-phi` (`Bs-to-phi-A12`).](../figures/Bs-to-phi-A12.pdf)

![Posterior-predicted form factor for `Bs-to-phi` (`Bs-to-phi-A2`).](../figures/Bs-to-phi-A2.pdf)

![Posterior-predicted form factor for `Bs-to-phi` (`Bs-to-phi-T1`).](../figures/Bs-to-phi-T1.pdf)

![Posterior-predicted form factor for `Bs-to-phi` (`Bs-to-phi-T2`).](../figures/Bs-to-phi-T2.pdf)

![Posterior-predicted form factor for `Bs-to-phi` (`Bs-to-phi-T23`).](../figures/Bs-to-phi-T23.pdf)

![Posterior-predicted form factor for `Bs-to-phi` (`Bs-to-phi-V`).](../figures/Bs-to-phi-V.pdf)

```{=latex}
\clearpage
```

# Spin-1/2 to spin-1/2 ($1/2^+ \to 1/2^+$)

## Posterior `Lambdab-to-Lambda`


This posterior varies 25 `SSE` coefficients.
It is constrained by:

- `Lambda_b->Lambda::f_time+long+perp^V+A+T+T5[nominal,no-prior]@DM:2016A`


### Goodness of fit

The table lists the local $p$ value of each constraint. The fit is saturated
(the number of data points equals the number of coefficients, d.o.f. $= 0$), so no
global $p$ value is defined.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `Lambda_b->Lambda::f_time+long+perp^V+A+T+T5[nominal,no-prior]@DM:2016A` | 100.0% |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-f0A`).](../figures/Lambdab-to-Lambda-f0A.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-f0T`).](../figures/Lambdab-to-Lambda-f0T.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-f0T5`).](../figures/Lambdab-to-Lambda-f0T5.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-f0V`).](../figures/Lambdab-to-Lambda-f0V.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-fperpA`).](../figures/Lambdab-to-Lambda-fperpA.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-fperpT`).](../figures/Lambdab-to-Lambda-fperpT.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-fperpT5`).](../figures/Lambdab-to-Lambda-fperpT5.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-fperpV`).](../figures/Lambdab-to-Lambda-fperpV.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-ftA`).](../figures/Lambdab-to-Lambda-ftA.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambda` (`Lambdab-to-Lambda-ftV`).](../figures/Lambdab-to-Lambda-ftV.pdf)

```{=latex}
\clearpage
```

## Posterior `Lambdab-to-Lambdac`


This posterior varies 15 `SSE` coefficients.
It is constrained by:

- `Lambda_b->Lambda_c::f_time+long+perp^V+A+T+T5@DKMR:2017A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `Lambda_b->Lambda_c::f_time+long+perp^V+A+T+T5@DKMR:2017A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.12$ / 3) | **99.0%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-f0A`).](../figures/Lambdab-to-Lambdac-f0A.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-f0T`).](../figures/Lambdab-to-Lambdac-f0T.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-f0T5`).](../figures/Lambdab-to-Lambdac-f0T5.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-f0V`).](../figures/Lambdab-to-Lambdac-f0V.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-fperpA`).](../figures/Lambdab-to-Lambdac-fperpA.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-fperpT`).](../figures/Lambdab-to-Lambdac-fperpT.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-fperpT5`).](../figures/Lambdab-to-Lambdac-fperpT5.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-fperpV`).](../figures/Lambdab-to-Lambdac-fperpV.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-ftA`).](../figures/Lambdab-to-Lambdac-ftA.pdf)

![Posterior-predicted form factor for `Lambdab-to-Lambdac` (`Lambdab-to-Lambdac-ftV`).](../figures/Lambdab-to-Lambdac-ftV.pdf)

```{=latex}
\clearpage
```

## Posterior `Lambdac-to-Lambda`


This posterior varies 15 `SSE` coefficients.
It is constrained by:

- `Lambda_c->Lambda::f_time+long+perp^V+A@M:2016A`

> **Note.** No (lattice or LCSR) tensor form-factor data are available for this
> transition. The tensor coefficients are therefore not varied and retain their
> database default values; the tensor form factors below are not determined by this fit.

### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `Lambda_c->Lambda::f_time+long+perp^V+A@M:2016A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.01$ / 2) | **99.7%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Lambdac-to-Lambda` (`Lambdac-to-Lambda-f0A`).](../figures/Lambdac-to-Lambda-f0A.pdf)

![Posterior-predicted form factor for `Lambdac-to-Lambda` (`Lambdac-to-Lambda-f0V`).](../figures/Lambdac-to-Lambda-f0V.pdf)

![Posterior-predicted form factor for `Lambdac-to-Lambda` (`Lambdac-to-Lambda-fperpA`).](../figures/Lambdac-to-Lambda-fperpA.pdf)

![Posterior-predicted form factor for `Lambdac-to-Lambda` (`Lambdac-to-Lambda-fperpV`).](../figures/Lambdac-to-Lambda-fperpV.pdf)

![Posterior-predicted form factor for `Lambdac-to-Lambda` (`Lambdac-to-Lambda-ftA`).](../figures/Lambdac-to-Lambda-ftA.pdf)

![Posterior-predicted form factor for `Lambdac-to-Lambda` (`Lambdac-to-Lambda-ftV`).](../figures/Lambdac-to-Lambda-ftV.pdf)

```{=latex}
\clearpage
```

## Posterior `Lambdac-to-neutron`


This posterior varies 25 `SSE` coefficients.
It is constrained by:

- `Lambda_c->neutron::f_time+long+perp^V+A+T+T5[HO]@M:2017A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `Lambda_c->neutron::f_time+long+perp^V+A+T+T5[HO]@M:2017A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.07$ / 3) | **99.5%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-f0A`).](../figures/Lambdac-to-neutron-f0A.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-f0T`).](../figures/Lambdac-to-neutron-f0T.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-f0T5`).](../figures/Lambdac-to-neutron-f0T5.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-f0V`).](../figures/Lambdac-to-neutron-f0V.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-fperpA`).](../figures/Lambdac-to-neutron-fperpA.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-fperpT`).](../figures/Lambdac-to-neutron-fperpT.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-fperpT5`).](../figures/Lambdac-to-neutron-fperpT5.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-fperpV`).](../figures/Lambdac-to-neutron-fperpV.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-ftA`).](../figures/Lambdac-to-neutron-ftA.pdf)

![Posterior-predicted form factor for `Lambdac-to-neutron` (`Lambdac-to-neutron-ftV`).](../figures/Lambdac-to-neutron-ftV.pdf)

```{=latex}
\clearpage
```

## Posterior `Lambdac-to-proton`


This posterior varies 25 `SSE` coefficients.
It is constrained by:

- `Lambda_c->proton::f_time+long+perp^V+A+T+T5[HO]@M:2017A`


### Goodness of fit

The table lists the local $p$ value of each constraint together with the global $p$
value and total $\chi^2$ of the best-fit point.

| Constraint | local $p$ value |
|:-----------|----------------:|
| `Lambda_c->proton::f_time+long+perp^V+A+T+T5[HO]@M:2017A` | 100.0% |
| **total** ($\chi^2$ / d.o.f. $= 0.07$ / 3) | **99.5%** |

### Posterior-predicted form factors

The bands show the posterior-predicted form factors (`SSE`); the points show the
constraints entering the fit.

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-f0A`).](../figures/Lambdac-to-proton-f0A.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-f0T`).](../figures/Lambdac-to-proton-f0T.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-f0T5`).](../figures/Lambdac-to-proton-f0T5.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-f0V`).](../figures/Lambdac-to-proton-f0V.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-fperpA`).](../figures/Lambdac-to-proton-fperpA.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-fperpT`).](../figures/Lambdac-to-proton-fperpT.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-fperpT5`).](../figures/Lambdac-to-proton-fperpT5.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-fperpV`).](../figures/Lambdac-to-proton-fperpV.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-ftA`).](../figures/Lambdac-to-proton-ftA.pdf)

![Posterior-predicted form factor for `Lambdac-to-proton` (`Lambdac-to-proton-ftV`).](../figures/Lambdac-to-proton-ftV.pdf)

```{=latex}
\clearpage
```

