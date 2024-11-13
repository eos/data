import eos
import matplotlib
import scipy
import numpy as np
import matplotlib.pyplot as plt
import logging
import ellipse

from scipy.stats import gaussian_kde
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.legend_handler import HandlerTuple

eos.logger.setLevel(logging.INFO)

posterior = "WET-1"

nWC = 4

samples = np.load("data/"+posterior+"/samples/samples.npy")[:,:nWC]
weights = np.load("data/"+posterior+"/samples/weights.npy")

analysis = eos.AnalysisFile('analysis.yaml').analysis(posterior)

samples = np.concatenate((samples, -samples))
weights = np.concatenate((weights, weights)) / 2

# Separate modes
wc1WET1 = samples[:,0]
wc2WET1 = samples[:,1]
maskWET1_A = (((wc1WET1 > -1.6 - 1.17 * wc2WET1) & (wc1WET1 < - 1.17 * wc2WET1)) | ((wc1WET1 < 1.6 - 1.17 * wc2WET1) & (wc1WET1 > - 1.17 * wc2WET1)))
maskWET1_B = ((wc1WET1 < -1.6 - 1.17 * wc2WET1) | (wc1WET1 > 1.6 - 1.17 * wc2WET1))

samples_A = samples[maskWET1_A]
weights_A = weights[maskWET1_A] / sum(weights[maskWET1_A])
samples_B = samples[maskWET1_B]
weights_B = weights[maskWET1_B] / sum(weights[maskWET1_B])

# Read the bounds from the analysis
params = analysis.varied_parameters
bounds = [(samples[:,i].min(), samples[:,i].max()) for i in range(nWC)]

# Main color
color  = "C0"
color2 = "C1"

# Multiplication factor for the KDE estimate
kde_smearing = 1.0

# Show datapoints?
points = True

# SM point
SM_point = [-0.041469, -0.899772, 0.011126, 0.194904]

fig, axes = plt.subplots(nWC, nWC, figsize=(3.0 * nWC, 3.0 * nWC), dpi=100)

# add lifetime ellipse
ellipse.plot_ellipses(axes, 1, 4, SM=False)

legended_plot = axes[2, 0]

for i in range(nWC):
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

    ax.vlines(SM_point[i],     ax.get_ylim()[0], ax.get_ylim()[1], color="k")

    if i == nWC - 1:
        ax.set_xlabel(params[i].latex())
    else:
        ax.xaxis.set_major_formatter(plt.NullFormatter())
        ax.xaxis.set_tick_params(bottom=False)

    for j in range(0, nWC):
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

        ax.plot(SM_point[j], SM_point[i], marker='+', markeredgewidth=3, ls='none', ms=15, alpha=0.5, color="k")
        # Set bounds
        ax.set_xlim(left=xmin, right=xmax)
        ax.set_ylim(bottom=ymin, top=ymax)
        ax.set_xbound(lower=xmin, upper=xmax)
        ax.set_ybound(lower=ymin, upper=ymax)

        if j == 0:
            ax.set_ylabel(params[i].latex())
        else:
            ax.yaxis.set_major_formatter(plt.NullFormatter())
            ax.yaxis.set_tick_params(left=False)

        if i == nWC - 1:
            ax.set_xlabel(params[j].latex())
        else:
            ax.xaxis.set_major_formatter(plt.NullFormatter())
            ax.xaxis.set_tick_params(bottom=False)

# Watermark
xdelta, ydelta = (0.05, 0.04)

ax = axes[nWC - 1, 0]
version = 'v{version}'.format(version=eos.__version__)
ax.text(xdelta, ydelta, r'\textsf{{\textbf{{EOS {version}}}}}'.format(version=version),
        transform=ax.transAxes,
        color='OrangeRed', alpha=0.5, bbox=dict(facecolor='white', alpha=0.5, lw=0),
        horizontalalignment='left', verticalalignment='bottom', zorder=+5)

# Caption
rec1 = plt.Rectangle((0,0),1,1, color=color, alpha=0.8)
rec2 = plt.Rectangle((0,0),1,1, color=color2, alpha=0.8)
sm_point,  = plt.plot([1],[0], marker='+', markeredgewidth=3, ls='none', ms=15, alpha=0.5, color="k")
sm_line =  plt.vlines(1, 0, 0, color="k")


legended_plot.legend(handles=[rec1, rec2, (sm_line, sm_point)], labels = ["A", "B", "SM"],
                     loc='lower left', handler_map={tuple: HandlerTuple(ndivide=None)})

fig.tight_layout()
fig.savefig("figures/WET-1.pdf", bbox_inches='tight', dpi=300)
fig.savefig("figures/WET-1.png", bbox_inches='tight', dpi=300)