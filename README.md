# Analysis-2023-03
## New determination of $|V_{ub}/V_{cb}|$ from $B_s^0\to \lbrace K^-, D_s^- \rbrace \mu^+\nu$

Authors: C. Bolognani, D. van Dyk, K.K. Vos

### Contents

#### Ancillary Files

The files in this directory represent input and results of

  - a LCSR analysis for the full set of $\bar{B}_s \rightarrow K$ form factors;
  - a joint analysis of the available LCSR and LQCD form factor determinations;
  - and a determination of $|V_{ub}/V_{cb}|$ from LHCb data.

These files are:
  - ``lcsr-bs-to-k.yaml``: Definition and description of the analysis of $\bar{B}_s\to K$ form factors using LCSR, for use with the `eos-analysis` command-line tool.
    - The posteriors labelled ``lcsr`` & ``lcsr-const`` provide access to the two analyses with different models for the duality threshold parameters.
  - ``ff-bs-to-k.yaml``: Definition and description of the analysis of the available $\bar{B}_s\to K$ form factor results in the full $q^2$ range, for use with the `eos-analysis` command-line tool. All posteriors use a unitarity-bounded parametrisation.
    - The posteriors labelled ``ff-lcsr``, ``ff-lqcd``, and ``ff-lcsr-lqcd`` correspond to the different sets of constraints utilised in the analysis.
  - `VubVcb-bs-to-k-ds-l-nu.yaml`: Definition and description of the analysis extracting $|V_{ub}/V_{cb}|$ from an LHCb measurement of $B_s^0\to \lbrace K^-, D_s^- \rbrace \mu^+\nu$ decays.
    - The posteriors ``bs-k-ds-lnu-lcsr``, ``bs-k-ds-lnu-lqcd``, and ``bs-k-ds-lnu-lcsr-lqcd`` mirror those defined in ``ff-bs-to-k.yaml``.
  - ``BvDV_BsK_LCSR_form_factors.yaml``: EOS constraint file containing the multivariate Gaussian fit to the LCSR results for the form factors.

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
  <td><a href="figures/threshold-fp.pdf?raw=true"><img src="/figures/threshold-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between a $q^2$-dependent and a $q^2$-independent model for the duality threshold in the $f_+^{B_s \to K}$ determination.
  </td>
</tr>
<tr>
  <td><a href="figures/threshold-fz.pdf?raw=true"><img src="/figures/threshold-fz.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between a $q^2$-dependent and a $q^2$-independent model for the duality threshold in the $f_0^{B_s \to K}$ determination.
  </td>
</tr>
<tr>
  <td><a href="figures/threshold-fT.pdf?raw=true"><img src="/figures/threshold-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between a $q^2$-dependent and a $q^2$-independent model for the duality threshold in the $f_T^{B_s \to K}$ determination.
  </td>
</tr>
<tr>
  <td><a href="figures/saturation-fp.pdf?raw=true"><img src="/figures/saturation-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Saturation of the unitarity bound related to the $f_+^{B_s \to K}$ form factor for the posterior LCSR+LQCD.
  </td>
</tr>
<tr>
  <td><a href="figures/saturation-fz.pdf?raw=true"><img src="/figures/saturation-fz.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Saturation of the unitarity bound related to the $f_0^{B_s \to K}$ form factor for the posterior LCSR+LQCD.
  </td>
</tr>
<tr>
  <td><a href="figures/saturation-fT.pdf?raw=true"><img src="/figures/saturation-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Saturation of the unitarity bound related to the $f_T^{B_s \to K}$ form factor for the posterior LCSR+LQCD.
  </td>
</tr>
<tr>
  <td><a href="figures/result-fp.pdf?raw=true"><img src="/figures/result-fp.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the representative form factor $f_+^{B_s\to K}(q^2)$, rescaled by the pole term $P(q^2) = 1 - q^2 / M_{B_u^*}^2$ to improve legibility. Only the results for the posterior LCSR+LQCD are shown.
  </td>
</tr>
<tr>
  <td><a href="figures/result-fz.pdf?raw=true"><img src="/figures/result-fz.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the representative form factor $f_0^{B_s\to K}(q^2)$. Only the results for the posterior LCSR+LQCD are shown.
  </td>
</tr>
<tr>
  <td><a href="figures/result-fT.pdf?raw=true"><img src="/figures/result-fT.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the representative form factor $f_T^{B_s\to K}(q^2)$, rescaled by the pole term $P(q^2) = 1 - q^2 / M_{B_u^*}^2$ to improve legibility. Only the results for the posterior LCSR+LQCD are shown.
  </td>
</tr>
<tr>
  <td><a href="figures/compare_ff_q20.pdf?raw=true"><img src="/figures/compare_ff_q20.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison plot of our results for $f_+^{B_s \to K}(q^2=0)$ and $f_T^{B_s \to K}(q^2=0)$ with the available results in the literature.
  </td>
</tr>
<tr>
  <td><a href="figures/dGammadq2_fits.pdf?raw=true"><img src="/figures/dGammadq2_fits.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between the differential decay rate of $B_s^0\to K^- \mu^+\nu$ in units of $|V_{ub}|^2$, for the different $\bar{B}\to K$ form factor analyses studied in the analysis. The form factors are predicted from the posteriors LCSR, LQCD, and LCSR+LQCD.
  </td>
</tr>  
<tr>
  <td><a href="figures/dGammadq2_bsm.pdf?raw=true"><img src="/figures/dGammadq2_bsm.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Comparison between the differential decay rate of $B_s^0\to K^- \mu^+\nu$, normalised by $V_{ub}=1$, in the SM and taking into account possible BSM physics. The form factors are determined from the LCSR+LQCD posterior and the BSM parameter space is taken from <a href="https://doi.org/10.5281/zenodo.8027015">EOS-DATA-2023-01v2</a>.
  </td>
</tr>  
  <th colspan=2>Supplementary Material</th>
</tr>
<tr>
  <td><a href="figures/result-fp-compare_fits.pdf?raw=true"><img src="/figures/result-fp-compare_fits.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $f_+^{B_s\to K}(q^2)$, rescaled by the pole term $P(q^2) = 1 - q^2 / M_{B_u^*}^2$ to improve legibility. Predictions obtained from all three posteriors are shown.
  </td>
</tr>
<tr>
  <td><a href="figures/result-fz-compare_fits.pdf?raw=true"><img src="/figures/result-fz-compare_fits.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the representative form factor $f_0^{B_s\to K}(q^2)$. Predictions obtained from all three posteriors are shown.
  </td>
</tr>
<tr>
  <td><a href="figures/result-fT-compare_fits.pdf?raw=true"><img src="/figures/result-fT-compare_fits.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the representative form factor $f_T^{B_s\to K}(q^2)$, rescaled by the pole term $P(q^2) = 1 - q^2 / M_{B_u^*}^2$ to improve legibility. Predictions obtained from all three posteriors are shown.
  </td>
</tr>
<tr>
  <td><a href="figures/result-fp-compare_lqcd.pdf?raw=true"><img src="/figures/result-fp-compare_lqcd.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $f_+^{B_s\to K}(q^2)$, rescaled by the pole term $P(q^2) = 1 - q^2 / M_{B_u^*}^2$ to improve legibility. Predictions obtained from all three posteriors are shown. Unutilised LQCD constraints are overlayed with the results.
  </td>
</tr>
<tr>
  <td><a href="figures/result-fz-compare_lqcd.pdf?raw=true"><img src="/figures/result-fz-compare_lqcd.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Overview plot for the form factor $f_0^{B_s\to K}(q^2)$. Predictions obtained from all three posteriors are shown. Unutilised LQCD constraints are overlayed with the results.
  </td>
</tr>
</table>

### How to reproduce the posterior samples

The posterior samples within our various fits can be obtained in the command line.
The process requires an up-to-date version of EOS (>= v1.0.9) and involves the command
```
eos-analysis sample-nested -f ANALYSISFILE -b DATADIR POSTERIOR
```
where:
  - `ANALYSISFILE` is the path to one of the analysis file, i.e. `lcsr-bs-to-k.yaml`, `ff-bs-to-k.yaml`, `VubVcb-bs-to-k-ds-l-nu.yaml`;
  - `DATADIR` is the path to a directory where the samples will be stored;
  - `POSTERIOR` is the name of a posterior for which samples shall be produced.
    
The full list of valid values for `POSTERIOR` is displayed by running `eos-analysis list-posteriors -f ANALYSISFILE`.

The posterior samples will be stored in the directory `DATADIR/POSTERIOR/samples`.

### How to predict observables

Once the posterior samples have been produced, posterior-predictive samples of (pseudo)observables can be produced in the command line.
The process requires an up-to-date version of EOS (>= v1.0.9) and involves the command
```
eos-analysis predict-observables -f ANALYSISFILE -b DATADIR POSTERIOR PREDICTION
```
where:
  - `ANALYSISFILE` is the path to one of the analysis files, i.e. `lcsr-bs-to-k.yaml`, `ff-bs-to-k.yaml`, `VubVcb-bs-to-k-ds-l-nu.yaml`;
  - `DATADIR` is the path to a directory where the samples will be stored;
  - `POSTERIOR` is the name of a posterior for which samples shall be produced;
  - `PREDICTION` is the name of a set of predictions for (pseudo)observables.

The full list of valid values for `PREDICTION` is displayed by running `eos-analysis list-predictions -f ANALYSISFILE`.

The posterior-predictive samples will be stored in the directory `DATADIR/POSTERIOR/pred-PREDICTION`.
