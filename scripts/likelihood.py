import eos
import matplotlib
import scipy
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import gaussian_kde
from scipy.stats import norm
from scipy.stats import multivariate_normal
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.legend_handler import HandlerTuple

posterior = "no-fsfd"

# Number of parameters that we want to plot
nParams = 3

samples = np.load("data/"+posterior+"/samples/samples.npy")[:, [0, 2, -1]]
weights = np.load("data/"+posterior+"/samples/weights.npy")

analysis = eos.AnalysisFile('likelihood.yaml').analysis(posterior)

# Compute gaussian approximation parameters
mean_BR = np.average(samples, weights = weights, axis = 0)
var_BR  = np.average((samples - mean_BR)**2, weights = weights, axis = 0)
covariance_BRs  = np.average(np.array([np.outer(s-mean_BR[0:nParams], s-mean_BR[0:nParams]) for s in samples]), weights = weights, axis = 0)

# Read the bounds from the analysis
params_all = analysis.varied_parameters
params = [params_all[0], params_all[2], params_all[-1]]
bounds = [(samples[:,i].min(), samples[:,i].max()) for i in range(nParams)]
# Main color
color  = "C0"
# Multiplication factor for the KDE estimate
kde_smearing = 1.0

# Show datapoints?
points = True
fig, axes = plt.subplots(nParams, nParams, figsize=(3.0 * nParams, 3.0 * nParams), dpi=100)

legended_plot = axes[2, 0]

for i in range(nParams):
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
    # plot gaussian approximation
    ax.plot(x, norm.pdf(x, mean_BR[i], np.sqrt(var_BR[i])), color = "C1")

    plevelf = lambda x, pdf_1, P: pdf_1[pdf_1 > x * pdf_norm].sum() - P * pdf_norm
    plevel = scipy.optimize.brentq(plevelf, 0., 1., args=(pdf, 68.27 / 100.0 ))
    ax.fill_between(np.ma.masked_array(x, mask=pdf < plevel * pdf_norm),
                    np.ma.masked_array(pdf, mask=pdf < plevel * pdf_norm, fill_value=np.nan),
                    facecolor=color, alpha=0.4)

    ax.set_xlim(left=xmin, right=xmax)
    ax.set_xbound(lower=xmin, upper=xmax)
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_tick_params(left=False)

    if i == nParams - 1:
        ax.set_xlabel(params[i].latex())
    else:
        ax.xaxis.set_major_formatter(plt.NullFormatter())
        ax.xaxis.set_tick_params(bottom=False)

    for j in range(0, nParams):
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
        kde.set_bandwidth(bw_method=kde.factor * kde_smearing)

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

        # plot 2d guassian approximation
        mean = mean_BR[[j, i]]
        cov  = covariance_BRs[[j, i]][:, [j, i]]
        rv = multivariate_normal(mean, cov)

        # Create a grid of (x, y) coordinates
        positions = np.dstack((xx, yy))

        # Compute the probability density function (PDF) on the grid
        pdf_gauss = rv.pdf(positions)
        pdf_gauss /= pdf_gauss.sum()

        # Find the contour levels for 68%, 95%, and 99% confidence intervals
        confidence_levels = [0.00, 0.68, 0.95, 0.99]
        contour_levels = []

        # Define the function to calculate the cumulative probability level
        plevel = lambda x, pdf, P: pdf[pdf > x].sum() - P

        # Total probability (since the PDF values are on a grid, sum them)
        for cl in confidence_levels:
            # Find the threshold for the given confidence level
            level = scipy.optimize.brentq(plevel, 0., pdf_gauss.max(), args=(pdf_gauss, cl))
            contour_levels.append(level)

        # Plot the contours of the 2D Gaussian with confidence intervals
        colors_gauss = [matplotlib.colors.to_rgba("C1", alpha) for alpha in np.linspace(0.20, 0.80, 4)]
        ax.contourf(pdf_gauss.transpose(),
                     colors=colors_gauss,
                     extent=[xmin, xmax, ymin, ymax],
                     levels=contour_levels[::-1])

        ax.grid(visible=True, alpha=0.25)

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

        if i == nParams - 1:
            ax.set_xlabel(params[j].latex())
        else:
            ax.xaxis.set_major_formatter(plt.NullFormatter())
            ax.xaxis.set_tick_params(bottom=False)

# Watermark
xdelta, ydelta = (0.05, 0.04)

ax = axes[nParams - 1, 0]
version = 'v{version}'.format(version=eos.__version__)
ax.text(xdelta, ydelta, r'\textsf{{\textbf{{EOS {version}}}}}'.format(version=version),
        transform=ax.transAxes,
        color='OrangeRed', alpha=0.5, bbox=dict(facecolor='white', alpha=0.5, lw=0),
        horizontalalignment='left', verticalalignment='bottom', zorder=+5)

# Caption
rec = plt.Rectangle((0,0),1,1, color=color,  alpha=0.8)
rec_gauss = plt.Rectangle((0,0),1,1, color="C1",  alpha=0.8)

legended_plot.legend(handles=[rec, rec_gauss], labels = ["full", "approx."],
                     loc='upper right', handler_map={tuple: HandlerTuple(ndivide=None)})

fig.tight_layout()
fig.savefig("figures/likelihood.pdf", bbox_inches='tight', dpi=300)
fig.savefig("figures/likelihood.png", bbox_inches='tight', dpi=300)
