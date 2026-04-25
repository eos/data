# Analysis 2025-05
## Exploiting perpendicular momentum distributions of semileptonic decays

Authors: C. Earnshaw, B. Mitreska, D. van Dyk

### Contents

#### Ancillary Files

The files in this directory represent inputs and results of an EOS-based analysis of LHCb data on $\bar{B}_s^0\to D_s^+\mu^-\bar\nu$,
in particular the differential branching ratio with respect to the perpendicular momentum projection of the $D_s^+$.

 - ``analysis.yaml``: Definition and description of the analysis, including a theory-only posterior (``FF-only``) and data-driven posteriors (``FF-shape``, ``FF-shape-Projection``, and ``CKM``) for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.19.
   The samples are stored as ``eos.ImportanceSamples`` and ``eos.Predictions`` objects and can be loaded directly in EOS.

 - ``figures``: Figures produced in the course of the analysis. Both PDF and PNG formats are available.

 - ``output``: Binary output generated in the course of the analysis. Three response matrices are stored here in row-major ordering in NumPy's ``npz`` format.

#### Figures

<table>
<tr>
  <th>Figure</th>
  <th>Caption</th>
</tr>
<tr>
  <th colspan="2">Main Material</th>
</tr>
<tr>
  <td><a href="figures/theory-vs-reconstructed.pdf?raw=true"><img src="/figures/theory-vs-reconstructed.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The rate of $\bar{B}_s^0\to D_s^+\mu^-\bar\nu$ as obtained by the LHCb experiment [LHCb:2020cyw](https://dx.doi.org/10.1103/PhysRevD.101.072004) including
   detector effects (black error bars labelled as LHCb 2020) overlaid with with our theoretical prediction eq. (2.5) in bins of $k_\perp$ (shown as blue bands).
  </td>
</tr>
<tr>
  <td><a href="figures/efficiency_fit.pdf?raw=true"><img src="/figures/efficiency_fit.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The efficiency as documented in the supplementary material [LHCb-2019-041-CDS](https://cds.cern.ch/record/2706102/) of the LHCb measurement
   [LHCb:2020cyw](https://dx.doi.org/10.1103/PhysRevD.101.072004) (black errorbars). We fit the efficiency with a Legendre polynomial of degree three (blue curve).
  </td>
</tr>
<tr>
  <td><a href="figures/resolution_fit.pdf?raw=true"><img src="/figures/resolution_fit.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The resolution as documented in the supplementary material [LHCb-2019-041-CDS](https://cds.cern.ch/record/2706102/) of the LHCb measurement
   [LHCb:2020cyw](https://dx.doi.org/10.1103/PhysRevD.101.072004) (black errorbars). We fit the resolution with a double-sided Crystal Ball density (blue curve).
  </td>
</tr>
<tr>
  <td><a href="figures/showcase-detector-effects.pdf?raw=true"><img src="/figures/showcase-detector-effects.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The rate of $\bar{B}_s^0\to D_s^+\mu^-\bar\nu$ as obtained from the LHCb experiment [LHCb:2020cyw](https://dx.doi.org/10.1103/PhysRevD.101.072004)
   including detector effects (black error bars, labelled LHCb 2020). It is overlaid with with our theory-level prediction eq. (2.5) in bins of
   $k_\perp$ (blue bands) and our detector level prediction obtained by multiplication with the response matrix eq. (3.14) obtained from the full
   acceptance function $A$ (orange bands).
  </td>
</tr>
<tr>
  <td><a href="figures/comparison-response-matrices.pdf?raw=true"><img src="/figures/comparison-response-matrices.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The variability of the forward folding by plotting the detector-level effect using two different response matrices $R_\text{flat}$ (gray bands)
   and $R$ (orange bands). The lack of variation of the response matrix indicates little to no dependence on the underlying signal model.
  </td>
</tr>
<tr>
  <td><a href="figures/projection-results.pdf?raw=true"><img src="/figures/projection-results.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The one-dimensional marginal posterior distributions the ratios of form factor parameters $\alpha_1^{(+)}/\alpha_0^{(+)}$ and $\alpha_2^{(+)}/\alpha_0^{(+)}$,
   accompanied by their joint two-dimensional marginal posterior distribution. Curves show the posterior density, and shared areas/contours indicate the central
   interval/region at $68\%$ probability (prior information: gray curves, areas, and contours; LHCb Run-3 projection: dashed red curves, areas, and contours).
  </td>
</tr>
<tr>
  <th colspan="2">Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/ff-shape-current-vs-projection.pdf?raw=true"><img src="/figures/ff-shape-current-vs-projection.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison of the determinations of the form factor parameters from the current data set (blue curves and contours) and from the projected data set at the
   end of LHCb run 3 (orange curves and contours). For the fits, $|V_{cb}|$ is fixed to $39\times 10^{-3}$.
  </td>
</tr>
</table>
