# Analysis-2026-05
## Determination of SSE form factor parameters for EOS v1.1

Authors: C. Bolognani, N. Gubernari, F. Herren, M. Kirk, M. Reboud, D. van Dyk

### Contents

#### Ancillary Files

The files in this directory contain the necessary ingredients to reproduce the fits and predictions of the SSE form-factor parameters that serve as defaults in EOS v1.1.

 - ``analysis.yaml``: Definition and description of the entire analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
   Each posterior provides the nominal results for the SSE form-factor parameters of the eponymous transition:
   - Pseudoscalar to pseudoscalar transitions: ``B-to-D``, ``B-to-K``, ``B-to-eta``, ``B-to-etaprime``, ``B-to-pi``, ``Bs-to-Ds``, ``Bs-to-K``, ``Bs-to-eta``, ``Bs-to-etaprime``, ``D-to-K``, ``D-to-eta``, ``D-to-etaprime``, ``Ds-to-eta``, ``Ds-to-etaprime``.
   - Pseudoscalar to vector transitions: ``B-to-Dstar``, ``B-to-Kstar``, ``B-to-rho``, ``Bc-to-Jpsi``, ``Bs-to-Dsstar``, ``Bs-to-Kstar``, ``Bs-to-phi``.
   - Spin-1/2 to spin-1/2 transitions: ``Lambdab-to-Lambda``, ``Lambdab-to-Lambdac``, ``Lambdac-to-Lambda``, ``Lambdac-to-neutron``, ``Lambdac-to-proton``.

 - ``data``: Results of the analysis for each posterior ``<transition>``.
   - ``data/<transition>/nested``: Dynesty nested-sampling results.
   - ``data/<transition>/samples``: Weighted posterior samples obtained from the nested sampling.
   - ``data/<transition>/mode-default``: Best-fit point and goodness-of-fit information.
   - Posterior-predictive samples of the form factors are not included due to their size; they can be regenerated with the ``<transition>.predict`` steps of ``analysis.yaml``.

 - ``figures``: Figures produced in the course of the analysis, for which both PDF and PNG formats are available.

 - ``reports``: Report listing the constraints, goodness of fit, and form-factor predictions for every posterior (``report.pdf``), generated from the template ``report.md.jinja`` via ``report.md``.

 - ``scripts``: Auxiliary scripts.
   - ``generate-sse-snippet.py``: Produces the EOS parameter-database entries for the fitted SSE coefficients of a transition.
   - ``generate-lambdab-to-lambdac.py``: Converts the DKMR:2017A constraint into synthetic $\Lambda_b \to \Lambda_c$ form-factor values and generates the corresponding blocks of ``analysis.yaml``.

#### Figures

<table>
<tr>
  <th>Figure</th>
  <th>Caption</th>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B \to D$</th>
</tr>
<tr>
  <td><a href="figures/B-to-D-marginals.pdf"><img src="/figures/B-to-D-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B \to D$ (posterior <code>B-to-D</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-D-fp.pdf"><img src="/figures/B-to-D-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-D-f0.pdf"><img src="/figures/B-to-D-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B \to K$</th>
</tr>
<tr>
  <td><a href="figures/B-to-K-marginals.pdf"><img src="/figures/B-to-K-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B \to K$ (posterior <code>B-to-K</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-K-fp.pdf"><img src="/figures/B-to-K-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-K-f0.pdf"><img src="/figures/B-to-K-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-K-fT.pdf"><img src="/figures/B-to-K-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B \to \eta$</th>
</tr>
<tr>
  <td><a href="figures/B-to-eta-marginals.pdf"><img src="/figures/B-to-eta-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B \to \eta$ (posterior <code>B-to-eta</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-eta-fp.pdf"><img src="/figures/B-to-eta-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \eta$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-eta-f0.pdf"><img src="/figures/B-to-eta-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \eta$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-eta-fT.pdf"><img src="/figures/B-to-eta-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \eta$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B \to \eta^\prime$</th>
</tr>
<tr>
  <td><a href="figures/B-to-etaprime-marginals.pdf"><img src="/figures/B-to-etaprime-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B \to \eta^\prime$ (posterior <code>B-to-etaprime</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-etaprime-fp.pdf"><img src="/figures/B-to-etaprime-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \eta^\prime$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-etaprime-f0.pdf"><img src="/figures/B-to-etaprime-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \eta^\prime$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-etaprime-fT.pdf"><img src="/figures/B-to-etaprime-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \eta^\prime$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B \to \pi$</th>
</tr>
<tr>
  <td><a href="figures/B-to-pi-marginals.pdf"><img src="/figures/B-to-pi-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B \to \pi$ (posterior <code>B-to-pi</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-pi-fp.pdf"><img src="/figures/B-to-pi-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \pi$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-pi-f0.pdf"><img src="/figures/B-to-pi-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \pi$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-pi-fT.pdf"><img src="/figures/B-to-pi-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \pi$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B_s \to D_s$</th>
</tr>
<tr>
  <td><a href="figures/Bs-to-Ds-marginals.pdf"><img src="/figures/Bs-to-Ds-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B_s \to D_s$ (posterior <code>Bs-to-Ds</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Ds-fp.pdf"><img src="/figures/Bs-to-Ds-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Ds-f0.pdf"><img src="/figures/Bs-to-Ds-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B_s \to K$</th>
</tr>
<tr>
  <td><a href="figures/Bs-to-K-marginals.pdf"><img src="/figures/Bs-to-K-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B_s \to K$ (posterior <code>Bs-to-K</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-K-fp.pdf"><img src="/figures/Bs-to-K-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-K-f0.pdf"><img src="/figures/Bs-to-K-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-K-fT.pdf"><img src="/figures/Bs-to-K-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B_s \to \eta$</th>
</tr>
<tr>
  <td><a href="figures/Bs-to-eta-marginals.pdf"><img src="/figures/Bs-to-eta-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B_s \to \eta$ (posterior <code>Bs-to-eta</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-eta-fp.pdf"><img src="/figures/Bs-to-eta-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \eta$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-eta-f0.pdf"><img src="/figures/Bs-to-eta-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \eta$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-eta-fT.pdf"><img src="/figures/Bs-to-eta-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \eta$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $B_s \to \eta^\prime$</th>
</tr>
<tr>
  <td><a href="figures/Bs-to-etaprime-marginals.pdf"><img src="/figures/Bs-to-etaprime-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B_s \to \eta^\prime$ (posterior <code>Bs-to-etaprime</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-etaprime-fp.pdf"><img src="/figures/Bs-to-etaprime-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \eta^\prime$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-etaprime-f0.pdf"><img src="/figures/Bs-to-etaprime-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \eta^\prime$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-etaprime-fT.pdf"><img src="/figures/Bs-to-etaprime-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \eta^\prime$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $D \to K$</th>
</tr>
<tr>
  <td><a href="figures/D-to-K-marginals.pdf"><img src="/figures/D-to-K-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $D \to K$ (posterior <code>D-to-K</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-K-fp.pdf"><img src="/figures/D-to-K-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to K$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-K-f0.pdf"><img src="/figures/D-to-K-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to K$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-K-fT.pdf"><img src="/figures/D-to-K-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to K$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $D \to \eta$</th>
</tr>
<tr>
  <td><a href="figures/D-to-eta-marginals.pdf"><img src="/figures/D-to-eta-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $D \to \eta$ (posterior <code>D-to-eta</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-eta-fp.pdf"><img src="/figures/D-to-eta-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to \eta$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-eta-f0.pdf"><img src="/figures/D-to-eta-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to \eta$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-eta-fT.pdf"><img src="/figures/D-to-eta-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to \eta$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $D \to \eta^\prime$</th>
</tr>
<tr>
  <td><a href="figures/D-to-etaprime-marginals.pdf"><img src="/figures/D-to-etaprime-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $D \to \eta^\prime$ (posterior <code>D-to-etaprime</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-etaprime-fp.pdf"><img src="/figures/D-to-etaprime-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to \eta^\prime$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-etaprime-f0.pdf"><img src="/figures/D-to-etaprime-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to \eta^\prime$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/D-to-etaprime-fT.pdf"><img src="/figures/D-to-etaprime-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D \to \eta^\prime$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $D_s \to \eta$</th>
</tr>
<tr>
  <td><a href="figures/Ds-to-eta-marginals.pdf"><img src="/figures/Ds-to-eta-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $D_s \to \eta$ (posterior <code>Ds-to-eta</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Ds-to-eta-fp.pdf"><img src="/figures/Ds-to-eta-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D_s \to \eta$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Ds-to-eta-f0.pdf"><img src="/figures/Ds-to-eta-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D_s \to \eta$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Ds-to-eta-fT.pdf"><img src="/figures/Ds-to-eta-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D_s \to \eta$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to pseudoscalar: $D_s \to \eta^\prime$</th>
</tr>
<tr>
  <td><a href="figures/Ds-to-etaprime-marginals.pdf"><img src="/figures/Ds-to-etaprime-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $D_s \to \eta^\prime$ (posterior <code>Ds-to-etaprime</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Ds-to-etaprime-fp.pdf"><img src="/figures/Ds-to-etaprime-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D_s \to \eta^\prime$ form factor $f_+$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Ds-to-etaprime-f0.pdf"><img src="/figures/Ds-to-etaprime-f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D_s \to \eta^\prime$ form factor $f_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Ds-to-etaprime-fT.pdf"><img src="/figures/Ds-to-etaprime-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $D_s \to \eta^\prime$ form factor $f_T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to vector: $B \to D^*$</th>
</tr>
<tr>
  <td><a href="figures/B-to-Dstar-marginals.pdf"><img src="/figures/B-to-Dstar-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B \to D^*$ (posterior <code>B-to-Dstar</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Dstar-V.pdf"><img src="/figures/B-to-Dstar-V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D^*$ form factor $V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Dstar-A0.pdf"><img src="/figures/B-to-Dstar-A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D^*$ form factor $A_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Dstar-A1.pdf"><img src="/figures/B-to-Dstar-A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D^*$ form factor $A_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Dstar-A12.pdf"><img src="/figures/B-to-Dstar-A12.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D^*$ form factor $A_{12}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Dstar-T1.pdf"><img src="/figures/B-to-Dstar-T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D^*$ form factor $T_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Dstar-T2.pdf"><img src="/figures/B-to-Dstar-T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D^*$ form factor $T_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Dstar-T23.pdf"><img src="/figures/B-to-Dstar-T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to D^*$ form factor $T_{23}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to vector: $B \to K^*$</th>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-marginals.pdf"><img src="/figures/B-to-Kstar-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B \to K^*$ (posterior <code>B-to-Kstar</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-V.pdf"><img src="/figures/B-to-Kstar-V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K^*$ form factor $V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-A0.pdf"><img src="/figures/B-to-Kstar-A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K^*$ form factor $A_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-A1.pdf"><img src="/figures/B-to-Kstar-A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K^*$ form factor $A_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-A2.pdf"><img src="/figures/B-to-Kstar-A2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K^*$ form factor $A_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-A12.pdf"><img src="/figures/B-to-Kstar-A12.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K^*$ form factor $A_{12}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-T1.pdf"><img src="/figures/B-to-Kstar-T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K^*$ form factor $T_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-T2.pdf"><img src="/figures/B-to-Kstar-T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K^*$ form factor $T_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-Kstar-T23.pdf"><img src="/figures/B-to-Kstar-T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to K^*$ form factor $T_{23}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to vector: $B \to \rho$</th>
</tr>
<tr>
  <td><a href="figures/B-to-rho-marginals.pdf"><img src="/figures/B-to-rho-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B \to \rho$ (posterior <code>B-to-rho</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-rho-V.pdf"><img src="/figures/B-to-rho-V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \rho$ form factor $V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-rho-A0.pdf"><img src="/figures/B-to-rho-A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \rho$ form factor $A_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-rho-A1.pdf"><img src="/figures/B-to-rho-A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \rho$ form factor $A_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-rho-A2.pdf"><img src="/figures/B-to-rho-A2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \rho$ form factor $A_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-rho-T1.pdf"><img src="/figures/B-to-rho-T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \rho$ form factor $T_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-rho-T2.pdf"><img src="/figures/B-to-rho-T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \rho$ form factor $T_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/B-to-rho-T23.pdf"><img src="/figures/B-to-rho-T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B \to \rho$ form factor $T_{23}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to vector: $B_c \to J/\psi$</th>
</tr>
<tr>
  <td><a href="figures/Bc-to-Jpsi-marginals.pdf"><img src="/figures/Bc-to-Jpsi-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B_c \to J/\psi$ (posterior <code>Bc-to-Jpsi</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Bc-to-Jpsi-V.pdf"><img src="/figures/Bc-to-Jpsi-V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_c \to J/\psi$ form factor $V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bc-to-Jpsi-A0.pdf"><img src="/figures/Bc-to-Jpsi-A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_c \to J/\psi$ form factor $A_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bc-to-Jpsi-A1.pdf"><img src="/figures/Bc-to-Jpsi-A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_c \to J/\psi$ form factor $A_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bc-to-Jpsi-A12.pdf"><img src="/figures/Bc-to-Jpsi-A12.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_c \to J/\psi$ form factor $A_{12}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bc-to-Jpsi-T1.pdf"><img src="/figures/Bc-to-Jpsi-T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_c \to J/\psi$ form factor $T_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bc-to-Jpsi-T2.pdf"><img src="/figures/Bc-to-Jpsi-T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_c \to J/\psi$ form factor $T_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bc-to-Jpsi-T23.pdf"><img src="/figures/Bc-to-Jpsi-T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_c \to J/\psi$ form factor $T_{23}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to vector: $B_s \to D_s^*$</th>
</tr>
<tr>
  <td><a href="figures/Bs-to-Dsstar-marginals.pdf"><img src="/figures/Bs-to-Dsstar-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B_s \to D_s^*$ (posterior <code>Bs-to-Dsstar</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Dsstar-V.pdf"><img src="/figures/Bs-to-Dsstar-V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s^*$ form factor $V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Dsstar-A0.pdf"><img src="/figures/Bs-to-Dsstar-A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s^*$ form factor $A_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Dsstar-A1.pdf"><img src="/figures/Bs-to-Dsstar-A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s^*$ form factor $A_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Dsstar-A12.pdf"><img src="/figures/Bs-to-Dsstar-A12.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s^*$ form factor $A_{12}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Dsstar-T1.pdf"><img src="/figures/Bs-to-Dsstar-T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s^*$ form factor $T_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Dsstar-T2.pdf"><img src="/figures/Bs-to-Dsstar-T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s^*$ form factor $T_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Dsstar-T23.pdf"><img src="/figures/Bs-to-Dsstar-T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to D_s^*$ form factor $T_{23}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to vector: $B_s \to K^*$</th>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-marginals.pdf"><img src="/figures/Bs-to-Kstar-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B_s \to K^*$ (posterior <code>Bs-to-Kstar</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-V.pdf"><img src="/figures/Bs-to-Kstar-V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K^*$ form factor $V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-A0.pdf"><img src="/figures/Bs-to-Kstar-A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K^*$ form factor $A_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-A1.pdf"><img src="/figures/Bs-to-Kstar-A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K^*$ form factor $A_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-A2.pdf"><img src="/figures/Bs-to-Kstar-A2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K^*$ form factor $A_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-A12.pdf"><img src="/figures/Bs-to-Kstar-A12.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K^*$ form factor $A_{12}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-T1.pdf"><img src="/figures/Bs-to-Kstar-T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K^*$ form factor $T_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-T2.pdf"><img src="/figures/Bs-to-Kstar-T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K^*$ form factor $T_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-Kstar-T23.pdf"><img src="/figures/Bs-to-Kstar-T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to K^*$ form factor $T_{23}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Pseudoscalar to vector: $B_s \to \phi$</th>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-marginals.pdf"><img src="/figures/Bs-to-phi-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $B_s \to \phi$ (posterior <code>Bs-to-phi</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-V.pdf"><img src="/figures/Bs-to-phi-V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \phi$ form factor $V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-A0.pdf"><img src="/figures/Bs-to-phi-A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \phi$ form factor $A_0$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-A1.pdf"><img src="/figures/Bs-to-phi-A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \phi$ form factor $A_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-A2.pdf"><img src="/figures/Bs-to-phi-A2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \phi$ form factor $A_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-A12.pdf"><img src="/figures/Bs-to-phi-A12.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \phi$ form factor $A_{12}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-T1.pdf"><img src="/figures/Bs-to-phi-T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \phi$ form factor $T_1$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-T2.pdf"><img src="/figures/Bs-to-phi-T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \phi$ form factor $T_2$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Bs-to-phi-T23.pdf"><img src="/figures/Bs-to-phi-T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $B_s \to \phi$ form factor $T_{23}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Spin-1/2 to spin-1/2: $\Lambda_b \to \Lambda$</th>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-marginals.pdf"><img src="/figures/Lambdab-to-Lambda-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $\Lambda_b \to \Lambda$ (posterior <code>Lambdab-to-Lambda</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-ftV.pdf"><img src="/figures/Lambdab-to-Lambda-ftV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_t^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-f0V.pdf"><img src="/figures/Lambdab-to-Lambda-f0V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_0^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-fperpV.pdf"><img src="/figures/Lambdab-to-Lambda-fperpV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_\perp^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-ftA.pdf"><img src="/figures/Lambdab-to-Lambda-ftA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_t^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-f0A.pdf"><img src="/figures/Lambdab-to-Lambda-f0A.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_0^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-fperpA.pdf"><img src="/figures/Lambdab-to-Lambda-fperpA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_\perp^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-f0T.pdf"><img src="/figures/Lambdab-to-Lambda-f0T.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_0^T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-fperpT.pdf"><img src="/figures/Lambdab-to-Lambda-fperpT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_\perp^T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-f0T5.pdf"><img src="/figures/Lambdab-to-Lambda-f0T5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_0^{T5}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambda-fperpT5.pdf"><img src="/figures/Lambdab-to-Lambda-fperpT5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda$ form factor $f_\perp^{T5}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Spin-1/2 to spin-1/2: $\Lambda_b \to \Lambda_c$</th>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-marginals.pdf"><img src="/figures/Lambdab-to-Lambdac-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $\Lambda_b \to \Lambda_c$ (posterior <code>Lambdab-to-Lambdac</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-ftV.pdf"><img src="/figures/Lambdab-to-Lambdac-ftV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_t^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-f0V.pdf"><img src="/figures/Lambdab-to-Lambdac-f0V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_0^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-fperpV.pdf"><img src="/figures/Lambdab-to-Lambdac-fperpV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_\perp^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-ftA.pdf"><img src="/figures/Lambdab-to-Lambdac-ftA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_t^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-f0A.pdf"><img src="/figures/Lambdab-to-Lambdac-f0A.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_0^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-fperpA.pdf"><img src="/figures/Lambdab-to-Lambdac-fperpA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_\perp^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-f0T.pdf"><img src="/figures/Lambdab-to-Lambdac-f0T.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_0^T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-fperpT.pdf"><img src="/figures/Lambdab-to-Lambdac-fperpT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_\perp^T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-f0T5.pdf"><img src="/figures/Lambdab-to-Lambdac-f0T5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_0^{T5}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdab-to-Lambdac-fperpT5.pdf"><img src="/figures/Lambdab-to-Lambdac-fperpT5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_b \to \Lambda_c$ form factor $f_\perp^{T5}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Spin-1/2 to spin-1/2: $\Lambda_c \to \Lambda$</th>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-Lambda-marginals.pdf"><img src="/figures/Lambdac-to-Lambda-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $\Lambda_c \to \Lambda$ (posterior <code>Lambdac-to-Lambda</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-Lambda-ftV.pdf"><img src="/figures/Lambdac-to-Lambda-ftV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to \Lambda$ form factor $f_t^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-Lambda-f0V.pdf"><img src="/figures/Lambdac-to-Lambda-f0V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to \Lambda$ form factor $f_0^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-Lambda-fperpV.pdf"><img src="/figures/Lambdac-to-Lambda-fperpV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to \Lambda$ form factor $f_\perp^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-Lambda-ftA.pdf"><img src="/figures/Lambdac-to-Lambda-ftA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to \Lambda$ form factor $f_t^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-Lambda-f0A.pdf"><img src="/figures/Lambdac-to-Lambda-f0A.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to \Lambda$ form factor $f_0^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-Lambda-fperpA.pdf"><img src="/figures/Lambdac-to-Lambda-fperpA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to \Lambda$ form factor $f_\perp^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Spin-1/2 to spin-1/2: $\Lambda_c \to n$</th>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-marginals.pdf"><img src="/figures/Lambdac-to-neutron-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $\Lambda_c \to n$ (posterior <code>Lambdac-to-neutron</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-ftV.pdf"><img src="/figures/Lambdac-to-neutron-ftV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_t^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-f0V.pdf"><img src="/figures/Lambdac-to-neutron-f0V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_0^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-fperpV.pdf"><img src="/figures/Lambdac-to-neutron-fperpV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_\perp^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-ftA.pdf"><img src="/figures/Lambdac-to-neutron-ftA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_t^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-f0A.pdf"><img src="/figures/Lambdac-to-neutron-f0A.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_0^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-fperpA.pdf"><img src="/figures/Lambdac-to-neutron-fperpA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_\perp^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-f0T.pdf"><img src="/figures/Lambdac-to-neutron-f0T.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_0^T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-fperpT.pdf"><img src="/figures/Lambdac-to-neutron-fperpT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_\perp^T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-f0T5.pdf"><img src="/figures/Lambdac-to-neutron-f0T5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_0^{T5}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-neutron-fperpT5.pdf"><img src="/figures/Lambdac-to-neutron-fperpT5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to n$ form factor $f_\perp^{T5}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <th colspan=2>Spin-1/2 to spin-1/2: $\Lambda_c \to p$</th>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-marginals.pdf"><img src="/figures/Lambdac-to-proton-marginals.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Marginal posterior distributions of the SSE coefficients for $\Lambda_c \to p$ (posterior <code>Lambdac-to-proton</code>).
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-ftV.pdf"><img src="/figures/Lambdac-to-proton-ftV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_t^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-f0V.pdf"><img src="/figures/Lambdac-to-proton-f0V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_0^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-fperpV.pdf"><img src="/figures/Lambdac-to-proton-fperpV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_\perp^V$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-ftA.pdf"><img src="/figures/Lambdac-to-proton-ftA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_t^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-f0A.pdf"><img src="/figures/Lambdac-to-proton-f0A.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_0^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-fperpA.pdf"><img src="/figures/Lambdac-to-proton-fperpA.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_\perp^A$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-f0T.pdf"><img src="/figures/Lambdac-to-proton-f0T.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_0^T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-fperpT.pdf"><img src="/figures/Lambdac-to-proton-fperpT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_\perp^T$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-f0T5.pdf"><img src="/figures/Lambdac-to-proton-f0T5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_0^{T5}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
<tr>
  <td><a href="figures/Lambdac-to-proton-fperpT5.pdf"><img src="/figures/Lambdac-to-proton-fperpT5.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction of the $\Lambda_c \to p$ form factor $f_\perp^{T5}$, overlaid on the input constraints. The filled area corresponds to the 68% probability envelope.
  </td>
</tr>
</table>
