import eos
import matplotlib
import scipy
import numpy as np
import matplotlib.pyplot as plt
import ellipse

from scipy.stats import gaussian_kde
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.legend_handler import HandlerTuple

posterior = "WET-3"

nWC = 4

samples = np.load("data/"+posterior+"/samples/samples.npy")[:,:nWC]
weights = np.load("data/"+posterior+"/samples/weights.npy")

analysis = eos.AnalysisFile('analysis.yaml').analysis(posterior)

# Separate modes
wc1pWET3 = samples[:,0]
wc2pWET3 = samples[:,1]
maskWET3_1 = wc1pWET3 < 1.15 - 1.17 * wc2pWET3
maskWET3_2 = ((wc1pWET3 > 1.15 - 1.17 * wc2pWET3) & (wc1pWET3 < 2.45 - 1.17 * wc2pWET3))
samples_1 = samples[maskWET3_1]
weights_1 = weights[maskWET3_1] / sum(weights[maskWET3_1])
samples_2 = samples[maskWET3_2]
weights_2 = weights[maskWET3_2] / sum(weights[maskWET3_2])

# Read the bounds from the analysis
params = analysis.varied_parameters

bounds = [(samples[:,i].min(), samples[:,i].max()) for i in range(nWC)]
# Main color
color = "C0"
color2 = "C1"
# Multiplication factor for the KDE estimate
kde_smearing = 1.0

# Show datapoints?
points = True

# SM point
SM_point = [0, 0, 0, 0]

fig, axes = plt.subplots(nWC, nWC, figsize=(3.0 * nWC, 3.0 * nWC), dpi=100)

# add lifetime ellipse
ellipse.plot_ellipses(axes, 1, 4)

legended_plot = axes[2, 0]

for i in range(nWC):
    # diagonal
    ax = axes[i, i]
    xsamples_1 = samples_1[:, i]
    xsamples_2 = samples_2[:, i]

    xmin = bounds[i][0]
    xmax = bounds[i][1]

    kde_1 = gaussian_kde(xsamples_1, weights=weights_1)
    kde_1.set_bandwidth(bw_method='silverman')
    kde_1.set_bandwidth(bw_method=kde_1.factor * kde_smearing)

    kde_2 = gaussian_kde(xsamples_2, weights=weights_2)
    kde_2.set_bandwidth(bw_method='silverman')
    kde_2.set_bandwidth(bw_method=kde_2.factor * kde_smearing)

    x = np.linspace(xmin, xmax, 100)
    pdf_1 = kde_1(x)
    pdf_2 = kde_2(x)
    pdf_norm_1 = pdf_1.sum()
    pdf_norm_2 = pdf_2.sum()


    ax.plot(x, pdf_1, color=color)
    ax.plot(x, pdf_2, color=color2)

    plevelf_1 = lambda x, pdf_1, P: pdf_1[pdf_1 > x * pdf_norm_1].sum() - P * pdf_norm_1
    plevel_1 = scipy.optimize.brentq(plevelf_1, 0., 1., args=(pdf_1, 68.27 / 100.0 ))
    ax.fill_between(np.ma.masked_array(x, mask=pdf_1 < plevel_1 * pdf_norm_1),
                    np.ma.masked_array(pdf_1, mask=pdf_1 < plevel_1 * pdf_norm_1, fill_value=np.nan),
                    facecolor=color, alpha=0.4)

    plevelf_2 = lambda x, pdf_2, P: pdf_2[pdf_2 > x * pdf_norm_2].sum() - P * pdf_norm_2
    plevel_2 = scipy.optimize.brentq(plevelf_2, 0., 1., args=(pdf_2, 68.27 / 100.0 ))
    ax.fill_between(np.ma.masked_array(x, mask=pdf_2 < plevel_2 * pdf_norm_2),
                    np.ma.masked_array(pdf_2, mask=pdf_2 < plevel_2 * pdf_norm_2, fill_value=np.nan),
                    facecolor=color2, alpha=0.4)

    ax.set_xlim(left=xmin, right=xmax)
    ax.set_xbound(lower=xmin, upper=xmax)
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_tick_params(left=False)

    ax.vlines(SM_point[i], ax.get_ylim()[0], ax.get_ylim()[1], color="k")

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
        xsamples_1 = samples_1[:, j]
        ysamples_1 = samples_1[:, i]
        xsamples_2 = samples_2[:, j]
        ysamples_2 = samples_2[:, i]
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

        xysamples_1 = samples_1[:, (j, i)]
        kde_1 = gaussian_kde(np.transpose(xysamples_1), weights=weights_1)
        kde_1.set_bandwidth(bw_method='silverman')
        kde_1.set_bandwidth(bw_method=kde_1.factor * kde_smearing)

        xysamples_2 = samples_2[:, (j, i)]
        kde_2 = gaussian_kde(np.transpose(xysamples_2), weights=weights_2)
        kde_2.set_bandwidth(bw_method='silverman')
        kde_2.set_bandwidth(bw_method=kde_2.factor * kde_smearing)

        xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
        positions = np.vstack([xx.ravel(), yy.ravel()])
        pdf_1 = np.reshape(kde_1(positions).T, xx.shape)
        pdf_1 /= pdf_1.sum()
        pdf_2 = np.reshape(kde_2(positions).T, xx.shape)
        pdf_2 /= pdf_2.sum()

        # find the PDF value corresponding to a given cummulative probability
        plevel_1 = lambda x, pdf_1, P: pdf_1[pdf_1 > x].sum() - P
        plevels_1 = []
        labels_1 = []
        for level in [0, 68, 95, 99]:
            plevels_1.append(scipy.optimize.brentq(plevel_1, 0., 1., args=(pdf_1, level / 100.0)))
            labels_1.append('{}%'.format(level))

        plevel_2 = lambda x, pdf_2, P: pdf_2[pdf_2 > x].sum() - P
        plevels_2 = []
        labels_2 = []
        for level in [0, 68, 95, 99]:
            plevels_2.append(scipy.optimize.brentq(plevel_2, 0., 1., args=(pdf_2, level / 100.0)))
            labels_2.append('{}%'.format(level))


        colors = [matplotlib.colors.to_rgba(color, alpha) for alpha in np.linspace(0.20, 0.80, 4)]
        colors2 = [matplotlib.colors.to_rgba(color2, alpha) for alpha in np.linspace(0.20, 0.80, 4)]
        ax.contourf(pdf_1.transpose(),
                     colors=colors,
                     extent=[xmin, xmax, ymin, ymax],
                     levels=plevels_1[::-1])
        ax.contourf(pdf_2.transpose(),
                     colors=colors2,
                     extent=[xmin, xmax, ymin, ymax],
                     levels=plevels_2[::-1])

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
fig.savefig("figures/WET-3.pdf", bbox_inches='tight', dpi=300)
fig.savefig("figures/WET-3.png", bbox_inches='tight', dpi=300)