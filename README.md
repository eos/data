# Analysis-2023-08
## Semileptonic Charm Decays in the Weak Effective Theory

Authors: C. Bolognani, M. Reboud, D. van Dyk, K.K. Vos

### Contents

#### Ancillary Files

The files in this directory represent input and approximations to the results of an analysis
of exclusive $c \to s \ell^+\nu$ decays.

 - ``analysis.yaml``: Definition and description of the entire analysis for use with the ``eos-analysis`` command-line tool.
   - The posteriors labelled ``SM-all``, ``CKM-all``, and ``WET-all`` provide the nominal results of the analysis.
   - The posteriors labelled ``SM-all-rescaled``, ``CKM-all-rescaled``, and ``WET-all-rescaled`` provide the analysis results for the “scale factor“ scenario.
   - The posteriors labelled ``CKM-Ds-Dstar-to-l-nu``, ``CKM-D-to-K-l-nu``, and ``CKM-Lc-to-L-l-nu`` provide supplementary results.
   - The various prediction sets were used to produce the various figures and diagnose the quality and inputs of the fits.

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.12.
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
  <td><a href="figures/FF-D-to-K-fp.pdf?raw=true"><img src="/figures/FF-D-to-K-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $D\to \bar{K}$ form factor $f_+$ as function of the
squared momentum transfer $q^2$ at truncation order K = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-D-to-K-fz.pdf?raw=true"><img src="/figures/FF-D-to-K-fz.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $D\to \bar{K}$ form factor $f_0$ as function of the
squared momentum transfer $q^2$ at truncation order K = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-D-to-K-ft.pdf?raw=true"><img src="/figures/FF-D-to-K-ft.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $D\to \bar{K}$ form factor $f_T$ as function of the
squared momentum transfer $q^2$ at truncation order K = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BR-comparison.pdf?raw=true"><img src="/figures/BR-comparison.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Comparison of the predictions in our “nominal” scenario for the branching ratios
  of $D_s^+\to \ell^+\nu$, $D^{+(0)}\to K_S^0(K^-)\ell^+\nu$, and $\Lambda_c\to \Lambda\ell^+\nu$ decays.
  </td>
</tr>
<tr>
  <td><a href="figures/CKM-comparison-Vcs-nominal.pdf?raw=true"><img src="/figures/CKM-comparison-Vcs-nominal.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Marginalised one-dimensional posterior densities for $\vert V_{cs}\vert$ within the CKM fit model, comparing the individual experimental likelihoods.
  </td>
</tr>
<tr>
  <td><a href="figures/CKM-comparison-Vcs-scenarios.pdf?raw=true"><img src="/figures/CKM-comparison-Vcs-scenarios.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Marginalised one-dimensional posterior densities for $\vert V_{cs}\vert$ within the CKM fit model, comparing the nominal and scale factor scenarios.
  </td>
</tr>
<tr>
  <td><a href="figures/WET-all.pdf?raw=true"><img src="/figures/WET-all.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Marginalised 1D- and 2D-posterior distributions for the 9 parameters of interest of our WET
model in the nominal scenario.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/WET-all-rescaled.pdf?raw=true"><img src="/figures/WET-all-rescaled.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Marginalised 1D- and 2D-posterior distributions for the 9 parameters of interest of our WET
model in the scale factor scenario.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-fperpV.pdf?raw=true"><img src="/figures/FF-Lc-to-L-fperpV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{\perp,V}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-flongV.pdf?raw=true"><img src="/figures/FF-Lc-to-L-flongV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{0,V}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-ftimeV.pdf?raw=true"><img src="/figures/FF-Lc-to-L-ftimeV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{t,V}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-fperpA.pdf?raw=true"><img src="/figures/FF-Lc-to-L-fperpA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{\perp,A}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-flongA.pdf?raw=true"><img src="/figures/FF-Lc-to-L-flongA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{0,A}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-ftimeA.pdf?raw=true"><img src="/figures/FF-Lc-to-L-ftimeA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{t,A}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-fperpT.pdf?raw=true"><img src="/figures/FF-Lc-to-L-fperpT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{\perp,T}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-flongT.pdf?raw=true"><img src="/figures/FF-Lc-to-L-flongT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{0,T}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-fperpT5.pdf?raw=true"><img src="/figures/FF-Lc-to-L-fperpT5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{\perp,T5}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-Lc-to-L-flongT5.pdf?raw=true"><img src="/figures/FF-Lc-to-L-flongT5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Prior-predictive distributions for the $\Lambda_c\to \Lambda$ form factor $f_{0,T5}$ as function of the
squared momentum transfer $q^2$ at truncation order K = 2.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-saturation-0mA.pdf?raw=true"><img src="/figures/FF-saturation-0mA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Posterior-predictive distributions of the saturation of the $J^P = 0^-$ bound for the axial current in the nominal scenario.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-saturation-1pA.pdf?raw=true"><img src="/figures/FF-saturation-1pA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Posterior-predictive distributions of the saturation of the $J^P = 1^+$ bound for the axial current in the nominal scenario.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-saturation-0pV.pdf?raw=true"><img src="/figures/FF-saturation-0pV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Posterior-predictive distributions of the saturation of the $J^P = 0^+$ bound for the vector current in the nominal scenario.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-saturation-1mV.pdf?raw=true"><img src="/figures/FF-saturation-1mV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Posterior-predictive distributions of the saturation of the $J^P = 1^-$ bound for the longitudinally polarized vector current in the nominal scenario.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-saturation-1mT.pdf?raw=true"><img src="/figures/FF-saturation-1mT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Posterior-predictive distributions of the saturation of the $J^P = 1^-$ bound for the tensor current in the nominal scenario.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-saturation-1pT5.pdf?raw=true"><img src="/figures/FF-saturation-1pT5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
  Posterior-predictive distributions of the saturation of the $J^P = 1^+$ bound for the tensor current in the nominal scenario.
  </td>
</tr>
</table>