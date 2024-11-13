import eos
import matplotlib
import scipy
import numpy as np
import matplotlib.pyplot as plt
import logging

from scipy.stats import gaussian_kde
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.legend_handler import HandlerTuple

eos.logger.setLevel(logging.INFO)

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
    "WET-1": mask_array[0],
    "WET-2": mask_array[1],
    "WET-3": mask_array[2],
    "WET-4": mask_array[3]
}

nBRs = 4
# Main color
color  = "C0"
color2 = "C1"

# Multiplication factor for the KDE estimate
kde_smearing = 1.0

# Show datapoints?
points = True

for id in ids:
    posterior = id

    samples = np.load("data/"+posterior+"/pred-BRs/samples.npy")
    weights = np.load("data/"+posterior+"/pred-BRs/weights.npy")

    samples_A = samples[masks[posterior][0]]
    weights_A = weights[masks[posterior][0]] / sum(weights[masks[posterior][0]])
    samples_B = samples[masks[posterior][1]]
    weights_B = weights[masks[posterior][1]] / sum(weights[masks[posterior][1]])

    analysis = analysis_file.analysis(posterior)

    params = [r"$\mathcal{B}(\bar{B}_s \to D_s^+ \pi^-)$", r"$\mathcal{B}(\bar{B} \to D^+ K^-)$",
          r"$\mathcal{B}(\bar{B}_s \to D_s^{*+} \pi^-)$", r"$\mathcal{B}(\bar{B} \to D^{*+} K^-)$"]

    bounds = [(2.0e-3, 5.0e-3), (0.15e-3, 0.3e-3), (1.0e-3,4.6e-3), (0.15e-3,0.3e-3)]

    fig, axes = plt.subplots(nBRs, nBRs, figsize=(3.0 * nBRs, 3.0 * nBRs), dpi=100)

    legended_plot = axes[2, 0]

    for i in range(nBRs):
        # diagonal
        ax = axes[i, i]
        xsamples_A = samples_A[:, i]
        xsamples_B = samples_B[:, i]

        xmin = bounds[i][0]
        xmax = bounds[i][1]

        kde_A = gaussian_kde(xsamples_A, weights=weights_A)
        kde_A.set_bandwidth(bw_method='silverman')
        kde_A.set_bandwidth(bw_method=kde_A.factor * kde_smearing)

        kde_B = gaussian_kde(xsamples_B, weights=weights_B)
        kde_B.set_bandwidth(bw_method='silverman')
        kde_B.set_bandwidth(bw_method=kde_B.factor * kde_smearing)

        x = np.linspace(xmin, xmax, 100)
        pdf_A = kde_A(x)
        pdf_B = kde_B(x)
        pdf_norm_A = pdf_A.sum()
        pdf_norm_B = pdf_B.sum()

        ax.plot(x, pdf_A, color=color)
        ax.plot(x, pdf_B, color=color2)

        plevelf_A = lambda x, pdf_A, P: pdf_A[pdf_A > x * pdf_norm_A].sum() - P * pdf_norm_A
        plevel_A = scipy.optimize.brentq(plevelf_A, 0., 1., args=(pdf_A, 68.27 / 100.0 ))
        ax.fill_between(np.ma.masked_array(x, mask=pdf_A < plevel_A * pdf_norm_A),
                        np.ma.masked_array(pdf_A, mask=pdf_A < plevel_A * pdf_norm_A, fill_value=np.nan),
                        facecolor=color, alpha=0.4)

        plevelf_B = lambda x, pdf_B, P: pdf_B[pdf_B > x * pdf_norm_B].sum() - P * pdf_norm_B
        plevel_B = scipy.optimize.brentq(plevelf_B, 0., 1., args=(pdf_B, 68.27 / 100.0 ))
        ax.fill_between(np.ma.masked_array(x, mask=pdf_B < plevel_B * pdf_norm_B),
                        np.ma.masked_array(pdf_B, mask=pdf_B < plevel_B * pdf_norm_B, fill_value=np.nan),
                        facecolor=color2, alpha=0.4)

        ax.set_xlim(left=xmin, right=xmax)
        ax.set_xbound(lower=xmin, upper=xmax)
        ax.set_ylim(bottom=0)
        ax.yaxis.set_major_formatter(plt.NullFormatter())
        ax.yaxis.set_tick_params(left=False)


        if i == nBRs - 1:
            ax.set_xlabel(params[i])
        else:
            ax.xaxis.set_major_formatter(plt.NullFormatter())
            ax.xaxis.set_tick_params(bottom=False)

        for j in range(0, nBRs):
            if j > i:
                axes[i, j].set_axis_off()

            if j >= i:
                continue

            ax = axes[i, j]
            xsamples_A = samples_A[:, j]
            ysamples_A = samples_A[:, i]
            xsamples_B = samples_B[:, j]
            ysamples_B = samples_B[:, i]
            xsamples = samples[:, j]
            ysamples = samples[:, i]
            xmin = bounds[j][0]
            xmax = bounds[j][1]
            ymin = bounds[i][0]
            ymax = bounds[i][1]
            if points:
                ax.hist2d(xsamples, ysamples, weights=weights, alpha=1.0,
                        bins=[np.linspace(xmin, xmax, 100), np.linspace(ymin, ymax, 100)],
                        cmap='Greys', rasterized=True)

            xysamples_A = samples_A[:, (j, i)]
            kde_A = gaussian_kde(np.transpose(xysamples_A), weights=weights_A)
            kde_A.set_bandwidth(bw_method='silverman')
            kde_A.set_bandwidth(bw_method=kde_A.factor * kde_smearing)

            xysamples_B = samples_B[:, (j, i)]
            kde_B = gaussian_kde(np.transpose(xysamples_B), weights=weights_B)
            kde_B.set_bandwidth(bw_method='silverman')
            kde_B.set_bandwidth(bw_method=kde_B.factor * kde_smearing)

            xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
            positions = np.vstack([xx.ravel(), yy.ravel()])
            pdf_A = np.reshape(kde_A(positions).T, xx.shape)
            pdf_A /= pdf_A.sum()
            pdf_B = np.reshape(kde_B(positions).T, xx.shape)
            pdf_B /= pdf_B.sum()

            # find the PDF value corresponding to a given cummulative probability
            plevel_A = lambda x, pdf_A, P: pdf_A[pdf_A > x].sum() - P
            plevels_A = []
            labels_A = []
            for level in [0, 68, 95, 99]:
                plevels_A.append(scipy.optimize.brentq(plevel_A, 0., 1., args=(pdf_A, level / 100.0)))
                labels_A.append('{}%'.format(level))

            plevel_B = lambda x, pdf_B, P: pdf_B[pdf_B > x].sum() - P
            plevels_B = []
            labels_B = []
            for level in [0, 68, 95, 99]:
                plevels_B.append(scipy.optimize.brentq(plevel_B, 0., 1., args=(pdf_B, level / 100.0)))
                labels_B.append('{}%'.format(level))

            colors  = [matplotlib.colors.to_rgba(color, alpha) for alpha in np.linspace(0.20, 0.80, 4)]
            colors2 = [matplotlib.colors.to_rgba(color2, alpha) for alpha in np.linspace(0.20, 0.80, 4)]
            ax.contourf(pdf_A.transpose(),
                        colors=colors,
                        extent=[xmin, xmax, ymin, ymax],
                        levels=plevels_A[::-1])
            ax.contourf(pdf_B.transpose(),
                        colors=colors2,
                        extent=[xmin, xmax, ymin, ymax],
                        levels=plevels_B[::-1])


            ax.grid(visible=True, alpha=0.25)

            # Set bounds
            ax.set_xlim(left=xmin, right=xmax)
            ax.set_ylim(bottom=ymin, top=ymax)
            ax.set_xbound(lower=xmin, upper=xmax)
            ax.set_ybound(lower=ymin, upper=ymax)

            if j == 0:
                ax.set_ylabel(params[i])
            else:
                ax.yaxis.set_major_formatter(plt.NullFormatter())
                ax.yaxis.set_tick_params(left=False)

            if i == nBRs - 1:
                ax.set_xlabel(params[j])
            else:
                ax.xaxis.set_major_formatter(plt.NullFormatter())
                ax.xaxis.set_tick_params(bottom=False)

    # Watermark
    xdelta, ydelta = (0.05, 0.04)

    ax = axes[nBRs - 1, 0]
    version = 'v{version}'.format(version=eos.__version__)
    ax.text(xdelta, ydelta, r'\textsf{{\textbf{{EOS {version}}}}}'.format(version=version),
            transform=ax.transAxes,
            color='OrangeRed', alpha=0.5, bbox=dict(facecolor='white', alpha=0.5, lw=0),
            horizontalalignment='left', verticalalignment='bottom', zorder=+5)

    # Caption
    rec1 = plt.Rectangle((0,0), 1, 1, color=color,  alpha=0.8)
    rec2 = plt.Rectangle((0,0), 1, 1, color=color2, alpha=0.8)


    legended_plot.legend(handles=[rec1, rec2], labels = [f'{id}A', f'{id}B'],
                     loc='lower left', handler_map={tuple: HandlerTuple(ndivide=None)})

    fig.tight_layout()
    fig.savefig(f'figures/BR-corner-{id}.pdf', bbox_inches='tight', dpi=300)
    fig.savefig(f'figures/BR-corner-{id}.png', bbox_inches='tight', dpi=300)