# Analysis 2024-02
## A Simple Parametrisation of the Pion Form Factor

Authors: M.Kirk, B. Kubis, M. Reboud, D. van Dyk

### Contents

#### Ancillary Files

The files in this directory represent inputs and approximations to the results of an EOS-based analysis
of the isospin $I=1$ projection of the pion electromagnetic form factor.

 - ``analysis.yaml``: Definition and description of the entire analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
   - The posterior ``FF-fp-I1-order5`` provides the nominal results of the analysis.
   - The posteriors ``FF-fp-I1-order1`` to ``FF-fp-I1-order4`` provide supplementary results.
   - The various prediction sets were used to produce figure 1 and to determine the entries of table 1.

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.13.
   The samples are stored as ``eos.ImportanceSamples`` and ``eos.Predictions`` objects and can be loaded directly in EOS.

 - ``figures``: Main and supplementary figures produced in the course of the analysis. Both PDF and PNG formats are available.

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
  <td><a href="figures/FF-fp2-I1-all.pdf?raw=true"><img src="/figures/FF-fp2-I1-all.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The squared magnitude of the form factor $F_\pi^{I=1}(q^2)$.
   We show the envelope at 68% probability for truncation $N = 5$ juxtaposed with data by the
   Belle, CLEO, and NA7 experiments. A single data point by
   the JLab-F<sub>&pi;</sub> experiment at $q^2 = −2.45 \text{GeV}^2$ is not shown
   but agrees within $0.8 \sigma$ with the best-fit curve. Data points
   in the shaded region ($q^2 \geq 1 \text{GeV}^2$) are not fitted. However,
   we extend the posterior-prediction of the $N = 5$ fit into this
   region as two dashed curves, indicating only the 68% envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-arg-fp-I1-timelike-with-data.pdf?raw=true"><img src="/figures/FF-arg-fp-I1-timelike-with-data.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The phase of the form factor $F_\pi^{I=1}(q^2)$.
   We show the envelope at 68% probability for truncation $N = 5$ obtained from a fit to data by the
   Belle, CLEO, JLab-F<sub>&pi;</sub>, and NA7 experiments in the region $q^2 < 1 \text{GeV}^2$.
   We extend the posterior-prediction of the $N = 5$ fit into the region $q^2 \geq 1 \text{GeV}^2$
   as two dashed curves, indicating only the 68% envelope.
   For reference, we overlay our phase predictions with the input from <a href="https://doi.org/10.1007/JHEP02(2019)006">Colangelo, Hoferichter, Stoffer 2018</a>.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/rho-mass-width.pdf?raw=true"><img src="/figures/rho-mass-width.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The mass and total decay width of the $\rho(770)$ meson. We show the contours at 68% and 95% probability for truncations $N=3$ to $N=5$.
   For reference, we overlay our results with world average as published by the <a href="https://doi.org/10.1103/PhysRevD.110.030001">Particle Data Group (PDG)</a>.
  </td>
</tr>
<tr>
  <td><a href="figures/FF-arg-fp-I1-timelike.pdf?raw=true"><img src="/figures/FF-arg-fp-I1-timelike.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   The phase of the form factor $F_\pi^{I=1}(q^2)$.
   We show the envelope at 68% probability for truncation $N = 5$ obtained from a fit to data by the
   Belle, CLEO, JLab-F<sub>&pi;</sub>, and NA7 experiments in the region $q^2 < 1 \text{GeV}^2$.
   We extend the posterior-prediction of the $N = 5$ fit into the region $q^2 \geq 1 \text{GeV}^2$
   as two dashed curves, indicating only the 68% envelope.
  </td>
</tr>
</table>
