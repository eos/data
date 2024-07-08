import eos
import numpy as np
import scipy.stats

# Load the data
labels = [
    r'SM (nominal)',
    r'CKM (nominal)',
    r'WET (nominal)',
    r'SM (scale factor)',
    r'CKM (scale factor)',
    r'WET (scale factor)'
]
ids = [
    'SM-all',
    'CKM-all',
    'WET-all',
    'SM-all-rescaled',
    'CKM-all-rescaled',
    'WET-all-rescaled'
]

nparams = [
    0,
    1,
    9,
    0,
    1,
    9
]

theory = [
    'decay-constant::D_s@FLAG:2021A',
    'decay-constant::D_s^*@MDLLSYZ:2024A',
    'decay-constant::D_s^*,T@PZ:2021A',
    'D->K::f_++f_0@ETM:2017B',
    'D->K::f_T@ETM:2018A',
    'D->K::f_++f_0@FNALMILC:2022A',
    'D->K::f_0+f_++f_T@HPQCD:2022A',
    'Lambda_c->Lambda::f_time+long+perp^V+A@M:2016A',
    'Lambda_c->Lambda::f_perp^T_f_perp^V@SCET',
    'Lambda_c->Lambda::f_long^T_f_long^V@SCET',
    'Lambda_c->Lambda::f_perp^T5_f_perp^A@SCET',
    'Lambda_c->Lambda::f_long^T5_f_long^A@SCET',
    'Lambda_c->Lambda::f_perp^T_f_perp^V@HQET',
    'Lambda_c->Lambda::f_long^T_f_long^V@HQET',
    'Lambda_c->Lambda::f_perp^T5_f_perp^A@HQET',
    'Lambda_c->Lambda::f_long^T5_f_long^A@HQET'
]

analysis_file = eos.AnalysisFile('analysis.yaml')
for id, label, nparam in zip(ids, labels, nparams):
    # Load the data
    mode    = eos.data.Mode(f'data/{id}/mode--default')
    nested  = eos.data.DynestyResults(f'data/{id}/nested')
    #samples = eos.data.ImportanceSamples(f'data/{id}/samples')

    # Compute the goodness-of-fit
    analysis = analysis_file.analysis(f'{id}')
    for p, v in zip(analysis.varied_parameters, mode.mode):
        p.set(v)
    gof = analysis.goodness_of_fit()

    exp_chi2 = 0
    exp_dof  = 0
    th_chi2  = 0
    th_dof   = 0
    for entry in gof:
        name = str(entry[0])
        if name in theory:
            th_chi2  += entry[1].chi2
            th_dof   += entry[1].dof
        else:
            exp_chi2 += entry[1].chi2
            exp_dof  += entry[1].dof

    logz  = nested.results['logz'][-1]
    dlogz = nested.results['logzerr'][-1]

    exp_dof -= nparam

    pvalue = scipy.stats.chi2(exp_dof).sf(exp_chi2)

    # Output the row
    print(fr'{label:>40} & {exp_chi2:>5.2f} & {exp_dof:>3} & {pvalue * 100:>4.1f}\% & {logz:>4.1f} \pm {dlogz:2.1f}\\')

print('')
