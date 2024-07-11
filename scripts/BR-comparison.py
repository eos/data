import eos
import numpy as np
import matplotlib.pyplot as plt
from wquantiles import quantile


def predicted_central(post,pred,which):
    prediction = eos.data.Prediction('data/'+post+'/pred-'+pred)
    return quantile(prediction.samples[:,which],prediction.weights,0.5)

def predicted_error(post,pred,which):
    prediction = eos.data.Prediction('data/'+post+'/pred-'+pred)
    low  = quantile(prediction.samples[:, which], prediction.weights, 0.5) - quantile(prediction.samples[:, which], prediction.weights, 0.5-0.34)
    high = quantile(prediction.samples[:, which], prediction.weights, 0.5+0.34) - quantile(prediction.samples[:, which], prediction.weights, 0.5)
    return [low, high]

# Making the pull plot
fig, ax = plt.subplots(ncols=1, figsize=(6,7.5))
fig.canvas.draw()

d = {
    "Dsmu+nu": {
        "latex": r"$\mathcal{B}(D_s^+ \to \mu^+ \nu)$",
        "measured-cen": 5.35e-03,
        "measured-err": 0.10e-03,
        "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 0),
        "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 0),
        "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 0),
        "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 0),
        "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 0),
        "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 0),
        "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 0),
        "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 0),
    },
    "Dstau+nu": {
        "latex": r"$\mathcal{B}(D_s^+\to\tau^+ \nu)$",
        "measured-cen": 5.39e-02,
        "measured-err": 0.12e-02,
        "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 1),
        "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 1),
        "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 1),
        "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 1),
        "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 1),
        "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 1),
        "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 1),
        "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 1),
    },
    # "Dsste+nu": {
    #     "latex": r"$\mathcal{B}(D_s^{*+}\to e^+ \nu)$",
    #     "measured-cen": 2.1e-05,
    #     "measured-err": 1.1e-05,
    #     "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 2),
    #     "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 2),
    #     "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 2),
    #     "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 2),
    #     "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 2),
    #     "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 2),
    #     "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 2),
    #     "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 2),
    # },
    "D0K-e+nu": {
        "latex": r"$\mathcal{B}(D^0\to K^- e^+ \nu)$",
        "measured-cen": 3.525e-02,
        "measured-err": 0.023e-02,
        "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 3),
        "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 3),
        "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 3),
        "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 3),
        "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 3),
        "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 3),
        "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 3),
        "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 3),
    },
    "D0K-mu+nu": {
        "latex": r"$\mathcal{B}(D^0\to K^- \mu^+ \nu)$",
        "measured-cen": 3.41e-02,
        "measured-err": 0.04e-02,
        "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 4),
        "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 4),
        "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 4),
        "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 4),
        "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 4),
        "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 4),
        "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 4),
        "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 4),
    },
    "DpK0bare+nu": {
        "latex": r"$\mathcal{B}(D^+\to \overline{K}^0 e^+ \nu)$",
        "measured-cen": 8.72e-02,
        "measured-err": 0.09e-02,
        "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 5),
        "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 5),
        "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 5),
        "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 5),
        "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 5),
        "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 5),
        "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 5),
        "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 5),
    },
    "DpK0barmu+nu": {
        "latex": r"$\mathcal{B}(D^+\to \overline{K}^0 \mu^+ \nu)$",
        "measured-cen": 8.72e-02,
        "measured-err": 0.19e-02,
        "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 6),
        "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 6),
        "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 6),
        "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 6),
        "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 6),
        "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 6),
        "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 6),
        "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 6),
    },
    "LcLe+nu": {
        "latex": r"$\mathcal{B}(\Lambda_c^+\to \Lambda e^+ \nu)$",
        "measured-cen": 3.56e-02,
        "measured-err": 0.13e-02,
        "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 7),
        "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 7),
        "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 7),
        "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 7),
        "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 7),
        "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 7),
        "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 7),
        "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 7),
    },
    #"LcLmu+nu": {
    #    "latex": r"$\mathcal{B}(\Lambda_c^+\to \Lambda \mu^+ \nu)$",
    #    "measured-cen": 3.49e-02,
    #    "measured-err": 0.53e-02,
    #    "predict-cen-TH":  predicted_central('TH-all',  'BR-comparison', 8),
    #    "predict-err-TH":  predicted_error(  'TH-all',  'BR-comparison', 8),
    #    "predict-cen-SM":  predicted_central('SM-all',  'BR-comparison', 8),
    #    "predict-err-SM":  predicted_error(  'SM-all',  'BR-comparison', 8),
    #    "predict-cen-CKM": predicted_central('CKM-all', 'BR-comparison', 8),
    #    "predict-err-CKM": predicted_error(  'CKM-all', 'BR-comparison', 8),
    #    "predict-cen-WET": predicted_central('WET-all', 'BR-comparison', 8),
    #    "predict-err-WET": predicted_error(  'WET-all', 'BR-comparison', 8),
    #},
}

labels = []
for key in d.keys():
    labels.append(d[key]["latex"])
labels.append(" ")

yvals = list(range(1, len(labels)))
yvals.reverse()

yvals_TH =  [yvals[i] + 0.05 for i in range(len(yvals))]
yvals_SM =  [yvals[i] + 0.10 for i in range(len(yvals))]
yvals_CKM = [yvals[i] + 0.15 for i in range(len(yvals))]
yvals_WET = [yvals[i] + 0.20 for i in range(len(yvals))]
predicts_err_TH = [[], []]
predicts_val_TH = []
predicts_err_SM = [[], []]
predicts_val_SM = []
predicts_err_CKM = [[], []]
predicts_val_CKM = []
predicts_err_WET = [[], []]
predicts_val_WET = []
measures_err = []
measures_val = []

for key in d.keys():
    # normalizing measured value
    measures_val.append(1.0)
    measures_err.append(d[key]["measured-err"] / d[key]["measured-cen"])

    # TH
    predicts_val_TH.append(d[key]["predict-cen-TH"] / d[key]["measured-cen"])
    predicts_err_TH[0].append(d[key]["predict-err-TH"][0] / d[key]["measured-cen"])
    predicts_err_TH[1].append(d[key]["predict-err-TH"][1] / d[key]["measured-cen"])

    # SM
    predicts_val_SM.append(d[key]["predict-cen-SM"] / d[key]["measured-cen"])
    predicts_err_SM[0].append(d[key]["predict-err-SM"][0] / d[key]["measured-cen"])
    predicts_err_SM[1].append(d[key]["predict-err-SM"][1] / d[key]["measured-cen"])

    # CKM
    predicts_val_CKM.append(d[key]["predict-cen-CKM"] / d[key]["measured-cen"])
    predicts_err_CKM[0].append(d[key]["predict-err-CKM"][0] / d[key]["measured-cen"])
    predicts_err_CKM[1].append(d[key]["predict-err-CKM"][1] / d[key]["measured-cen"])

    # # WET
    # predicts_val_WET.append(d[key]["predict-cen-WET"] / d[key]["measured-cen"])
    # predicts_err_WET[0].append(d[key]["predict-err-WET"][0] / d[key]["measured-cen"])
    # predicts_err_WET[1].append(d[key]["predict-err-WET"][1] / d[key]["measured-cen"])

ax.yaxis.set_ticklabels(labels[::-1])
ax.set_xlabel(r"$\mathcal{B}/\mathcal{B}_{\mathrm{measured}}$")
ax.set_xlim([0.945,1.13])
ax.axvline(x = 1, color = 'lightgray')
ax.axhline(y = 1.5, color = 'lightgray')
ax.axhline(y = 5.5, color = 'lightgray')
ax.set_ylim([0.5,len(labels)-0.5])

ax.errorbar(measures_val,     yvals,     xerr=measures_err,     color="black", fmt="d", label=r"measurement")
ax.errorbar(predicts_val_TH,  yvals_TH,  xerr=predicts_err_TH,  color="C4",    fmt="o", label=r"theory only")
ax.errorbar(predicts_val_SM,  yvals_SM,  xerr=predicts_err_SM,  color="C6",    fmt="v", label=r"SM posterior prediction")
ax.errorbar(predicts_val_CKM, yvals_CKM, xerr=predicts_err_CKM, color="C9",    fmt="s", label=r"CKM posterior prediction")
# ax.errorbar(predicts_val_WET, yvals_WET, xerr=predicts_err_WET, color="C10",   fmt="*", label=r"WET posterior prediction")


ax.legend(loc='upper center',ncol=2,bbox_to_anchor=(0.5,1.15))

fig.savefig('figures/BR-comparison.png')
fig.savefig('figures/BR-comparison.pdf')