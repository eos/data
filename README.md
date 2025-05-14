# Analysis 2023-09
## Challenging $\overline{B}\_{(s)}\to D\_{(s)}^{(\ast)}$ Form Factors with the Heavy Quark Expansion

Authors: M. Bordone, N. Gubernari, M. Jung, D. van Dyk

### Contents

#### Ancillary Files

The files in this directory represent inputs and approximations to the results of an EOS-based analysis
of  $\overline{B}\_{(s)}\to D\_{(s)}^{(\ast)}$ form factors

 - ``analysis.yaml``: Definition and description of the entire analysis for use with an interactive Jupyter notebook and/or the ``eos-analysis`` command-line tool.
   - The posterior ``HQE321red-q-LQCD+UB+SU3`` provides the nominal results of the analysis.
   - The posteriors ``HQE210red-q-LQCD+UB``, ``HQE210red-q-LQCD+UB+SU3``, ``HQE321red-q-LQCD+UB``, and ``HQE321-q-LQCD+UB+SR`` provide supplementary results.
   - The various prediction sets were used to produce the figures listed below.

 - ``data``: Posterior samples and posterior-predictive samples produced in the course of the analysis, using EOS version 1.0.14.
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
  <td><a href="figures/saturations.pdf?raw=true"><img src="/figures/saturations.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Individual plots of the saturation of the unitarity bounds for each $\bar{c}b$ current.
    The two plots on the right show the saturation of the tensor currents for the first time.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A1-combined.pdf?raw=true"><img src="/figures/BToDstar-A1-combined.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Plot of the $\overline{B}\to D^*$ form factor $A_1$ as function of $q^2$.
    Solid curves correspond to the median values and shaded regions correspond to the central $68\%$ credible interval.
    The nominal results of our previous work involving sum-rule results are shown in green.
    Our nominal results of this work in the $3/2/1^∗$ model with $\text{SU(3)}_F$ symmetry are shown in blue.
    Auxiliary result of this work in the $3/2/1$ model are shown in orange.
  </td>
</tr>
<tr>
  <td><a href="figures/R0-ratio.pdf?raw=true"><img src="/figures/R0-ratio.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Plot of the $\overline{B}\to D^*$ form factor ratio $R_0$ as function of $q^2$.
    Solid curves correspond to the median values and shaded regions correspond to the central $68\%$ credible interval.
    The nominal results of our previous work involving sum-rule results are shown in green.
    Our nominal results of this work in the $3/2/1^∗$ model with $\text{SU(3)}_F$ symmetry are shown in blue.
    Auxiliary result of this work in the $3/2/1$ model are shown in orange.
  </td>
</tr>
<tr>
  <td><a href="figures/R1-ratio.pdf?raw=true"><img src="/figures/R1-ratio.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Plot of the $\overline{B}\to D^*$ form factor ratio $R_1$ as function of $q^2$.
    Solid curves correspond to the median values and shaded regions correspond to the central $68\%$ credible interval.
    The nominal results of our previous work involving sum-rule results are shown in green.
    Our nominal results of this work in the $3/2/1^∗$ model with $\text{SU(3)}_F$ symmetry are shown in blue.
    Auxiliary result of this work in the $3/2/1$ model are shown in orange.
  </td>
</tr>
<tr>
  <td><a href="figures/R2-ratio.pdf?raw=true"><img src="/figures/R2-ratio.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Plot of the $\overline{B}\to D^*$ form factor ratio $R_2$ as function of $q^2$.
    Solid curves correspond to the median values and shaded regions correspond to the central $68\%$ credible interval.
    The nominal results of our previous work involving sum-rule results are shown in green.
    Our nominal results of this work in the $3/2/1^∗$ model with $\text{SU(3)}_F$ symmetry are shown in blue.
    Auxiliary result of this work in the $3/2/1$ model are shown in orange.
  </td>
</tr>
<tr>
  <td><a href="figures/S6s.pdf?raw=true"><img src="/figures/S6s.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    Plot of the angular observable S6s for $\overline{B}\to D^{\ast}\mu^-\bar\nu$ decays in bins of $q^2$.
  </td>
</tr>
<tr>
  <th colspan=2>Supplementary Material</th>
</tr>
<!-- f_+ -->
<tr>
  <th colspan=2>$\overline{B}\to D$ form factor $f_+$</th>
</tr>
<tr>
  <td><a href="figures/BToD-f+-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToD-f+-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_+$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-f+-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToD-f+-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_+$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-f+-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToD-f+-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_+$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-f+-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToD-f+-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_+$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-f+-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToD-f+-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_+$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- f_0 -->
<tr>
  <th colspan=2>$\overline{B}\to D$ form factor $f_0$</th>
</tr>
<tr>
  <td><a href="figures/BToD-f0-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToD-f0-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_0$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-f0-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToD-f0-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_0$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-f0-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToD-f0-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_0$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-f0-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToD-f0-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_0$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-f0-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToD-f0-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_0$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- f_T -->
<tr>
  <th colspan=2>$\overline{B}\to D$ form factor $f_T$</th>
</tr>
<tr>
  <td><a href="figures/BToD-fT-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToD-fT-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_T$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-fT-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToD-fT-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_T$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-fT-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToD-fT-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_T$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-fT-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToD-fT-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_T$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToD-fT-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToD-fT-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_T$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- V -->
<tr>
  <th colspan=2>$\overline{B}\to D^*$ form factor $V$</th>
</tr>
<tr>
  <td><a href="figures/BToDstar-V-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-V-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $V$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-V-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-V-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $V$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-V-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-V-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $V$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-V-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-V-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $V$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-V-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToDstar-V-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $V$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- A0 -->
<tr>
  <th colspan=2>$\overline{B}\to D^*$ form factor $A_0$</th>
</tr>
<tr>
  <td><a href="figures/BToDstar-A0-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-A0-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_0$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A0-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-A0-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_0$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A0-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-A0-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_0$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A0-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-A0-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_0$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A0-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToDstar-A0-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_0$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- A1 -->
<tr>
  <th colspan=2>$\overline{B}\to D^*$ form factor $A_1$</th>
</tr>
<tr>
  <td><a href="figures/BToDstar-A1-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-A1-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_1$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A1-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-A1-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_1$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A1-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-A1-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_1$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A1-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-A1-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_1$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A1-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToDstar-A1-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_1$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- A12 -->
<tr>
  <th colspan=2>$\overline{B}\to D^*$ form factor $A_{12}$</th>
</tr>
<tr>
  <td><a href="figures/BToDstar-A12-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-A12-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_{12}$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A12-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-A12-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_{12}$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A12-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-A12-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_{12}$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A12-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-A12-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_{12}$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-A12-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToDstar-A12-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_{12}$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- T1 -->
<tr>
  <th colspan=2>$\overline{B}\to D^*$ form factor $T_1$</th>
</tr>
<tr>
  <td><a href="figures/BToDstar-T1-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-T1-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_1$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T1-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-T1-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_1$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T1-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-T1-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_1$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T1-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-T1-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_1$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T1-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToDstar-T1-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_1$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- T2 -->
<tr>
  <th colspan=2>$\overline{B}\to D^*$ form factor $T_2$</th>
</tr>
<tr>
  <td><a href="figures/BToDstar-T2-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-T2-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_2$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T2-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-T2-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_2$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T2-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-T2-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_2$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T2-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-T2-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_1$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T2-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToDstar-T2-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_2$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- T23 -->
<tr>
  <th colspan=2>$\overline{B}\to D^*$ form factor $T_{23}$</th>
</tr>
<tr>
  <td><a href="figures/BToDstar-T23-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-T23-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_{23}$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T23-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-T23-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_{23}$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T23-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BToDstar-T23-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_{23}$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T23-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BToDstar-T23-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_{23}$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BToDstar-T23-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BToDstar-T23-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $T_{23}$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s -> D_s f_+ -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s$ form factor $f_+$</th>
</tr>
<tr>
  <td><a href="figures/BsToDs-f+-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDs-f+-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_+$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-f+-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDs-f+-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_+$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-f+-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDs-f+-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D$ form factor $f_+$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-f+-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDs-f+-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_+$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-f+-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDs-f+-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_+$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s -> D_s f_0 -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s$ form factor $f_0$</th>
</tr>
<tr>
  <td><a href="figures/BsToDs-f0-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDs-f0-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_0$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-f0-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDs-f0-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_0$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-f0-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDs-f0-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_0$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-f0-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDs-f0-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_0$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-f0-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDs-f0-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_0$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s->D_s f_T -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s$ form factor $f_T$</th>
</tr>
<tr>
  <td><a href="figures/BsToDs-fT-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDs-fT-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_T$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-fT-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDs-fT-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_T$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-fT-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDs-fT-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_T$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-fT-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDs-fT-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_T$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDs-fT-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDs-fT-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s$ form factor $f_T$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s->D_s^* V -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s^*$ form factor $V$</th>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-V-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-V-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $V$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-V-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-V-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $V$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-V-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-V-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $V$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-V-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-V-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $V$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDstar-V-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDsstar-V-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $V$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s->D_s^* A0 -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s^*$ form factor $A_0$</th>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A0-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-A0-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_0$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A0-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-A0-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_0$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A0-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-A0-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_0$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A0-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-A0-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_0$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A0-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDsstar-A0-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_0$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s->D_s^* A1 -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s^*$ form factor $A_1$</th>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A1-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-A1-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_1$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A1-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-A1-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}\to D^*$ form factor $A_1$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A1-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-A1-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_1$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A1-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-A1-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_1$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A1-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDsstar-A1-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_1$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s->D_s^* A12 -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s^*$ form factor $A_{12}$</th>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A12-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-A12-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_{12}$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A12-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-A12-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_{12}$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A12-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-A12-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_{12}$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A12-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-A12-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_{12}$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-A12-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDsstar-A12-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $A_{12}$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s->D_s^* T1 -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s^*$ form factor $T_1$</th>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T1-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-T1-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_1$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T1-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-T1-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_1$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T1-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-T1-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_1$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T1-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-T1-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_1$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T1-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDsstar-T1-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_1$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s->D_s^* T2 -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s^*$ form factor $T_2$</th>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T2-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-T2-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_2$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T2-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-T2-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_2$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T2-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-T2-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_2$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T2-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-T2-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_1$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T2-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDsstar-T2-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_2$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
<!-- B_s->D_s^* T23 -->
<tr>
  <th colspan=2>$\overline{B}_s\to D_s^*$ form factor $T_{23}$</th>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T23-HQE210red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-T23-HQE210red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_{23}$ as function of $q^2$ in the $2/1/0^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T23-HQE210red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-T23-HQE210red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_{23}$ as function of $q^2$ in the $2/1/0^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T23-HQE321red-q-LQCD+UB.pdf?raw=true"><img src="/figures/BsToDsstar-T23-HQE321red-q-LQCD+UB.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_{23}$ as function of $q^2$ in the $3/2/1^*$ model fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T23-HQE321red-q-LQCD+UB+SU3.pdf?raw=true"><img src="/figures/BsToDsstar-T23-HQE321red-q-LQCD+UB+SU3.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_{23}$ as function of $q^2$ in the $3/2/1^*$ model w/ SU(3) flavour symmetry fitted to the <code>LQCD</code> likelihood.
  </td>
</tr>
<tr>
  <td><a href="figures/BsToDsstar-T23-HQE321-q-LQCD+UB+SR.pdf?raw=true"><img src="/figures/BsToDsstar-T23-HQE321-q-LQCD+UB+SR.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Plot of the $\overline{B}_s\to D_s^*$ form factor $T_{23}$ as function of $q^2$ in the $3/2/1$ model fitted to the combined <code>LQCD</code> and <code>QCDSR</code> likelihood.
  </td>
</tr>
</table>
