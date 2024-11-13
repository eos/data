import eos
import numpy as np
import matplotlib.pyplot as plt
from wquantiles import quantile

def predicted_95(post,pred,which,mask):
    prediction = eos.data.Prediction('data/'+post+'/pred-'+pred)
    samples = prediction.samples[mask]
    weights = prediction.weights[mask]/sum(prediction.weights[mask])
    return quantile(samples[:,which],weights,0.95)

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
# create masks for WET
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
    "WET1": mask_array[0],
    "WET2": mask_array[1],
    "WET3": mask_array[2],
    "WET4": mask_array[3]
}

# Making the plot
fig, ax = plt.subplots(ncols=1, figsize=(6,3.5))
fig.canvas.draw()

d = {
    "Gamma_B": {
        "latex": r"$\Gamma(b \to c\bar{u}q)$",
        "measured-cen": 0.476312,
        "predict-cen-WET1_A":  predicted_95('WET-1', 'Gamma', 0, masks['WET1'][0]),
        "predict-cen-WET1_B":  predicted_95('WET-1', 'Gamma', 0, masks['WET1'][1]),
        "predict-cen-WET2_A":  predicted_95('WET-2', 'Gamma', 0, masks['WET2'][0]),
        "predict-cen-WET2_B":  predicted_95('WET-2', 'Gamma', 0, masks['WET2'][1]),
        "predict-cen-WET3_A":  predicted_95('WET-3', 'Gamma', 0, masks['WET3'][0]),
        "predict-cen-WET3_B":  predicted_95('WET-3', 'Gamma', 0, masks['WET3'][1]),
        "predict-cen-WET4_A":  predicted_95('WET-4', 'Gamma', 0, masks['WET4'][0]),
        "predict-cen-WET4_B":  predicted_95('WET-4', 'Gamma', 0, masks['WET4'][1]),
    }
}

labels = []
for key in d.keys():
    labels.append(d[key]["latex"])
labels.append("")

yvals = list(range(1, len(labels)))
yvals.reverse()

yvals_WET1_A =  [yvals[i] + 0.025 for i in range(len(yvals))]
yvals_WET1_B =  [yvals[i] + 0.050 for i in range(len(yvals))]
yvals_WET2_A =  [yvals[i] + 0.075 for i in range(len(yvals))]
yvals_WET2_B =  [yvals[i] + 0.100 for i in range(len(yvals))]
yvals_WET3_A =  [yvals[i] + 0.125 for i in range(len(yvals))]
yvals_WET3_B =  [yvals[i] + 0.150 for i in range(len(yvals))]
yvals_WET4_A =  [yvals[i] + 0.175 for i in range(len(yvals))]
yvals_WET4_B =  [yvals[i] + 0.200 for i in range(len(yvals))]
predicts_err_WET1_A  = [[], []]
predicts_val_WET1_A  = []
predicts_err_WET1_B  = [[], []]
predicts_val_WET1_B  = []
predicts_err_WET2_A  = [[], []]
predicts_val_WET2_A  = []
predicts_err_WET2_B  = [[], []]
predicts_val_WET2_B  = []
predicts_err_WET3_A  = [[], []]
predicts_val_WET3_A  = []
predicts_err_WET3_B  = [[], []]
predicts_val_WET3_B  = []
predicts_err_WET4_A  = [[], []]
predicts_val_WET4_A  = []
predicts_err_WET4_B  = [[], []]
predicts_val_WET4_B  = []
measures_err = []
measures_val = []

for key in d.keys():
    # WET1
    predicts_val_WET1_A.append(d[key]["predict-cen-WET1_A"] / d[key]["measured-cen"])
    predicts_val_WET1_B.append(d[key]["predict-cen-WET1_B"] / d[key]["measured-cen"])

    # WET2
    predicts_val_WET2_A.append(d[key]["predict-cen-WET2_A"] / d[key]["measured-cen"])
    predicts_val_WET2_B.append(d[key]["predict-cen-WET2_B"] / d[key]["measured-cen"])

    # WET3
    predicts_val_WET3_A.append(d[key]["predict-cen-WET3_A"] / d[key]["measured-cen"])
    predicts_val_WET3_B.append(d[key]["predict-cen-WET3_B"] / d[key]["measured-cen"])

    # WET4
    predicts_val_WET4_A.append(d[key]["predict-cen-WET4_A"] / d[key]["measured-cen"])
    predicts_val_WET4_B.append(d[key]["predict-cen-WET4_B"] / d[key]["measured-cen"])

ax.errorbar(predicts_val_WET1_A,  yvals_WET1_A,  xerr=[predicts_val_WET1_A, [0]],  color="C1",    fmt="v", label=r"WET-1A")
ax.errorbar(predicts_val_WET1_B,  yvals_WET1_B,  xerr=[predicts_val_WET1_B, [0]],  color="C1",    fmt="s", label=r"WET-1B")
ax.errorbar(predicts_val_WET2_A,  yvals_WET2_A,  xerr=[predicts_val_WET2_A, [0]],  color="C2",    fmt="v", label=r"WET-2A")
ax.errorbar(predicts_val_WET2_B,  yvals_WET2_B,  xerr=[predicts_val_WET2_B, [0]],  color="C2",    fmt="s", label=r"WET-2B")
ax.errorbar(predicts_val_WET3_A,  yvals_WET3_A,  xerr=[predicts_val_WET3_A, [0]],  color="C3",    fmt="v", label=r"WET-3A")
ax.errorbar(predicts_val_WET3_B,  yvals_WET3_B,  xerr=[predicts_val_WET3_B, [0]],  color="C3",    fmt="s", label=r"WET-3B")
ax.errorbar(predicts_val_WET4_A,  yvals_WET4_A,  xerr=[predicts_val_WET4_A, [0]],  color="C4",    fmt="v", label=r"WET-4A")
ax.errorbar(predicts_val_WET4_B,  yvals_WET4_B,  xerr=[predicts_val_WET4_B, [0]],  color="C4",    fmt="s", label=r"WET-4B")

ax.set_yticks(([yvals[i] + 0.1 for i in range(len(yvals))] + [0])[::-1])
ax.yaxis.set_ticklabels(labels[::-1])
ax.set_xlabel(r"Saturation of $\Gamma(B^-)$")

ax.set_xlim([0.85,1.1])
ax.axvline(x = 1, color = 'lightgray')
ax.set_ylim([0.995,1.225])

ax.legend(loc='upper center',ncol=4,bbox_to_anchor=(0.5,1.3))

fig.savefig('figures/lifetime-comparison.png')
fig.savefig('figures/lifetime-comparison.pdf')