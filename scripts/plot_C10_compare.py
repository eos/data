import eos
import numpy as _np
import scipy as _scipy
import matplotlib.pyplot as plt
import os
from matplotlib import rcParams
from eos.analysis_file_context import AnalysisFileContext
parameters = eos.Parameters.Defaults()
import matplotlib as _matplotlib
from matplotlib import rcParams

rcParams.update({'font.size': 9})
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['axes.labelsize'] = 9
pt = 1./72.27

from eos.figure.item import TwoDimensionalHistogramItem, TwoDimensionalKernelDensityEstimateItem

lambda_CKM = -5.383319178425827e-05 + 1.427709577227314e-04j

class ModifiedTwoDimensionalHistogramItem(TwoDimensionalHistogramItem):
    def draw(self, ax):
        """Draw the two-dimensional histogram on the provided axes.

        :param ax: The matplotlib axes onto which the histogram is drawn.
        :type ax: matplotlib.axes.Axes
        """
        ax.hist2d(_np.real((self.samples[:, 0]+1j*self.samples[:, 1])*lambda_CKM), _np.imag((self.samples[:, 0]+1j*self.samples[:, 1])*lambda_CKM), weights=self.weights, range=[self.xrange, self.yrange],
                  bins=self.bins, label=self.label, rasterized=True, cmap='Greys')

class ModifiedTwoDimensionalKernelDensityEstimateItem(TwoDimensionalKernelDensityEstimateItem):
    def prepare(self, context:AnalysisFileContext=None):
        """Prepare the two-dimensional kernel density estimate for drawing.

        Loads the data file, extracts the samples of the two chosen ``variables``, fits a Gaussian KDE
        (optionally rescaling the automatically determined bandwidth), and evaluates the resulting
        probability density on a regular grid spanning the x- and y-ranges for :meth:`draw`.

        :param context: The analysis file context used to resolve the relative path to ``datafile``.
            If ``None``, a default context rooted at the current working directory is used.
        :type context: AnalysisFileContext | None
        """

        context = AnalysisFileContext() if context is None else context

        # These checks are necessary to ensure that the data file is in the correct format,
        # but they are not possible in the __post_init__ method, because the data file might not yet exist.
        datafile = context.data_path(self.datafile)
        os.path.exists(datafile) or eos.error(f"Data file '{datafile}' does not exist when preparing 2D KDE")
        name = os.path.split(datafile)[-1]
        if name == 'samples':
            self._datafile = eos.data.ImportanceSamples(datafile)

            if self.variables[0] not in self._datafile.lookup_table:
                raise ValueError(f"Data file '{datafile}' does not contain samples of variable '{self.variables[0]}'")
            if self.variables[1] not in self._datafile.lookup_table:
                raise ValueError(f"Data file '{datafile}' does not contain samples of variable '{self.variables[1]}'")

            self._xidx = self._datafile.lookup_table[self.variables[0]]
            self._yidx = self._datafile.lookup_table[self.variables[1]]
        elif name.startswith('pred-'):
            self._datafile = eos.data.Prediction(datafile)

            stripped_lookup_table = { k.split(';')[0]: v for k, v in self._datafile.lookup_table.items() }

            if self.variables[0] in stripped_lookup_table:
                if len(stripped_lookup_table.keys()) != len(self._datafile.lookup_table.keys()):
                    # variable name matches when stripping potential kinematic info from prediction variable names
                    raise ValueError(f"Data file '{datafile}' contains multiple predictions for variable '{self.variables[0]}'; specify the full variable name including options and kinematics")
                self._xidx = stripped_lookup_table[self.variables[0]]
            else:
                if self.variables[0] not in self._datafile.lookup_table:
                    raise ValueError(f"Data file '{datafile}' does not contain predictions for variable '{self.variables[0]}'")
                self._xidx = self._datafile.lookup_table[self.variables[0]]

            if self.variables[1] in stripped_lookup_table:
                if len(stripped_lookup_table.keys()) != len(self._datafile.lookup_table.keys()):
                    # variable name matches when stripping potential kinematic info from prediction variable names
                    raise ValueError(f"Data file '{datafile}' contains multiple predictions for variable '{self.variables[1]}'; specify the full variable name including options and kinematics")
                self._yidx = stripped_lookup_table[self.variables[1]]
            else:
                if self.variables[1] not in self._datafile.lookup_table:
                    raise ValueError(f"Data file '{datafile}' does not contain predictions for variable '{self.variables[1]}'")
                self._yidx = self._datafile.lookup_table[self.variables[1]]
        else:
            eos.error(f"Data file '{datafile}' has an unsupported format")
            raise NotImplementedError

        samples_ = self._datafile.samples[:, (self._xidx, self._yidx)]
        samples = samples_.copy()
        samples[:,0] = _np.real((samples_[:, 0]+1j*samples_[:, 1])*lambda_CKM)
        samples[:,1] = _np.imag((samples_[:, 0]+1j*samples_[:, 1])*lambda_CKM)
        weights = self._datafile.weights

        eos.inprogress(f"Computing KDE for samples of variables '{self.variables[0]}' and '{self.variables[1]}'")
        self._kde = _scipy.stats.gaussian_kde(samples.T, weights=weights)
        self._kde.set_bandwidth(bw_method='silverman')
        if self.bandwidth is not None:
            self._kde.set_bandwidth(bw_method=self._kde.factor * self.bandwidth)

        # determine the extent of the plot
        if self.xrange is None:
            self.xrange = (samples[:, 0].min(), samples[:, 0].max())
        if self.yrange is None:
            self.yrange = (samples[:, 1].min(), samples[:, 1].max())

        # compute the PDF on a grid
        xx,yy = _np.mgrid[self.xrange[0]:self.xrange[1]:100j, self.yrange[0]:self.yrange[1]:100j]
        self._positions = _np.vstack([xx.ravel(), yy.ravel()])
        self._pdf = _np.reshape(self._kde(self._positions).T, xx.shape)
        self._pdf /= self._pdf.sum()

    def draw(self, ax):
        """Draw the two-dimensional kernel density estimate on the provided axes.

        Draws contour lines at the requested credibility ``levels`` and, depending on the
        ``contours`` setting, optionally fills the contour areas and/or labels the contour lines.

        :param ax: The matplotlib axes onto which the KDE is drawn.
        :type ax: matplotlib.axes.Axes
        """
        plevels = self._plevels()
        labels = [f'{level}%' for level in self.levels]

        if 'areas' in self.contours:
            colors = [_matplotlib.colors.to_rgba(self.color, alpha) for alpha in _np.linspace(0.50, 1.00, len(self.levels))]
            ax.contourf(self._pdf.transpose(),
                        colors=colors,
                        extent=[self.xrange[0], self.xrange[1], self.yrange[0], self.yrange[1]],
                        levels=plevels[::-1])

        CS = ax.contour(self._pdf.transpose(),
                        colors=self.color,
                        extent=[self.xrange[0], self.xrange[1], self.yrange[0], self.yrange[1]],
                        levels=plevels[::-1],
                        linestyles=self.linestyle)

        if 'labels' in self.contours:
            fmt = {}
            for level, label in zip(CS.levels, labels[::-1]):
                fmt[level] = label

            ax.clabel(CS, inline=1, fmt=fmt, fontsize=10)

items_kde = []
items_hist = []

for id,color in [('-AFB','orange'),('-AFB-fixed-rel-phases-v1','green'),('-AFB-fixed-phases-v1','blue'),
                 ('-future-AFB','orange'),('-future-AFB-fixed-rel-phases-v1','green'),('-future-AFB-fixed-phases-v1','blue')]:

    variables = [r'ucmumu::Re{c10}',r'ucmumu::Im{c10}',r"ucmumu::Re{c10'}",r"ucmumu::Im{c10'}"]
    content = eos.figure.data.DataFile.from_dict(**{'path': f'data/NP-fit-C10-C10p{id}/samples','label': r'label', 'color': color, 'kde': False})
    context = AnalysisFileContext()
    content.prepare(context=context)

    labels = content.labels(variables)

    x_range = [-8.0, 8.0]
    y_range = [-8.0, 8.0]
    x_range_ = [-3.0, 3.0]
    y_range_ = [-3.0, 3.0]

    if 'future' in id:
        linestyle = 'dashed'
    else:
        linestyle = 'solid'

    kde2D_item = {
                          'type': 'kde2D', 'label': content.label,
                          'datafile': context.data_path(content.path),
                          'variables': [variables[0], variables[1]],
                          'color': content.color,
                          'alpha' : 0.4,
                          'contours': ['lines','areas'],
                          'levels': [95],
                          'xrange': x_range,
                          'linestyle': linestyle,
                          'yrange': y_range
    }

    histo2D_item = {
                          'type': 'histogram2D', 'label': content.label,
                          'datafile': context.data_path(content.path),
                          'variables': [variables[0], variables[1]],
                          'color': content.color,
                          'xrange': x_range,
                          'yrange': y_range
    }

    items_hist.append(histo2D_item)
    items_kde.append(kde2D_item)

histo2D_item_ = histo2D_item.copy()
histo2D_item_.pop('type')
kde2D_item_ = kde2D_item.copy()
kde2D_item_.pop('type')

figure_args = {'plot': {
  'legend': {'position': 'upper right'},
  'xaxis': { 'label': labels[0], 'range': x_range_   },
  'yaxis': { 'label': labels[1], 'range': y_range_   },
  'aspect': 1,
  'items':
    []
  },
  'size' : (426.0*pt, 3.0),
  'watermark' : {'preliminary': False, 'position': 'lower left'},
}

figure_args['plot']['items'] = items_kde
figure = eos.figure.FigureFactory.from_dict(**figure_args)

items_hist_ = []
for item in items_hist:
    item_ = item.copy()
    item_.pop('type')
    items_hist_.append(ModifiedTwoDimensionalHistogramItem.from_dict(**item_))
figure.plot.items = items_hist_

items_kde_ = []
for item in items_kde:
    item_ = item.copy()
    item_.pop('type')
    items_kde_.append(ModifiedTwoDimensionalKernelDensityEstimateItem.from_dict(**item_))
figure.plot.items = items_kde_

figure.draw(output='figures/C10-AFB-compare.pdf')

colors = [[_matplotlib.colors.to_rgba(item.color, alpha) for alpha in _np.linspace(0.50, 1.00, len(item.levels))][0] for item in items_kde_]

labels = [r'best-fit to $\langle A_{\mathrm{FB}}\rangle$',
          r'using BM1 for phases',#r'$\langle A_{\mathrm{FB}}\rangle$'+'\n(fixed phases BM1'+r'$^\ast$)',
          r'using BM2 for phases',#r'$\langle A_{\mathrm{FB}}\rangle$'+'\n(fixed phases BM1)'
        ]
legend_entries = []
for item in figure.plot.items:
      legend_entries.extend(item.legend())
handles = [entry[0] for entry in legend_entries]
handles = handles[:3]

handles.append(_matplotlib.lines.Line2D([0], [0], color='black', lw=1, ls='solid'))
handles.append(_matplotlib.lines.Line2D([0], [0], color='black', lw=1, ls='dashed'))
labels.append('present data')
labels.append(r'$\frac{1}{5}$ stat. unc.')

leg = plt.legend(handles, labels, loc='center left', fontsize='smaller',frameon=False, bbox_to_anchor=(1.0, 0.5))
#leg.legend_handles[0].set_alpha(0.6)
plt.tight_layout(pad=0.2)
plt.savefig('figures/C10-AFB-compare.pdf')
plt.savefig('figures/C10-AFB-compare.png', dpi=300)


