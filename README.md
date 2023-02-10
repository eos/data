# Analysis-2024-01
## Detailed $SU(3)$ Flavour Symmetry Analysis of Charmless Two-Body $B$-Meson Decays Including Factorizable Corrections

Authors: M. Burgos Marcos, M. Reboud, K. K. Vos

N.B.: For simplicity, a slightly modified version of EOS was used in the context of this analysis.
Please contact the authors if you want to run this analysis.

### Contents

#### Ancillary Files

The files in this directory represent inputs and approximations to the results of an EOS-based analysis
of nonleptonic B decays

 - ``analysis.yaml``: Definition and description of the entire analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
   - The posterior ``Topological_no_eta_CKM`` provides the nominal results of the $SU(3)_F$ analysis.
   - The posterior ``QCDF_no_eta_CKM`` provide the nominal results of the analysis in the new parametrisation.
   - The various prediction sets were used to produce some of the figures listed below.

 - ``form-factor-analysis.yaml``: Definition and description of the ancillary form factor analysis.

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.14.
   The samples are stored as ``eos.ImportanceSamples`` and ``eos.Predictions`` objects and can be loaded directly in EOS.

 - ``figures``: Ancillary and supplementary figures produced in the course of the analysis. Both PDF and PNG formats are available.

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
  <td><a href="figures/dtheta.pdf?raw=true"><img src="/figures/dtheta.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   $68\%$ probability intervals of the (partially correlated) experimental constraints on the $B_d^0\to\pi^+\pi^-$ and $B_s^0\to K^+K^-$
   CP observables in the $(r_p, \theta_p)$ plane defined in the paper.
   The $1, 2$ and $3 \sigma$ postdictions of the global <code>Topological_no_eta_CKM</code> fit are overlaid; see the paper for details.
   The grey star and cross show the best-fit points from the CP asymmetries of $B_d^0\to\pi^+\pi^-$ and $B_s^0\to K^+K^-$, respectively.
  </td>
</tr>
<tr>
  <td><a href="figures/BRrelations.pdf?raw=true"><img src="/figures/BRrelations.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   $68\%$ probability intervals of the experimental constraints on the $B^+\to K^+\bar{K}^0$ and $B^+\to K^0\pi^+$ branching ratios.
   The $1, 2$ and $3 \sigma$ postdictions of the global <code>Topological_no_eta_CKM</code> fit are overlaid; see the paper for details.
   The $SU(3)_F$ symmetry excludes the grey region.
  </td>
</tr>
<tr>
  <td><a href="figures/BRs.pdf?raw=true"><img src="/figures/BRs.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Predicted observables within our fit models, combined with the measured values.
   The branching ratios and their ratios are normalized to their <code>QCDF_no_eta_CKM</code> postdictions for readability.
   Grey measurements are not directly used in the fit (ratios of branching ratios are used instead).
  </td>
</tr>
<tr>
  <td><a href="figures/ACPs.pdf?raw=true"><img src="/figures/ACPs.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Predicted observables within our fit models, combined with the measured values.
   The branching ratios and their ratios are normalized to their <code>QCDF_no_eta_CKM</code> postdictions for readability.
   Grey measurements are not directly used in the fit (ratios of branching ratios are used instead).
  </td>
</tr>
<tr>
  <td><a href="figures/SCPs.pdf?raw=true"><img src="/figures/SCPs.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Predicted observables within our fit models, combined with the measured values.
   The branching ratios and their ratios are normalized to their <code>QCDF_no_eta_CKM</code> postdictions for readability.
   Grey measurements are not directly used in the fit (ratios of branching ratios are used instead).
  </td>
</tr>
<tr>
  <td><a href="figures/BRratios.pdf?raw=true"><img src="/figures/BRratios.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Predicted observables within our fit models, combined with the measured values.
   The branching ratios and their ratios are normalized to their <code>QCDF_no_eta_CKM</code> postdictions for readability.
   Grey measurements are not directly used in the fit (ratios of branching ratios are used instead).
  </td>
</tr>
<tr>
  <td><a href="figures/alpha12.pdf?raw=true"><img src="/figures/alpha12.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   68\%, 95\% and 99\% cumulative contours of the $\tilde\alpha_1 + \tilde\alpha_2$ posterior distribution, assuming $\tilde\alpha_1 + \alpha_4^u > 0$.
   The $\times$ symbol shows the analysis best-fit point.
   We overlay the QCDF result for $\alpha_1 + \alpha_2$ obtained in Ref. [Beneke:2009ek].
  </td>
</tr>
<tr>
  <td><a href="figures/corner_plot_alpha.pdf?raw=true"><img src="/figures/corner_plot_alpha.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Corner plot of one-dimensional and two-dimensional marginalised posterior densities for the several $\alpha$ contributions.
   The ``$\times$'' symbol and the dashed black lines show the analysis best-fit point.
   The orange areas are the 1, 2 and $3\sigma$ contours of the posterior distribution obtained from a kernel density estimation.
  </td>
</tr>
<tr>
  <td><a href="figures/broken_dtheta.pdf?raw=true"><img src="/figures/broken_dtheta.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   $68\%$ probability intervals of the (partially correlated) experimental constraints on the $B_d^0\to K^+\pi^-$ and $B_s^0\to \pi^+K^-$
   CP observables and ratio of branching ratio in the $(r, \theta)$ plane defined in the paper.
   The $1, 2$ and $3 \sigma$ postdictions of our fit are overlaid.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/BRs_eta.pdf?raw=true"><img src="/figures/BRs_eta.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Predicted branching ratios of the decays involving $\eta$ mesons in the <code>Topological_no_eta_CKM</code> analysis.
   The few known measurements are in grey; they are not used in our fits.
  </td>
</tr>
<tr>
  <td><a href="figures/ACPs_eta.pdf?raw=true"><img src="/figures/ACPs_eta.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Predicted direct CP asymmetries of the decays involving $\eta$ mesons in the <code>Topological_no_eta_CKM</code> analysis.
   The few known measurements are in grey; they are not used in our fits.
  </td>
</tr>
<tr>
  <td><a href="figures/SCPs_eta.pdf?raw=true"><img src="/figures/SCPs_eta.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Predicted mixing induced CP asymmetries of the decays involving $\eta$ mesons in the <code>Topological_no_eta_CKM</code> analysis.
   The few known measurements are in grey; they are not used in our fits.
  </td>
</tr>
</table>
