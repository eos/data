import eos
import matplotlib
import scipy
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import gaussian_kde
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.legend_handler import HandlerTuple

posterior = "WET-all"

nWC = 9

samples = np.load("data/"+posterior+"/samples/samples.npy")[:,:nWC]
weights = np.load("data/"+posterior+"/samples/weights.npy")

analysis = eos.AnalysisFile('analysis.yaml').analysis(posterior)

# Symmetrize the samples
samples = np.concatenate([samples, [1,1,1,1,1,-1,-1,-1,-1] * samples])
weights = np.concatenate([weights, weights])

# Read the bounds from the analysis
params = analysis.varied_parameters
bounds =  [(params[i].min(), params[i].max()) for i in range(nWC)]

# Main color
color = "C0"

# Multiplication factor for the KDE estimate
kde_smearing = 1.5

# Show datapoints?
points = True

# SM point
SM_point = [1.01, 0, 0, 0, 0, 0, 0, 0, 0]

# bfp
bfp, _ = eos.find_mode('analysis.yaml', posterior, base_directory="data", importance_samples=True, optimizations=10)
bfp1 = bfp.point[:nWC]
bfp2 = [1,1,1,1,1,-1,-1,-1,-1] * bfp.point[:nWC]

fig, axes = plt.subplots(nWC, nWC, figsize=(3.0 * nWC, 3.0 * nWC), dpi=100)

legended_plot = axes[1, 0]

for i in range(nWC):
    # diagonal
    ax = axes[i, i]
    xsamples = samples[:, i]

    xmin = bounds[i][0]
    xmax = bounds[i][1]

    kde = gaussian_kde(xsamples, weights=weights)
    kde.set_bandwidth(bw_method='silverman')
    kde.set_bandwidth(bw_method=kde.factor * kde_smearing)

    x = np.linspace(xmin, xmax, 100)
    pdf = kde(x)
    pdf_norm = pdf.sum()

    ax.plot(x, pdf, color=color)

    plevelf = lambda x, pdf, P: pdf[pdf > x * pdf_norm].sum() - P * pdf_norm
    plevel = scipy.optimize.brentq(plevelf, 0., 1., args=(pdf, 68.27 / 100.0 ))
    ax.fill_between(np.ma.masked_array(x, mask=pdf < plevel * pdf_norm),
                    np.ma.masked_array(pdf, mask=pdf < plevel * pdf_norm, fill_value=np.nan),
                    facecolor=color, alpha=0.4)

    ax.set_xlim(left=xmin, right=xmax)
    ax.set_xbound(lower=xmin, upper=xmax)
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_tick_params(left=False)

    ax.vlines(SM_point[i], ax.get_ylim()[0], ax.get_ylim()[1], color="k")
    ax.vlines(bfp1[i],     ax.get_ylim()[0], ax.get_ylim()[1], ls = 'dotted', color="k")
    ax.vlines(bfp2[i],     ax.get_ylim()[0], ax.get_ylim()[1], ls = 'dotted', color="k")

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

        xysamples = samples[:, (j, i)]
        kde = gaussian_kde(np.transpose(xysamples), weights=weights)
        kde.set_bandwidth(bw_method='silverman')
        kde.set_bandwidth(bw_method=kde.factor * 1.5)

        xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
        positions = np.vstack([xx.ravel(), yy.ravel()])
        pdf = np.reshape(kde(positions).T, xx.shape)
        pdf /= pdf.sum()

        # find the PDF value corresponding to a given cummulative probability
        plevel = lambda x, pdf, P: pdf[pdf > x].sum() - P
        plevels = []
        labels = []
        for level in [0, 68, 95, 99]:
            plevels.append(scipy.optimize.brentq(plevel, 0., 1., args=(pdf, level / 100.0)))
            labels.append('{}%'.format(level))

        colors = [matplotlib.colors.to_rgba(color, alpha) for alpha in np.linspace(0.20, 0.80, 4)]
        ax.contourf(pdf.transpose(),
                     colors=colors,
                     extent=[xmin, xmax, ymin, ymax],
                     levels=plevels[::-1])

        ax.grid(visible=True, alpha=0.25)

        ax.plot(SM_point[j], SM_point[i], marker='+', markeredgewidth=3, ls='none', ms=15, alpha=0.5, color="k")
        ax.plot(bfp1[j], bfp1[i],         marker='x', markeredgewidth=3, ls='none', ms=10, alpha=0.5, color="k")
        ax.plot(bfp2[j], bfp2[i],         marker='x', markeredgewidth=3, ls='none', ms=10, alpha=0.5, color="k")

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
rec = plt.Rectangle((0,0),1,1, color=color, alpha=0.8)
sm_point,  = plt.plot([1],[0], marker='+', markeredgewidth=3, ls='none', ms=15, alpha=0.5, color="k")
bfp_point, = plt.plot([1],[0], marker='x', markeredgewidth=3, ls='none', ms=10, alpha=0.5, color="k")
sm_line =  plt.vlines(1, 0, 0, color="k")
bfp_line = plt.vlines(1, 0, 0, ls = 'dotted', color="k")


legended_plot.legend(handles=[rec, (sm_line, sm_point), (bfp_line, bfp_point)], labels = ["all data", "SM", "bfp"],
                     loc='upper left', handler_map={tuple: HandlerTuple(ndivide=None)})

fig.tight_layout()
fig.savefig("figures/WET-all.pdf", bbox_inches='tight', dpi=300)
fig.savefig("figures/WET-all.png", bbox_inches='tight', dpi=300)
