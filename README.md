# Analysis 2022-05
## Toward a complete description of $\boldsymbol{b \to u \ell^- \bar\nu}$ decays within the Weak Effective Theory

Authors: D. Leljak, B. Melic, F. Novak, M. Reboud, D. van Dyk

### Contents

#### Ancillary Files

The files in this directory represent input and approximations to the results of an analysis
of exclusive $\bar{B} \to \lbrace \pi, \rho, \omega\rbrace \ell^-\bar\nu$ decays.

 - ``b-to-u-l-nu.yaml``: Definition and description of the entire analysis for use with the ``eos-analysis`` command-line tool.
   - The posteriors labelled ``SM-all``, ``CKM-all``, and ``WET-all`` provide the nominal results of the analysis.
   - The posteriors labelled ``CKM-pi``, ``CKM-rho``, and ``CKM-omega`` provide supplementary results.
   - The various prediction sets were used to diagnose the quality and inputs of the fits, including predictions for leptonic B decays in the CKM and WET models.

 - ``ublnu-wet-LMNRvD2023.yaml``: Description of a Gaussian mixture density approximating the results of the fit within the WET fit model.
   The file contents follows the standard EOS format for a mixture density.

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.8.
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
  <td><a href="figures/CKM-comparison-Vub.pdf?raw=true"><img src="/figures/CKM-comparison-Vub.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginalised one-dimensional posterior densities for $\vert V_{ub}\vert$ within the CKM fit model.
   We show our nominal result for the full data set in blue.
   Additional results for datasets only containing either $\bar{B}\to \pi\ell^-\bar\nu$, $\bar{B}\to \rho\ell^-\bar\nu$, and $\bar{B}\to \omega\ell^-\bar\nu$ are shown in orange, green, and red.
   The shaded areas indicate the central intervals at $68\%$ probability.
  </td>
</tr>
<tr>
  <td><a href="figures/WET-all-interest.pdf?raw=true"><img src="/figures/WET-all-interest.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Corner plot of all one-dimensional and two-dimensional marginalised posterior densities within the WET fit model for the five parameters of interest.
   We show our nominal result for the full data set.
   The ''+'' and the solid black lines show the SM point ${C}_i = \delta_{i, (V,L)}$. The ''x'' and the dashed black lines show the two best-fit points.
   The blue areas are the $1, 2$ and $3 \sigma$ contours of the posterior distribution obtained from a kernel density estimation.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/CKM-B-to-pi-l-nu.pdf?raw=true"><img src="/figures/CKM-B-to-pi-l-nu.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Experimental data on $\bar{B}\to \pi\ell^-\bar\nu$ in comparison to posterior-predictive results for posteriors <code>CKM-all</code> and <code>CKM-pi</code>.</td>
</tr>
<tr>
  <td><a href="figures/CKM-B-to-rho-l-nu.pdf?raw=true"><img src="/figures/CKM-B-to-rho-l-nu.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Experimental data on $\bar{B}\to \rho\ell^-\bar\nu$ in comparison to posterior-predictive results for posteriors <code>CKM-all</code> and <code>CKM-rho</code>.</td>
</tr>
<tr>
  <td><a href="figures/CKM-B-to-omega-l-nu.pdf?raw=true"><img src="/figures/CKM-B-to-omega-l-nu.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Experimental data on $\bar{B}\to \omega\ell^-\bar\nu$ in comparison to posterior-predictive results for posteriors <code>CKM-all</code> and <code>CKM-omega</code>.</td>
</tr>
<tr>
  <td><a href="figures/CKM-extended-comparison.pdf?raw=true"><img src="/figures/CKM-extended-comparison.png?raw=true" width="1000px" height="auto"></a></td>
  <td>Marginalised one-dimensional posterior densities for $\vert V_{ub}\vert$ within the CKM fit model as in figure <code>CKM-comparison</code> juxtaposed with the poster-prediction for the integrated branching ratios of $\bar{B}\to \pi\ell^-\bar\nu$, $\bar{B}\to \rho\ell^-\bar\nu$, and $\bar{B}\to \omega\ell^-\bar\nu$ shown in orange, green, and red.
   The shaded areas indicate the central intervals at $68\%$ probability.</td>
</tr>
<tr>
  <td><a href="figures/WET-all-GMM.pdf?raw=true"><img src="/figures/WET-all-GMM.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Corner plot of all one-dimensional and two-dimensional marginalised posterior densities within the WET fit model for the five parameters of interest.
   We show our nominal result for the full data set.
   The ''+'' and the solid black lines show the SM point ${C}_i = \delta_{i, (V,L)}$.
   The ''x'' and the dashed black lines show the two best-fit points.
   The blue components represent the Gaussian mixture density that best fit our posterior samples.
   The transparence of the components gives a visual representation of the components weight.
   The description of the mixture is given in the ancillary file <code>ublnu-wet-LMNRvD2023.yaml</code>.
  </td>
</tr>

</table>
