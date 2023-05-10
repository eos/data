# Analysis 2023-02
## Dispersive analysis of $b\to s\ell^+\ell^-$ form factors

Authors: N. Gubernari, M. Reboud, D. van Dyk, J. Virto

### Contents

#### Ancillary Files

The files in this directory represent input and approximations to the results of an analysis of exclusive $b\to s\ell^+\ell^-$ form factors.

  - ``BToK_FF.yaml``: Definition and description of the analysis of $\bar{B}\to \bar{K}$ form factors, for use with the `eos-analysis` command-line tool.
    - The posteriors labelled ``Update``, ``Update2``, ``Update4`` provide access to the dispersively-bounded analyses. ``Update`` represents the nominal posterior with truncation order $N=3$, while the other posteriors features truncation orders $N=2$ and $N=4$, respectively.
    - The posterior labelled ``BSZ`` provides access to the BSZ-style analyses of the same data as ``Update`` without dispersive bounds.
  - ``BToKstar_FF.yaml``: Definition and description of the analysis of $\bar{B}\to \bar{K}^*$ form factors, for use with the `eos-analysis` command-line tool. The content mirrors that of ``BtoK_FF.yaml``
  - ``BsToPhi_FF.yaml``: Definition and description of the analysis of $\bar{B}_s\to \phi$ form factors, for use with the `eos-analysis` command-line tool. The content mirrors that of ``BtoK_FF.yaml``
  - `GRvDV-parameters-N2.yaml`: EOS constraint file containing the multivariate Gaussian approximation to the posterior PDF for the parameters in the dispersively-bounded parameterization introduced in the paper.
  - `BSZ-parameters-N2.yaml`: EOS constraint file containing the multivariate Gaussian approximation to the posterior PDF for the parameters in the parameterization of [Bharucha, Straub, Zwicky 2015](https://doi.org/10.1007/JHEP08(2016)098).

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
  <td><a href="figures/BToK_fp.pdf?raw=true"><img src="/figures/BToK_fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the representative form factor $f_+^{B\to K}(q^2)$, rescaled by the pole term $P(q^2) = 1 - q^2 / M_{B_s^*}^2$ to improve legibility.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_A1.pdf?raw=true"><img src="/figures/BToKstar_A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the representative form factor $A_1^{B\to K^*}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_A1.pdf?raw=true"><img src="/figures/BsToPhi_A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the representative form factor $A_1^{B_s\to \phi}(q^2)$.
  </td>
</tr>  
<tr>
  <td><a href="figures/saturations.pdf?raw=true"><img src="/figures/saturations.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Saturations of the dispersive bounds due to one- and two-particle contributions.
   The lines represent Gaussian-smoothed distributions of the saturations in our samples that we combined following the method described in the paper.
   The shaded area comprise the 68% probability interval for each scenario.
   The distributions are scaled with arbitrary factors for readability.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/BToK_f0.pdf?raw=true"><img src="/figures/BToK_f0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $f_0^{B\to K}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToK_fT.pdf?raw=true"><img src="/figures/BToK_fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $f_T^{B\to K}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_V.pdf?raw=true"><img src="/figures/BToKstar_V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $V^{B\to K^*}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_A0.pdf?raw=true"><img src="/figures/BToKstar_A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $A_0^{B\to K^*}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_A1.pdf?raw=true"><img src="/figures/BToKstar_A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $A_1^{B\to K^*}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_T1.pdf?raw=true"><img src="/figures/BToKstar_T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $T_1^{B\to K^*}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_T2.pdf?raw=true"><img src="/figures/BToKstar_T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $T_2^{B\to K^*}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_T23.pdf?raw=true"><img src="/figures/BToKstar_T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $T_{23}^{B\to K^*}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_V.pdf?raw=true"><img src="/figures/BsToPhi_V.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $V^{B_s\to \phi}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_A0.pdf?raw=true"><img src="/figures/BsToPhi_A0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $A_0^{B_s\to \phi}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_A1.pdf?raw=true"><img src="/figures/BsToPhi_A1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $A_1^{B_s\to \phi}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_T1.pdf?raw=true"><img src="/figures/BsToPhi_T1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $T_1^{B_s\to \phi}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_T2.pdf?raw=true"><img src="/figures/BsToPhi_T2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $T_2^{B_s\to \phi}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_T23.pdf?raw=true"><img src="/figures/BsToPhi_T23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $T_{23}^{B_s\to \phi}(q^2)$.
  </td>
</tr>
<tr>
  <td><a href="figures/BToK_Nfp.pdf?raw=true"><img src="/figures/BToK_Nfp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BToK_Nf0.pdf?raw=true"><img src="/figures/BToK_Nf0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BToK_NfT.pdf?raw=true"><img src="/figures/BToK_NfT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_NV.pdf?raw=true"><img src="/figures/BToKstar_NV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_NA0.pdf?raw=true"><img src="/figures/BToKstar_NA0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_NA1.pdf?raw=true"><img src="/figures/BToKstar_NA1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_NT1.pdf?raw=true"><img src="/figures/BToKstar_NT1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_NT2.pdf?raw=true"><img src="/figures/BToKstar_NT2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BToKstar_NT23.pdf?raw=true"><img src="/figures/BToKstar_NT23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>

<tr>
  <td><a href="figures/BsToPhi_NV.pdf?raw=true"><img src="/figures/BsToPhi_NV.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_NA0.pdf?raw=true"><img src="/figures/BsToPhi_NA0.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_NA1.pdf?raw=true"><img src="/figures/BsToPhi_NA1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_NT1.pdf?raw=true"><img src="/figures/BsToPhi_NT1.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_NT2.pdf?raw=true"><img src="/figures/BsToPhi_NT2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToPhi_NT23.pdf?raw=true"><img src="/figures/BsToPhi_NT23.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of the different parametrizations discussed in the analysis.
   The theory inputs are fitted with a BSZ parameterization and with an improved BGL-like parametrization using N = {2, 3, 4}.
   The inputs and the curves are normalized to the best-fit curve obtained with N = 3.
  </td>
</tr>
</table>

### How to reproduce the posterior samples

The posterior samples within our various fits can be obtained in the command line.
The process requires an up-to-date version of EOS (>= v1.0.7) and involves the command
```
eos-analysis sample-nested -f ANALYSISFILE -b DATADIR POSTERIOR
```
where:
  - `ANALYSISFILE` is the path to one of the analysis file, i.e. `BToK_FF.yaml`, `BToKstar_FF.yaml`, `BsTophi_FF.yaml`;
  - `DATADIR` is the path to a directory where the samples will be stored;
  - `POSTERIOR` is the name of a posterior for which samples shall be produced (e.g. `Update2`).
    
The full list of valid values for `POSTERIOR` is displayed by running `eos-analysis list-posteriors -f ANALYSISFILE`.

The posterior samples will be stored in the directory `DATADIR/POSTERIOR/samples`.

**Note**: The sampling process is very memory intensive and can easily consume up to 30GiB of RAM!

### How to predict observables

Once the posterior samples have been produced, posterior-predictive samples of (pseudo)observables can be produced in the command line.
The process requires an up-to-date version of EOS (>= v1.0.7) and involves the command
```
eos-analysis predict-observables -f ANALYSISFILE -b DATADIR POSTERIOR PREDICTION
```
where:
  - `ANALYSISFILE` is the path to one of the analysis file, i.e. `BToK_FF.yaml`, `BToKstar_FF.yaml`, `BsTophi_FF.yaml`;
  - `DATADIR` is the path to a directory where the samples will be stored;
  - `POSTERIOR` is the name of a posterior for which samples shall be produced (e.g. `Update2`);
  - `PREDICTION` is the name of a set of predictions for (pseudo)observables (e.g. `saturations`).

The full list of valid values for `PREDICTION` is displayed by running `eos-analysis list-predictions -f ANALYSISFILE`.

The posterior-predictive samples will be stored in the directory `DATADIR/POSTERIOR/pred-PREDICTION`.
