import eos
import numpy as np

# Load the data
labels = [
    r'WET-1',
    r'WET-2',
    r'WET-3',
    r'WET-4',
]
ids = [
    'WET-1',
    'WET-2',
    'WET-3',
    'WET-4'
]

nparams = [
    4,
    6,
    4,
    6
]


theory = [
    'B_(s)->D_(s)^(*)::FormFactors[f_0(Mpi2),f_0(MK2),A_0(Mpi2),A_0(MK2)]@BGJvD:2019A'
]

# create masks
analysis_file = eos.AnalysisFile('analysis.yaml')
samples_dict = {}
for id, label, nparam in zip(ids, labels, nparams):
    samples_dict[f'samples_{label}'] = np.load(f'data/{id}/samples/samples.npy')[:,:nparam]

wc1WET1   = samples_dict["samples_WET-1"][:,0]
wc2WET1   = samples_dict["samples_WET-1"][:,1]
wc5WET2   = samples_dict["samples_WET-2"][:,0]
wc6WET2   = samples_dict["samples_WET-2"][:,1]
wc1pWET3  = samples_dict["samples_WET-3"][:,0]
wc2pWET3  = samples_dict["samples_WET-3"][:,1]
wc5pWET4  = samples_dict["samples_WET-4"][:,0]
wc6pWET4  = samples_dict["samples_WET-4"][:,1]
wc8pWET4  = samples_dict["samples_WET-4"][:,3]
wc10pWET4 = samples_dict["samples_WET-4"][:,5]

mask_array = [
        [
            (((wc1WET1 > -1.6 - 1.17 * wc2WET1) & (wc1WET1 < - 1.17 * wc2WET1)) | ((wc1WET1 < 1.6 - 1.17 * wc2WET1) & (wc1WET1 > - 1.17 * wc2WET1))),
            ((wc1WET1 < -1.6 - 1.17 * wc2WET1) | (wc1WET1 > 1.6 - 1.17 * wc2WET1))
        ],
        [
            ((wc5WET2 < 2.25 - 0.81 * wc6WET2) & (wc5WET2 > -2.25 - 0.81 * wc6WET2)),
            (wc5WET2 > 2.25 - 0.81 * wc6WET2)
        ],
        [
            wc1pWET3 < 1.15 - 1.17 * wc2pWET3,
            ((wc1pWET3 > 1.15 - 1.17 * wc2pWET3) & (wc1pWET3 < 2.45 - 1.17 * wc2pWET3))
        ],
        [
            wc5pWET4 > -3.25 - 0.75 * wc6pWET4,
            ((wc5pWET4 < -3.25 - 0.75 * wc6pWET4) & (wc8pWET4 > 0.35 + 11.25 * wc10pWET4))
        ]
]

masks = {
    "WET-1": mask_array[0],
    "WET-2": mask_array[1],
    "WET-3": mask_array[2],
    "WET-4": mask_array[3]
}

for id, label, nparam in zip(ids, labels, nparams):
    # Load the data
    mode_A  = eos.data.Mode(f'data/{id}/mode-A')
    mode_B  = eos.data.Mode(f'data/{id}/mode-B')
    samples = eos.data.ImportanceSamples(f'data/{id}/samples')
    weights = np.load(f'data/{id}/samples/weights.npy')
    # Open the logz file and read it as a dictionary
    with open(f'data/{id}/logz.txt', 'r') as file:
        logz_dict = {}
        for line in file:
            key, value = line.strip().split(': ', 1) 
            logz_dict[key] = value


    # Compute the goodness-of-fit for mode A and B
    analysis = analysis_file.analysis(f'{id}')
    for p, v in zip(analysis.varied_parameters, mode_A.mode):
        p.set(v)
    gof_A = analysis.goodness_of_fit()

    for p, v in zip(analysis.varied_parameters, mode_B.mode):
        p.set(v)
    gof_B = analysis.goodness_of_fit()

    exp_chi2_A = 0
    exp_chi2_B = 0
    exp_dof    = 0
    th_chi2_A  = 0
    th_chi2_B  = 0
    th_dof     = 0
    for entry in gof_A:
        name = str(entry[0])
        if name in theory:
            th_chi2_A += entry[1].chi2
            th_dof    += entry[1].dof
        else:
            exp_chi2_A += entry[1].chi2
            exp_dof    += entry[1].dof

    for entry in gof_B:
        name = str(entry[0])
        if name in theory:
            th_chi2_B += entry[1].chi2
        else:
            exp_chi2_B += entry[1].chi2

    logz_tot  = float(logz_dict['logz'])
    dlogz     = float(logz_dict['logzerr'])
    
    mask_A = masks[f'{label}'][0]
    mask_B = masks[f'{label}'][1]

    logz_A = np.log(sum(weights[mask_A])) + logz_tot
    logz_B = np.log(sum(weights[mask_B])) + logz_tot

    # Output the row
    print(fr'{label:>40} & A & {exp_chi2_A:>5.2f} & {logz_A:>4.2f} \pm {dlogz:2.2f}\\')
    print(fr'{label:>40} & B & {exp_chi2_B:>5.2f} & {logz_B:>4.2f} \pm {dlogz:2.2f}\\')

print('')