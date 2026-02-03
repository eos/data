# Analysis 2025-01
## A Global Determination of |Vus|

Authors: M. Kirk, D. van Dyk

### Contents

#### Ancillary Files

The files in this directory represent inputs and results of an EOS-based analysis of $s \to u \ell^- \bar{\nu}$ transitions.

 - ``analysis_FF.yaml``: Definition and description of the FF analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
 - ``analysis_FF.smk``: Snakemake file that can be used to run all steps in the ``FF`` fit model analysis.
 - ``analyse_FF.ipynb``: Jupyter notebook that calculates numerics for our FF fit model, and generates figure 2.
 - ``analysis_CKM.yaml``: Definition and description of the CKM analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
 - ``analysis_CKM.smk``: Snakemake file that can be used to run all steps in the ``CKM`` fit model analysis.
 - ``analyse_CKM.ipynb``: Jupyter notebook that calculates numerics for our CKM fit model, and generates figures 3 and 4.
 - ``analysis_BSM.yaml``: Definition and description of the BSM analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
 - ``analysis_BSM.smk``: Snakemake file that can be used to run all steps in the ``BSM`` fit model analysis.
 - ``analyse_BSM.ipynb``: Jupyter notebook that calculates numerics for our BSM fit model.
 - The posteriors ``FF_2_2_4_4``, ``CKM_2_2_4_4``, ``BSM_2_2_4_4`` provide the nominal results of the analysis.
 - The posteriors ``FF_2_2_3_3``, ``FF_3_2_4_4``, ``FF_3_2_5_5``; ``CKM_2_2_3_3``, ``CKM_3_2_4_4``, ``CKM_3_2_5_5``; ``BSM_2_2_3_3``, ``BSM_3_2_4_4``, ``BSM_3_2_5_5`` provide supplementary results to determine our model choice uncertainty.
 - The various prediction sets were used to produce figures 2, 3, and 4, along with the numerical results in eqs. V.1, V.3, V.7, V.9, V.10, V.11, and V.13.

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.19
   The samples are stored as ``eos.ImportanceSamples`` and ``eos.Predictions`` objects and can be loaded directly in EOS.

 - ``figures``: Figures produced in the course of the analysis. Both PDF and PNG formats are available.

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
  <td><a href="figures/tau-differential-data.pdf?raw=true"><img src="/figures/tau-differential-data.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Normalised differential tau decay data from <a href="https://doi.org/10.1016/j.physletb.2007.08.045">Belle:2007goc</a>, along with the posterior prediction and 68% probability envelope of our nominal model fit.
  </td>
</tr>
<tr>
  <td><a href="figures/ckm-comparison.pdf?raw=true"><img src="/figures/ckm-comparison.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Our result for $|V{us}|$ shown as the shaded vertical band, in comparison to results in the literature.
    We show four independent results obtained from inclusive $\tau$ decays, corresponding to results from Refs. <a href="https://doi.org/10.1088/1126-6708/2003/01/060">Gamiz:2002nu</a>,<a href="https://doi.org/10.1103/PhysRevLett.94.011803">Gamiz:2004ar</a> (top-most data point), Refs. <a href="https://doi.org/10.48550/arXiv.1510.06954">Maltman:2015xwa</a>, <a href="https://doi.org/10.21468/SciPostPhysProc.1.006">Maltman:2019xeh</a> (second from top), Refs. <a href="https://doi.org/10.1103/PhysRevLett.121.202003">RBC:2018uyk</a>, <a href="https://doi.org/10.21468/SciPostPhysProc.1.006">Maltman:2019xeh</a> (second from bottom), and Ref. <a href="https://doi.org/10.1103/PhysRevLett.132.261901">ExtendedTwistedMass:2024myu</a> (bottom).
    We refer the interested reader to discussions in the <a href="https://hflav-eos.web.cern.ch/hflav-eos/tau/end-2023/vus.html">HFLAV report</a> for details of the differences between these determinations.
    The $K_{\ell 3}$, hyperon, and $\beta$ decay + unitarity results are taken from the <a href="https://pdg.lbl.gov/2025/reviews/rpp2024-rev-vud-vus.pdf">Particle Data Group</a>, while the global CKM fit is obtained by the <a href="http://ckmfitter.in2p3.fr/www/results/plots_summer23/num/ckmEval_results_summer23.html">CKMfitter collaboration</a>.
  </td>
</tr>
<tr>
  <td><a href="figures/Vus-correlations.pdf?raw=true"><img src="/figures/Vus-correlations.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Joint distribution of $|V_{us}|$, $f_{K^-}$, and $f_+(0)$ in our CKM fit model, along with a comparison to the $f_+(0)$ posterior in our FF fit model and the FLAG 2024 average.
  </td>
</tr>
</table>
