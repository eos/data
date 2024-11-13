import eos

# Load the data
labels = [
    r'SM'
]
ids = [
    'SM'
]

nparams = [
    0
]

theory = [
    'B_(s)->D_(s)^(*)::FormFactors[f_0(Mpi2),f_0(MK2),A_0(Mpi2),A_0(MK2)]@BGJvD:2019A'
]

analysis_file = eos.AnalysisFile('analysis.yaml')
for id, label, nparam in zip(ids, labels, nparams):
    # Load the data
    mode    = eos.data.Mode(f'data/{id}/mode-default')
    # Open the logz file and read it as a dictionary
    with open(f'data/{id}/logz.txt', 'r') as file:
        logz_dict = {}
        for line in file:
            key, value = line.strip().split(': ', 1)
            logz_dict[key] = value

    # Compute the goodness-of-fit for mode A
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
            th_chi2 += entry[1].chi2
            th_dof  += entry[1].dof
        else:
            exp_chi2 += entry[1].chi2
            exp_dof  += entry[1].dof

    logz  = float(logz_dict['logz'])
    dlogz = float(logz_dict['logzerr'])

    # Output the row
    print(fr'{label:>40} & {exp_chi2:>5.2f} & {logz:>4.2f} \pm {dlogz:2.2f}\\')

print('')