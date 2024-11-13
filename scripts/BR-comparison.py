import eos
import numpy as np
import matplotlib.pyplot as plt
from wquantiles import quantile

def predicted_central(post,pred,which,mask):
    prediction = eos.data.Prediction('data/'+post+'/pred-'+pred)
    samples = prediction.samples[mask]
    weights = prediction.weights[mask]/sum(prediction.weights[mask])
    return quantile(samples[:,which],weights,0.5)

def predicted_error(post,pred,which,mask):
    prediction = eos.data.Prediction('data/'+post+'/pred-'+pred)
    samples = prediction.samples[mask]
    weights = prediction.weights[mask]/sum(prediction.weights[mask])
    low  = quantile(samples[:, which], weights, 0.5) - quantile(samples[:, which], weights, 0.5-0.34)
    high = quantile(samples[:, which], weights, 0.5+0.34) - quantile(samples[:, which], weights, 0.5)
    return [low, high]

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
# Create mask for SM
mask_SM = [True]*len(np.load(f'data/SM/samples/samples.npy')[:,0])
mask_SM_pred = [True]*len(np.load(f'data/TH/samples/samples.npy')[:,0])

# Making the pull plot
fig, ax = plt.subplots(ncols=1, figsize=(6,7.5))
fig.canvas.draw()

d = {
    "BstoDsPi": {
        "latex": r"$\mathcal{B}(\bar{B}_s \to D_s^+ \pi^-)$",
        "measured-cen": 3.38962585e-03,
        "measured-err": np.sqrt(5.06068025e-07),
        "predict-cen-TH":      predicted_central('TH',    'BRs', 0, mask_SM_pred),
        "predict-err-TH":      predicted_error(  'TH',    'BRs', 0, mask_SM_pred),
        "predict-cen-SM":      predicted_central('SM',    'BRs', 0, mask_SM),
        "predict-err-SM":      predicted_error(  'SM',    'BRs', 0, mask_SM),
        "predict-cen-WET1_A":  predicted_central('WET-1', 'BRs', 0, masks['WET1'][0]),
        "predict-err-WET1_A":  predicted_error(  'WET-1', 'BRs', 0, masks['WET1'][0]),
        "predict-cen-WET1_B":  predicted_central('WET-1', 'BRs', 0, masks['WET1'][1]),
        "predict-err-WET1_B":  predicted_error(  'WET-1', 'BRs', 0, masks['WET1'][1]),
        "predict-cen-WET2_A":  predicted_central('WET-2', 'BRs', 0, masks['WET2'][0]),
        "predict-err-WET2_A":  predicted_error(  'WET-2', 'BRs', 0, masks['WET2'][0]),
        "predict-cen-WET2_B":  predicted_central('WET-2', 'BRs', 0, masks['WET2'][1]),
        "predict-err-WET2_B":  predicted_error(  'WET-2', 'BRs', 0, masks['WET2'][1]),
        "predict-cen-WET3_A":  predicted_central('WET-3', 'BRs', 0, masks['WET3'][0]),
        "predict-err-WET3_A":  predicted_error(  'WET-3', 'BRs', 0, masks['WET3'][0]),
        "predict-cen-WET3_B":  predicted_central('WET-3', 'BRs', 0, masks['WET3'][1]),
        "predict-err-WET3_B":  predicted_error(  'WET-3', 'BRs', 0, masks['WET3'][1]),
        "predict-cen-WET4_A":  predicted_central('WET-4', 'BRs', 0, masks['WET4'][0]),
        "predict-err-WET4_A":  predicted_error(  'WET-4', 'BRs', 0, masks['WET4'][0]),
        "predict-cen-WET4_B":  predicted_central('WET-4', 'BRs', 0, masks['WET4'][1]),
        "predict-err-WET4_B":  predicted_error(  'WET-4', 'BRs', 0, masks['WET4'][1]),
    },
    "BtoDK": {
        "latex": r"$\mathcal{B}(\bar{B} \to D^+ K^-)$",
        "measured-cen": 2.24991193e-04,
        "measured-err": np.sqrt(1.50936535e-10),
        "predict-cen-TH":      predicted_central('TH',    'BRs', 1, mask_SM_pred),
        "predict-err-TH":      predicted_error(  'TH',    'BRs', 1, mask_SM_pred),
        "predict-cen-SM":      predicted_central('SM',    'BRs', 1, mask_SM),
        "predict-err-SM":      predicted_error(  'SM',    'BRs', 1, mask_SM),
        "predict-cen-WET1_A":  predicted_central('WET-1', 'BRs', 1, masks['WET1'][0]),
        "predict-err-WET1_A":  predicted_error(  'WET-1', 'BRs', 1, masks['WET1'][0]),
        "predict-cen-WET1_B":  predicted_central('WET-1', 'BRs', 1, masks['WET1'][1]),
        "predict-err-WET1_B":  predicted_error(  'WET-1', 'BRs', 1, masks['WET1'][1]),
        "predict-cen-WET2_A":  predicted_central('WET-2', 'BRs', 1, masks['WET2'][0]),
        "predict-err-WET2_A":  predicted_error(  'WET-2', 'BRs', 1, masks['WET2'][0]),
        "predict-cen-WET2_B":  predicted_central('WET-2', 'BRs', 1, masks['WET2'][1]),
        "predict-err-WET2_B":  predicted_error(  'WET-2', 'BRs', 1, masks['WET2'][1]),
        "predict-cen-WET3_A":  predicted_central('WET-3', 'BRs', 1, masks['WET3'][0]),
        "predict-err-WET3_A":  predicted_error(  'WET-3', 'BRs', 1, masks['WET3'][0]),
        "predict-cen-WET3_B":  predicted_central('WET-3', 'BRs', 1, masks['WET3'][1]),
        "predict-err-WET3_B":  predicted_error(  'WET-3', 'BRs', 1, masks['WET3'][1]),
        "predict-cen-WET4_A":  predicted_central('WET-4', 'BRs', 1, masks['WET4'][0]),
        "predict-err-WET4_A":  predicted_error(  'WET-4', 'BRs', 1, masks['WET4'][0]),
        "predict-cen-WET4_B":  predicted_central('WET-4', 'BRs', 1, masks['WET4'][1]),
        "predict-err-WET4_B":  predicted_error(  'WET-4', 'BRs', 1, masks['WET4'][1]),
    },
     "BstoDsstarPi": {
        "latex": r"$\mathcal{B}(\bar{B}_s \to D_s^{*+} \pi^-)$",
        "measured-cen": 2.23197453e-03,
        "measured-err": np.sqrt(5.16443796e-07),
        "predict-cen-TH":      predicted_central('TH',    'BRs', 2, mask_SM_pred),
        "predict-err-TH":      predicted_error(  'TH',    'BRs', 2, mask_SM_pred),
        "predict-cen-SM":      predicted_central('SM',    'BRs', 2, mask_SM),
        "predict-err-SM":      predicted_error(  'SM',    'BRs', 2, mask_SM),
        "predict-cen-WET1_A":  predicted_central('WET-1', 'BRs', 2, masks['WET1'][0]),
        "predict-err-WET1_A":  predicted_error(  'WET-1', 'BRs', 2, masks['WET1'][0]),
        "predict-cen-WET1_B":  predicted_central('WET-1', 'BRs', 2, masks['WET1'][1]),
        "predict-err-WET1_B":  predicted_error(  'WET-1', 'BRs', 2, masks['WET1'][1]),
        "predict-cen-WET2_A":  predicted_central('WET-2', 'BRs', 2, masks['WET2'][0]),
        "predict-err-WET2_A":  predicted_error(  'WET-2', 'BRs', 2, masks['WET2'][0]),
        "predict-cen-WET2_B":  predicted_central('WET-2', 'BRs', 2, masks['WET2'][1]),
        "predict-err-WET2_B":  predicted_error(  'WET-2', 'BRs', 2, masks['WET2'][1]),
        "predict-cen-WET3_A":  predicted_central('WET-3', 'BRs', 2, masks['WET3'][0]),
        "predict-err-WET3_A":  predicted_error(  'WET-3', 'BRs', 2, masks['WET3'][0]),
        "predict-cen-WET3_B":  predicted_central('WET-3', 'BRs', 2, masks['WET3'][1]),
        "predict-err-WET3_B":  predicted_error(  'WET-3', 'BRs', 2, masks['WET3'][1]),
        "predict-cen-WET4_A":  predicted_central('WET-4', 'BRs', 2, masks['WET4'][0]),
        "predict-err-WET4_A":  predicted_error(  'WET-4', 'BRs', 2, masks['WET4'][0]),
        "predict-cen-WET4_B":  predicted_central('WET-4', 'BRs', 2, masks['WET4'][1]),
        "predict-err-WET4_B":  predicted_error(  'WET-4', 'BRs', 2, masks['WET4'][1]),
    },
    "BtoDstarK": {
        "latex": r"$\mathcal{B}(\bar{B} \to D^{*+} K^-)$",
        "measured-cen": 2.22760567e-04,
        "measured-err": np.sqrt(2.05122405e-10),
        "predict-cen-TH":      predicted_central('TH',    'BRs', 3, mask_SM_pred),
        "predict-err-TH":      predicted_error(  'TH',    'BRs', 3, mask_SM_pred),
        "predict-cen-SM":      predicted_central('SM',    'BRs', 3, mask_SM),
        "predict-err-SM":      predicted_error(  'SM',    'BRs', 3, mask_SM),
        "predict-cen-WET1_A":  predicted_central('WET-1', 'BRs', 3, masks['WET1'][0]),
        "predict-err-WET1_A":  predicted_error(  'WET-1', 'BRs', 3, masks['WET1'][0]),
        "predict-cen-WET1_B":  predicted_central('WET-1', 'BRs', 3, masks['WET1'][1]),
        "predict-err-WET1_B":  predicted_error(  'WET-1', 'BRs', 3, masks['WET1'][1]),
        "predict-cen-WET2_A":  predicted_central('WET-2', 'BRs', 3, masks['WET2'][0]),
        "predict-err-WET2_A":  predicted_error(  'WET-2', 'BRs', 3, masks['WET2'][0]),
        "predict-cen-WET2_B":  predicted_central('WET-2', 'BRs', 3, masks['WET2'][1]),
        "predict-err-WET2_B":  predicted_error(  'WET-2', 'BRs', 3, masks['WET2'][1]),
        "predict-cen-WET3_A":  predicted_central('WET-3', 'BRs', 3, masks['WET3'][0]),
        "predict-err-WET3_A":  predicted_error(  'WET-3', 'BRs', 3, masks['WET3'][0]),
        "predict-cen-WET3_B":  predicted_central('WET-3', 'BRs', 3, masks['WET3'][1]),
        "predict-err-WET3_B":  predicted_error(  'WET-3', 'BRs', 3, masks['WET3'][1]),
        "predict-cen-WET4_A":  predicted_central('WET-4', 'BRs', 3, masks['WET4'][0]),
        "predict-err-WET4_A":  predicted_error(  'WET-4', 'BRs', 3, masks['WET4'][0]),
        "predict-cen-WET4_B":  predicted_central('WET-4', 'BRs', 3, masks['WET4'][1]),
        "predict-err-WET4_B":  predicted_error(  'WET-4', 'BRs', 3, masks['WET4'][1]),
    }
}

labels = []
for key in d.keys():
    labels.append(d[key]["latex"])
labels.append("")

yvals = list(range(1, len(labels)))
yvals = [1.2 * yval for yval in yvals]
yvals.reverse()

yvals_SM_pred = [yvals[i] + 0.10 for i in range(len(yvals))]
yvals_SM =      [yvals[i] + 0.20 for i in range(len(yvals))]
yvals_WET1_A =  [yvals[i] + 0.30 for i in range(len(yvals))]
yvals_WET1_B =  [yvals[i] + 0.40 for i in range(len(yvals))]
yvals_WET2_A =  [yvals[i] + 0.50 for i in range(len(yvals))]
yvals_WET2_B =  [yvals[i] + 0.60 for i in range(len(yvals))]
yvals_WET3_A =  [yvals[i] + 0.70 for i in range(len(yvals))]
yvals_WET3_B =  [yvals[i] + 0.80 for i in range(len(yvals))]
yvals_WET4_A =  [yvals[i] + 0.90 for i in range(len(yvals))]
yvals_WET4_B =  [yvals[i] + 1.00 for i in range(len(yvals))]
predicts_err_SM_pred = [[], []]
predicts_val_SM_pred = []
predicts_err_SM      = [[], []]
predicts_val_SM      = []
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
    # normalizing measured value
    measures_val.append(1.0)
    measures_err.append(d[key]["measured-err"] / d[key]["measured-cen"])

    # TH
    predicts_val_SM_pred.append(d[key]["predict-cen-TH"] / d[key]["measured-cen"])
    predicts_err_SM_pred[0].append(d[key]["predict-err-TH"][0] / d[key]["measured-cen"])
    predicts_err_SM_pred[1].append(d[key]["predict-err-TH"][1] / d[key]["measured-cen"])
    # SM
    predicts_val_SM.append(d[key]["predict-cen-SM"] / d[key]["measured-cen"])
    predicts_err_SM[0].append(d[key]["predict-err-SM"][0] / d[key]["measured-cen"])
    predicts_err_SM[1].append(d[key]["predict-err-SM"][1] / d[key]["measured-cen"])

    # WET1
    predicts_val_WET1_A.append(d[key]["predict-cen-WET1_A"] / d[key]["measured-cen"])
    predicts_err_WET1_A[0].append(d[key]["predict-err-WET1_A"][0] / d[key]["measured-cen"])
    predicts_err_WET1_A[1].append(d[key]["predict-err-WET1_A"][1] / d[key]["measured-cen"])

    predicts_val_WET1_B.append(d[key]["predict-cen-WET1_B"] / d[key]["measured-cen"])
    predicts_err_WET1_B[0].append(d[key]["predict-err-WET1_B"][0] / d[key]["measured-cen"])
    predicts_err_WET1_B[1].append(d[key]["predict-err-WET1_B"][1] / d[key]["measured-cen"])

    # WET2
    predicts_val_WET2_A.append(d[key]["predict-cen-WET2_A"] / d[key]["measured-cen"])
    predicts_err_WET2_A[0].append(d[key]["predict-err-WET2_A"][0] / d[key]["measured-cen"])
    predicts_err_WET2_A[1].append(d[key]["predict-err-WET2_A"][1] / d[key]["measured-cen"])

    predicts_val_WET2_B.append(d[key]["predict-cen-WET2_B"] / d[key]["measured-cen"])
    predicts_err_WET2_B[0].append(d[key]["predict-err-WET2_B"][0] / d[key]["measured-cen"])
    predicts_err_WET2_B[1].append(d[key]["predict-err-WET2_B"][1] / d[key]["measured-cen"])

    # WET3
    predicts_val_WET3_A.append(d[key]["predict-cen-WET3_A"] / d[key]["measured-cen"])
    predicts_err_WET3_A[0].append(d[key]["predict-err-WET3_A"][0] / d[key]["measured-cen"])
    predicts_err_WET3_A[1].append(d[key]["predict-err-WET3_A"][1] / d[key]["measured-cen"])

    predicts_val_WET3_B.append(d[key]["predict-cen-WET3_B"] / d[key]["measured-cen"])
    predicts_err_WET3_B[0].append(d[key]["predict-err-WET3_B"][0] / d[key]["measured-cen"])
    predicts_err_WET3_B[1].append(d[key]["predict-err-WET3_B"][1] / d[key]["measured-cen"])

    # WET3
    predicts_val_WET4_A.append(d[key]["predict-cen-WET4_A"] / d[key]["measured-cen"])
    predicts_err_WET4_A[0].append(d[key]["predict-err-WET4_A"][0] / d[key]["measured-cen"])
    predicts_err_WET4_A[1].append(d[key]["predict-err-WET4_A"][1] / d[key]["measured-cen"])

    predicts_val_WET4_B.append(d[key]["predict-cen-WET4_B"] / d[key]["measured-cen"])
    predicts_err_WET4_B[0].append(d[key]["predict-err-WET4_B"][0] / d[key]["measured-cen"])
    predicts_err_WET4_B[1].append(d[key]["predict-err-WET4_B"][1] / d[key]["measured-cen"])

ax.errorbar(measures_val,         yvals,         xerr=measures_err,         color="black", fmt="o", label=r"measurement")
ax.errorbar(predicts_val_SM_pred, yvals_SM_pred, xerr=predicts_err_SM_pred, color="C5",    fmt="o", label=r"TH")
ax.errorbar(predicts_val_SM,      yvals_SM,      xerr=predicts_err_SM,      color="C0",    fmt="o", label=r"SM")
ax.errorbar(predicts_val_WET1_A,  yvals_WET1_A,  xerr=predicts_err_WET1_A,  color="C1",    fmt="v", label=r"WET-1A")
ax.errorbar(predicts_val_WET1_B,  yvals_WET1_B,  xerr=predicts_err_WET1_B,  color="C1",    fmt="s", label=r"WET-1B")
ax.errorbar(predicts_val_WET2_A,  yvals_WET2_A,  xerr=predicts_err_WET2_A,  color="C2",    fmt="v", label=r"WET-2A")
ax.errorbar(predicts_val_WET2_B,  yvals_WET2_B,  xerr=predicts_err_WET2_B,  color="C2",    fmt="s", label=r"WET-2B")
ax.errorbar(predicts_val_WET3_A,  yvals_WET3_A,  xerr=predicts_err_WET3_A,  color="C3",    fmt="v", label=r"WET-3A")
ax.errorbar(predicts_val_WET3_B,  yvals_WET3_B,  xerr=predicts_err_WET3_B,  color="C3",    fmt="s", label=r"WET-3B")
ax.errorbar(predicts_val_WET4_A,  yvals_WET4_A,  xerr=predicts_err_WET4_A,  color="C4",    fmt="v", label=r"WET-4A")
ax.errorbar(predicts_val_WET4_B,  yvals_WET4_B,  xerr=predicts_err_WET4_B,  color="C4",    fmt="s", label=r"WET-4B")

ax.set_yticks((yvals + [0])[::-1])
ax.yaxis.set_ticklabels(labels[::-1])
ax.set_xlabel(r"$\mathcal{B}/\mathcal{B}_{\mathrm{measured}}$")
ax.set_xlim([0.6,2.2])
ax.axvline(x = 1, color = 'lightgray')
ax.set_ylim([0.75,1.2*len(labels)])

ax.legend(loc='upper center',ncol=4,bbox_to_anchor=(0.5,1.2))

fig.savefig('figures/BR-comparison.png')
fig.savefig('figures/BR-comparison.pdf')