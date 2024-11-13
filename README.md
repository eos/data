# Analysis 2023-09
## Towards a Global Analysis of the $b \to c\bar{u} q$ Puzzle

Authors: S. Meiser, D. van Dyk, J. Virto

### Contents

#### Ancillary Files

The files in this directory represent inputs and approximations to the results of an EOS-based analysis
of exclusive $\bar{B}_s^0\to D_s^{(\*)+} \pi^-$ and $\bar{B}^0\to D^{(\*)+} K^-$ decays.

 - ``analysis.yaml``: Definition and description of the entire analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
   - The posteriors ``SM`` and ``WET-1`` to ``WET-4`` provide the nominal results of the analysis.
   - The posterior ``TH`` provides supplementary results.
   - The various prediction sets were used to produce some of the figures listed below.

 - ``likelihood.yaml``: Definition and description of the full experimental likelihood discussed in the paper and depicted in the figure ``likelihood``.

 - ``form-factors.yaml``: Definition and description of the posterior for the Heavy Quark Expansion (HQE) parameters for the $\bar{B}\to D^{(*)}$ form factors,
   corresponding to the results of [Bordone, Gubernari, Jung, van Dyk 2019](https://doi.org/10.1140/epjc/s10052-020-7850-9).

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.13.
   The samples are stored as ``eos.ImportanceSamples`` and ``eos.Predictions`` objects and can be loaded directly in EOS.

 - ``figures``: Ancillary and supplementary figures produced in the course of the analysis. Both PDF and PNG formats are available.

 - ``tables``: Tables produced in the course of the analysis.

 - ``scripts``: Scripts and other inputs files used to produce the figures and tables.

#### Figures

<table>
<tr>
  <th>Figure</th>
  <th>Caption</th>
</tr>
<tr>
  <th colspan=2>Main Material</th>
</tr>
<tr>
  <td><a href="figures/likelihood.pdf?raw=true"><img src="/figures/likelihood.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Selection of one-dimensional and two-dimensional marginal likelihoods arising from the global
   likelihood as described in Table 1. We choose to display the branching ratios $\mathcal{B}(\bar{B}_s\to D_s^{(*)} \pi)$
   and the hadronisation fraction $f_s/f_d$ for the LHCb phase at $7$ TeV centre-of-mass energy.
   Our choice highlights the non-Gaussian nature of the full likelihood and illustrates the effects of our Gaussian approximation.
  </td>
</tr>
<tr>
  <td><a href="figures/BR-comparison.pdf?raw=true"><img src="/figures/BR-comparison.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison of the branching ratios of the nonleptonic decays in units of the experimentally
measured branching ratios. We show the theory-based prior prediction (<code>TH</code>) and the various posterior postdictions
for the fit models <code>SM</code> and <code>WET-1</code> to <code>WET-4</code>. In the BSM-like models, the two modes A and B are
shown separately. The tension between the prior predictions and the SM postdiction on the one hand and the
measurements on the other is clearly visible. All intervals shown correspond to the central intervals at 68%
probability.
  </td>
</tr>
<tr>
  <td><a href="figures/lifetime-comparison.pdf?raw=true"><img src="/figures/lifetime-comparison.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison of the lifetime bound saturation.
   We show the various posterior postdictions
   for the fit models <code>WET-1</code> to <code>WET-4</code>,
   where the two modes A and B are shown separately.
   We show the upper bounds at 95% probability.
  </td>
</tr>
<tr>
  <td><a href="figures/WET-1.pdf?raw=true"><img src="/figures/WET-1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   One-dimensional and two-dimensional marginal posterior PDFs for the four parameters of interest
of the <code>WET-1</code> model. The “+” and the solid black lines show the SM point. The coloured areas are
the central 68%, 95%, and 99% integrated probability contours of the posterior distribution obtained from a
kernel density estimation. Blue areas belong to mode A, while orange areas belong to mode B. The boundaries
due to the lifetime constraint are illustrated as green ellipses.
  </td>
</tr>
<tr>
  <td><a href="figures/WET-2.pdf?raw=true"><img src="/figures/WET-2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   One-dimensional and two-dimensional marginal posterior PDFs for the six parameters of interest
of the <code>WET-2</code> model. The “+” and the solid black lines show the SM point. The coloured areas are
the central 68%, 95%, and 99% integrated probability contours of the posterior distribution obtained from a
kernel density estimation. Blue areas belong to mode A, while orange areas belong to mode B. The boundaries
due to the lifetime constraint are illustrated as green ellipses.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/WET-3.pdf?raw=true"><img src="/figures/WET-3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   One-dimensional and two-dimensional marginal posterior PDFs for the four parameters of interest
of the <code>WET-3</code> model. The “+” and the solid black lines show the SM point. The coloured areas are
the central 68%, 95%, and 99% integrated probability contours of the posterior distribution obtained from a
kernel density estimation. Blue areas belong to mode A, while orange areas belong to mode B. The boundaries
due to the lifetime constraint are illustrated as green ellipses.
  </td>
</tr>
<tr>
  <td><a href="figures/WET-4.pdf?raw=true"><img src="/figures/WET-4.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   One-dimensional and two-dimensional marginal posterior PDFs for the six parameters of interest
of the <code>WET-4</code> model. The “+” and the solid black lines show the SM point. The coloured areas are
the central 68%, 95%, and 99% integrated probability contours of the posterior distribution obtained from a
kernel density estimation. Blue areas belong to mode A, while orange areas belong to mode B. The boundaries
due to the lifetime constraint are illustrated as green ellipses.
  </td>
</tr>
<tr>
  <td><a href="figures/BR-corner-WET-1.pdf?raw=true"><img src="/figures/BR-corner-WET-1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   One-dimensional and two-dimensional marginal posterior-predictive PDFs for the four branching ratios of interested,
   obtained from the <code>WET-1</code> posterior. The coloured areas are
the central 68%, 95%, and 99% integrated probability contours of the posterior distribution obtained from a
kernel density estimation. Blue areas belong to mode A, while orange areas belong to mode B.
  </td>
</tr>
<tr>
  <td><a href="figures/BR-corner-WET-2.pdf?raw=true"><img src="/figures/BR-corner-WET-2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   One-dimensional and two-dimensional marginal posterior-predictive PDFs for the four branching ratios of interested,
   obtained from the <code>WET-2</code> posterior. The coloured areas are
the central 68%, 95%, and 99% integrated probability contours of the posterior distribution obtained from a
kernel density estimation. Blue areas belong to mode A, while orange areas belong to mode B.
  </td>
</tr>
<tr>
  <td><a href="figures/BR-corner-WET-3.pdf?raw=true"><img src="/figures/BR-corner-WET-3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   One-dimensional and two-dimensional marginal posterior-predictive PDFs for the four branching ratios of interested,
   obtained from the <code>WET-3</code> posterior. The coloured areas are
the central 68%, 95%, and 99% integrated probability contours of the posterior distribution obtained from a
kernel density estimation. Blue areas belong to mode A, while orange areas belong to mode B.
  </td>
</tr>
<tr>
  <td><a href="figures/BR-corner-WET-4.pdf?raw=true"><img src="/figures/BR-corner-WET-4.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   One-dimensional and two-dimensional marginal posterior-predictive PDFs for the four branching ratios of interested,
   obtained from the <code>WET-4</code> posterior. The coloured areas are
the central 68%, 95%, and 99% integrated probability contours of the posterior distribution obtained from a
kernel density estimation. Blue areas belong to mode A, while orange areas belong to mode B.
  </td>
</tr>
</table>
