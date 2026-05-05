# Analysis-2024-03
## Extracting fragmentation fractions from exclusive semi-leptonic decays

Authors: C. Bolognani, M. Jung, M. Reboud, K. K. Vos

### Contents

#### Ancillary Files

The files in this directory contain the necessary ingredients to reproduce the predictions and cross-checks of the main paper.

 - ``analysis.yaml``: Definition and description of the entire analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
   - The posterior ``BqToDq`` provides the nominal results for the analysis of `B_(s) -> D_(s)^(*) l nu` decays.
   - The posterior ``BqToDq-NP`` provides the nominal results for the NP analysis.
   - The posterior ``bToc`` provides the nominal results for the simultaneous analysis of `B_(s) -> D_(s)^(*) l nu` and `B_c -> J/psi l nu` decays.

 - ``outputs``: Ancillary and supplementary figures produced in the course of the analysis, for which both PDF and PNG formats are available, and means and covariance matrix for the NP analysis.

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
  <td><a href="outputs/ratios.pdf"><img src="/outputs/ratios.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Ratios $R_{sd}^D$, $R_{sd}^{D*}$ and $R_{cd}^{D*}$ as functions of the squared momentum transfer q2. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="outputs/corner-plot.pdf"><img src="/outputs/corner-plot.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Corner plot of our predictions for the (integrated) ratios $R_{sd}^D$, $R_{sd}^{D*}$, $R_{cd}^{D*}$ and $R_{cd}^{D}$.
  </td>
</tr>
<tr>
  <td><a href="outputs/BToP_ffs.pdf"><img src="/outputs/BToP_ffs.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Output of the BGL fit to the B_(s)-to-pseudoscalar form factors, excluding the tensor form factors (which are not needed for our main results).
  </td>
</tr>
<tr>
  <td><a href="outputs/BToV_ffs.pdf"><img src="/outputs/BToV_ffs.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Output of the BGL fit to the B_(s)-to-vector form factors.
  </td>
</tr>
<tr>
  <td><a href="outputs/BcToJpsi_ffs.pdf"><img src="/outputs/BcToJpsi_ffs.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Output of the BGL fit to the $B_c\to J/\psi$ form factors.
  </td>
</tr>
<tr>
  <td><a href="outputs/saturations.pdf"><img src="/outputs/saturations.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Saturation of the dispersive bounds in the fit to $B_{(s)} \to D_{(s)}^{(*)}$ and $B_c\to J/\psi$ form factors (posterior <code>bToc</code>).
  </td>
</tr>
</table>
