# Analysis A2025-02
## B_(s) -> eta^(’) and D_(s) -> eta^(’) form factors

Authors: B. Melic, M. Reboud

### Contents

#### Ancillary Files

The files in this directory represent inputs and approximations to the results of an EOS-based analysis
of the phenomenology of B_(s) -> eta^(’) and D_(s) -> eta^(’) form factors.

 - ``analysis.yaml``: Definition and description of the entire analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
   - The posteriors ``BToeta``, ``BToeta_prime``, ``BsToeta`` and ``BsToeta_prime`` provide the nominal results for the conformal expansion of B_(s) -> eta^(’)  form factors.
   - The posteriors ``DToeta``, ``DToeta_prime``, ``DsToeta`` and ``DsToeta_prime`` provide the nominal results for the conformal expansion of D_(s) -> eta^(’)  form factors.
   - The posterior ``BToeta_BFW`` provide the result of a unitary bounded conformal expansion of the B -> eta  form factors.
   - The posteriors ``BsToetas`` and ``BsToetas_LQCD`` are used to cross-check the results of the LCSR calculation against LQCD estimates.
   - The posteriors ``BToetaeta_prime`` and ``DToetaeta_prime`` are used to investigate correlations between the eta and eta' from factors.
   - The posteriors ``BToetalnu``, ``DToetalnu``, ``DToeta_primelnu``, ``DsToetalnu`` and ``DsToeta_primelnu`` provide the nominal results for the phenomenology study of the corresponding decays.
   - The posteriors ``Vub``, ``Vcd`` and ``Vcs`` provide the nominal results for the extraction of these CKM elements from experimental data.
   - The various prediction sets were used to produce all the figures and predictions of the paper.

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.17.
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
  <td><a href="figures/BToEtaEtaPrime_fp.pdf?raw=true"><img src="/figures/BToEtaEtaPrime_fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $B \to \eta^{(\prime)}$ $f^+$ form factors obtained with posterior <code>BToeta</code> and <code>BToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToEtaEtaPrime_f0.pdf?raw=true"><img src="/figures/BToEtaEtaPrime_f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $B \to \eta^{(\prime)}$ $f^0$ form factors obtained with posterior <code>BToeta</code> and <code>BToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToEtaEtaPrime_fT.pdf?raw=true"><img src="/figures/BToEtaEtaPrime_fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $B \to \eta^{(\prime)}$ $f^T$ form factors obtained with posterior <code>BToeta</code> and <code>BToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToEtaEtaPrime_fp.pdf?raw=true"><img src="/figures/BsToEtaEtaPrime_fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $B_s \to \eta^{(\prime)}$ $f^+$ form factors obtained with posterior <code>BsToeta</code> and <code>BsToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToEtaEtaPrime_f0.pdf?raw=true"><img src="/figures/BsToEtaEtaPrime_f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $B_s \to \eta^{(\prime)}$ $f^0$ form factors obtained with posterior <code>BsToeta</code> and <code>BsToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToEtaEtaPrime_fT.pdf?raw=true"><img src="/figures/BsToEtaEtaPrime_fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $B_s \to \eta^{(\prime)}$ $f^T$ form factors obtained with posterior <code>BsToeta</code> and <code>BsToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/DToEtaEtaPrime_fp.pdf?raw=true"><img src="/figures/DToEtaEtaPrime_fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $D \to \eta^{(\prime)}$ $f^+$ form factors obtained with posterior <code>DToeta</code> and <code>DToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/DToEtaEtaPrime_f0.pdf?raw=true"><img src="/figures/DToEtaEtaPrime_f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $D \to \eta^{(\prime)}$ $f^0$ form factors obtained with posterior <code>DToeta</code> and <code>DToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/DToEtaEtaPrime_fT.pdf?raw=true"><img src="/figures/DToEtaEtaPrime_fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $D \to \eta^{(\prime)}$ $f^T$ form factors obtained with posterior <code>DToeta</code> and <code>DToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/DsToEtaEtaPrime_fp.pdf?raw=true"><img src="/figures/DsToEtaEtaPrime_fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $D_s \to \eta^{(\prime)}$ $f^+$ form factors obtained with posterior <code>DsToeta</code> and <code>DsToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/DsToEtaEtaPrime_f0.pdf?raw=true"><img src="/figures/DsToEtaEtaPrime_f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $D_s \to \eta^{(\prime)}$ $f^0$ form factors obtained with posterior <code>DsToeta</code> and <code>DsToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/DsToEtaEtaPrime_fT.pdf?raw=true"><img src="/figures/DsToEtaEtaPrime_fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Summary plot of our results for the $D_s \to \eta^{(\prime)}$ $f^T$ form factors obtained with posterior <code>DsToeta</code> and <code>DsToeta_prime</code>.
   The error bars correspond to the LCSR results.
   The shaded areas are the $1\sigma$ uncertainty bands of our conformal extrapolation with a truncation order $N=2$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToEtas_fp.pdf?raw=true"><img src="/figures/BsToEtas_fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between our results for unphysical $B_s \to \eta_s$ $f^+$ form factors and the LQCD estimates of our Ref. [17].
   This figure is obtained using the posteriors <code>BsToetas</code> and <code>BsToetas_LQCD</code>.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToEtas_f0.pdf?raw=true"><img src="/figures/BsToEtas_f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between our results for unphysical $B_s \to \eta_s$ $f^0$ form factors and the LQCD estimates of our Ref. [17].
   This figure is obtained using the posteriors <code>BsToetas</code> and <code>BsToetas_LQCD</code>.
  </td>
</tr>
<tr>
  <td><a href="figures/Vcd.pdf?raw=true"><img src="/figures/Vcd.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginalized posteriors for the CKM parameters $V_{cd}$ obtained with a Kernel Density Estimate.
   The filled regions correspond to the centred 68\% probability intervals.
   The dashed lines show the total posterior using sum rules instead of lattice inputs for the decay constants.
   The grey line corresponds to the current world averages.
   This figure is obtained using the posteriors <code>Vcd</code>.
  </td>
</tr>
<tr>
  <td><a href="figures/Vcs.pdf?raw=true"><img src="/figures/Vcs.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginalized posteriors for the CKM parameters $V_{cs}$ obtained with a Kernel Density Estimate.
   The filled regions correspond to the centred 68\% probability intervals.
   The dashed lines show the total posterior using sum rules instead of lattice inputs for the decay constants.
   The grey line corresponds to the current world averages.
   This figure is obtained using the posteriors <code>Vcs</code>.
  </td>
</tr>
<tr>
  <td><a href="figures/Vub.pdf?raw=true"><img src="/figures/Vub.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginalized posteriors for the CKM parameters $|V_{ub}|$ obtained with a Kernel Density Estimate.
   The filled regions correspond to the centred 68\% probability intervals.
   The dashed lines show the total posterior using sum rules instead of lattice inputs for the decay constants.
   The grey line corresponds to the current world averages.
   This figure is obtained using the posteriors <code>Vub</code>.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/D_etalnu.pdf?raw=true"><img src="/figures/D_etalnu.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between our fit results for the differential $D\to\eta\ell\nu$ BR and some experimental measurements (listed in the appendix of the paper).
   The bands correspond to $1\sigma$ uncertainty intervals for the normalised differential branching ratios.
  </td>
</tr>
<tr>
  <td><a href="figures/D_etaPlnu.pdf?raw=true"><img src="/figures/D_etaPlnu.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between our fit results for the differential $D\to\eta'\ell\nu$ BR and some experimental measurements (listed in the appendix of the paper).
   The bands correspond to $1\sigma$ uncertainty intervals for the normalised differential branching ratios.
  </td>
</tr>
<tr>
  <td><a href="figures/Ds_etalnu.pdf?raw=true"><img src="/figures/Ds_etalnu.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between our fit results for the differential $D_s\to\eta\ell\nu$ BR and some experimental measurements (listed in the appendix of the paper).
   The bands correspond to $1\sigma$ uncertainty intervals for the normalised differential branching ratios.
  </td>
</tr>
<tr>
  <td><a href="figures/Ds_etaPlnu.pdf?raw=true"><img src="/figures/Ds_etaPlnu.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between our fit results for the differential $D_s\to\eta'\ell\nu$ BR and some experimental measurements (listed in the appendix of the paper).
   The bands correspond to $1\sigma$ uncertainty intervals for the normalised differential branching ratios.
  </td>
</tr>
<tr>
  <td><a href="figures/B_etalnu.pdf?raw=true"><img src="/figures/B_etalnu.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between our fit results for the differential $B\to\eta\ell\nu$ BR and some experimental measurements (listed in the appendix of the paper).
   The bands correspond to $1\sigma$ uncertainty intervals for the normalised differential branching ratios.
  </td>
</tr>
</table>