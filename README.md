# Analysis 2026-06
## Analysis as shown in Dominik Suelmann's thesis

Authors: D. Suelmann

### Contents

#### Ancillary Files

The files in this directory represent an EOS-based analysis of $\Lambda_c \to p \ell^+\ell^-$ decays
as shown in Dominik Suelmann's thesis. Included are fits of resonance parameters using LHCb data, fits to null-test measurements, predictions
for as-yet unmeasured observables and plots for visualization purposes.

 - ``analysis.yaml``: Definition and description of the analysis, including a SM posterior (``SM-fit``) for resonance parameter fits, posteriors with fixed C10 Wilson coefficients and different assumptions about strong phases (``C10-a``,``C10-b``,``C10-c``,``C10-d``,``C10-unc``, and ``C10-example``),
 posteriors with fixed C7 Wilson coefficients (``NP-fit-C7``,``NP-fit-C7p``) and posteriors for fits to the null-test AFB using current data (``NP-fit-C10-C10p-AFB``,``NP-fit-C10-C10p-AFB-fixed-phases-v1``,``NP-fit-C10-C10p-AFB-fixed-rel-phases-v1``) and for reduced statistical uncertainty (``NP-fit-C10-C10p-future-AFB``,``NP-fit-C10-C10p-future-AFB-fixed-phases-v1``,``NP-fit-C10-C10p-AFB-fixed-rel-phases-v1``).
 All are ready for use with the ``eos-analysis`` command-line tool.

 - ``data``: Posterior samples produced using EOS version 1.0.21.
   The samples are stored as ``eos.ImportanceSamples`` objects and can be loaded directly in EOS.
   The posterior-predictive samples were to large to upload here; please produce them using the
   posterior samples and the ``eos-analysis`` command-line tool.

 - ``scripts``: Scripts written in ``python`` to produce figures and tables of the analysis.

 - ``input``: Extra input files needed for some of the figures.

 - ``figures``: Figures as included in the thesis and produced using the included ``python`` scripts in ``scripts``.

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
  <td><a href="figures/corner_plot.pdf?raw=true"><img src="/figures/corner_plot.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Corner-plot of resonance parameters in $\Lambda_c\to p\ell^+\ell^-$ decays for SM fits using measurements
   by LHCb [LHCb:2024hju](https://doi.org/10.1103/PhysRevD.110.052007).
  </td>
</tr>
<tr>
  <td><a href="figures/SM_obs_binned.pdf?raw=true"><img src="/figures/SM_obs_binned.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    SM posterior predictions of the binned branching ratio $\langle \mathcal{B}\rangle$ and longitudinal polarization fraction $\langle F_L \rangle$
    in the bins used by LHCb [LHCb:2024hju](https://doi.org/10.1103/PhysRevD.110.052007). For the full-$q^2$ region, observables are shown in gray.
  </td>
</tr>
<tr>
  <td><a href="figures/dBR_dq2.pdf?raw=true"><img src="/figures/dBR_dq2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
    SM posterior predictions of the differential branching fraction using measurements by LHCb [LHCb:2024hju](https://doi.org/10.1103/PhysRevD.110.052007) (orange)
    and for strong phases other than the best-fit values (black lines).
  </td>
</tr>
<tr>
  <td><a href="figures/dBR_dq2_high_q2.pdf?raw=true"><img src="/figures/dBR_dq2_high_q2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Illustration of the interplay between resonant SM contributions, perturbative SM contributions and NP contributions in the high-$q^2$ region of
   the differential branching ratio. The resonant SM contribution (orange) is shown as posterior prediction using measurements by LHCb [LHCb:2024hju](https://doi.org/10.1103/PhysRevD.110.052007) with additional curves (black lines) for strong phases other than the best-fit values.
   The pure NP contribution (purple) is shown for $C_{10}=1$ together with form factor uncertainties calculated by EOS. The perturbative SM
   contribution (light blue) is taken from [Golz:2021imq](https://doi.org/10.1007/jhep09(2021)208).
  </td>
</tr>
<tr>
  <td><a href="figures/NP_FL_q2.pdf?raw=true"><img src="/figures/NP_FL_q2.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction for the unbinned longitudinal polarization fraction $F_L(q^2)$ in the SM (orange), for resonant SM contributions together with $C_7 = 0.15$ (purple), and for resonant SM contributions together with $C_7^\prime = 0.15$ (green). In all cases the resonance parameters of the SM contribution
   are fixed by LHCb measurements [LHCb:2024hju](https://doi.org/10.1103/PhysRevD.110.052007). Additional curves using best-fit values for the scenario with $C_7 = 0.15$, but different values for the strong phases, are shown as black lines.
  </td>
</tr>
<tr>
  <td><a href="figures/NP_FL_binned.pdf?raw=true"><img src="/figures/NP_FL_binned.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction for the binned longitudinal polarization fraction $\langle F_L \rangle$ in the SM (orange), for resonant SM contributions together with $C_7 = 0.15$ (purple), and for resonant SM contributions together with $C_7^\prime = 0.15$ (green). In all cases the resonance parameters of the SM contribution
   are fixed by LHCb measurements [LHCb:2024hju](https://doi.org/10.1103/PhysRevD.110.052007).
  </td>
</tr>
<tr>
  <td><a href="figures/thesis_AFB_general.pdf?raw=true"><img src="/figures/thesis_AFB_general.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Posterior prediction for the semi-binned null-test observable $\langle A_{\mathrm{FB}} \rangle(q^2)$ (left) and the binned null-test observable
   $\langle A_{\mathrm{FB}} \rangle$ for scenarios with $C_{10}=0.3$. In all cases the resonance parameters of the SM contribution
   are fixed by LHCb measurements [LHCb:2024hju](https://doi.org/10.1103/PhysRevD.110.052007). Curves are shown using uniform priors for the strong phases (purple)
   and using fixed strong phases (other colors).
  </td>
</tr>
<tr>
  <td><a href="figures/C10-AFB-compare.pdf?raw=true"><img src="/figures/C10-AFB-compare.png?raw=true" width="1000px" height="auto"></a></td>
  <td>
   Constraints on the NP Wilson coefficient $C_{10}$ using LHCb measurements
   of null-test observables $\langle A_{\mathrm{FB}} \rangle$ [LHCb:2025bfy](https://doi.org/10.1103/PhysRevD.111.L091102) and measurements of the branching fraction
   [LHCb:2024hju](https://doi.org/10.1103/PhysRevD.110.052007) to fix resonance parameters. Fits are performed using uniform priors for the strong phase (orange)
   and for fixed strong phases (green, blue). Additional curves (dashed) are shown assuming reduced statistical uncertainties.
  </td>
</tr>
</table>