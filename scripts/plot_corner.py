import eos
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
from eos.analysis_file_context import AnalysisFileContext

parameters = eos.Parameters.Defaults()

rcParams.update({'font.size': 7})
rcParams['xtick.labelsize'] = 7
rcParams['ytick.labelsize'] = 7
rcParams['axes.labelsize'] = 7
pt = 1./72.27

variables = ['Lambda_c->proton::res_a_phi@GHM2021','Lambda_c->proton::res_a_rho@GHM2021','Lambda_c->proton::res_a_omega@GHM2021','Lambda_c->proton::res_delta_phi_m_rho@GHM2021','Lambda_c->proton::res_delta_omega_m_rho@GHM2021']
content = eos.figure.data.DataFile.from_dict(**{'path': 'data/SM-fit/samples','label': r'label', 'color': 'red', 'kde': False})
context = AnalysisFileContext()
content.prepare(context=context)

size = len(variables)

figure_args_grid = {'type':'grid',
  'plots': [],
  'shape': (int(size),int(size)),
  'size' : (426.0*pt, 426.0*pt),
  'padding' : (0.0,0.0),
  'watermark' : {'preliminary': False, 'position': 'lower left'},
  'watermark_plot':(4,4),
}

# determine useful ranges empirically
absmin, absmax = np.array([+np.inf] * len(variables)), np.array([-np.inf] * len(variables))

indices = [content._datafile.lookup_table[v] for v in variables]
cmin, cmax = content.empirical_range
for idx, cidx in enumerate(indices):
    absmin[idx] = cmin[cidx] if cmin[cidx] < absmin[idx] else absmin[idx]
    absmax[idx] = cmax[cidx] if cmax[cidx] > absmax[idx] else absmax[idx]

    if absmin[idx] < 0:
      absmin[idx] = 0
    if absmax[idx] > 2*np.pi and 'delta' in variables[idx]:
      absmax[idx] = 2*np.pi
    # Check that the variables of the data files match
    unknown_variables = set(variables) - set(content.variables)
    if len(unknown_variables) > 0:
      raise ValueError(f"Unknown variables requested from data file '{content.path}': {list(unknown_variables)}")

#labels = content.labels(variables)
labels = ['$a_{\\phi}^{\\Lambda_c\\to p \\ell\\ell}$',
          '$a_{\\rho}^{\\Lambda_c\\to p \\ell\\ell}$',
          '$a_{\\omega}^{\\Lambda_c\\to p \\ell\\ell}$',
          '$\\delta_{\\phi\\mathrm{-}\\rho}^{\\Lambda_c\\to p \\ell\\ell}$',
          '$\\delta_{\\omega\\mathrm{-}\\rho}^{\\Lambda_c\\to p \\ell\\ell}$']

for i in range(size):     # rows
  for j in range(size): # columns

      if i < j:
          figure_args_grid['plots'].append({
              'type': 'empty'
          })

      elif i == j:
          figure_args_grid['plots'].append({
              'xaxis': {
                  'ticks': { 'visible': True, 'position': 'both' },
                  'label': labels[j],
                  'range': [ absmin[j], absmax[j] ]
              }
              if (i == size - 1) else
              {
                  'ticks': { 'visible': True, 'position': 'top' },
                  'range': [ absmin[j], absmax[j] ]
              },
              'yaxis': {
                  'ticks': { 'visible': False },
                  # 1D marginals, no label, no range
              },
              'grid': { 'visible': True, 'axis': 'x' },
              'items': [
                  {
                      'type': 'kde1D', 'label': content.label,
                      'datafile': context.data_path(content.path),
                      'variable': variables[j],
                      'color': content.color,
                      'range': [absmin[j], absmax[j]]
                  } if content.kde else {
                      'type': 'histogram1D', 'label': content.label,
                      'datafile': context.data_path(content.path),
                      'variable': variables[j],
                      'color': content.color,
                      'range': [absmin[j], absmax[j]]
                  }
              ]
          })

      else:
          figure_args_grid['plots'].append({
              'xaxis': {
                  'ticks': { 'visible': True, 'position': 'bottom' },
                  'label': labels[j],
                  'range': [ absmin[j], absmax[j] ]
              }
              if (i == size - 1) else
              {
                  'ticks': { 'visible': False, 'position': 'both' },
                  'range': [ absmin[j], absmax[j] ]
              },
              'yaxis': {
                  'ticks': { 'visible': True },
                  'label': labels[i],
                  'range': [ absmin[i], absmax[i] ]
              }
              if (j == 0) else
              {
                  'ticks': { 'visible': False },
                  'range': [ absmin[i], absmax[i] ]
              },
              'grid': { 'visible': True},
              'items': [
                  {
                      'type': 'histogram2D', 'label': content.label,
                      'datafile': context.data_path(content.path),
                      'variables': [variables[j], variables[i]],
                      'color': content.color,
                      'xrange': [absmin[j], absmax[j]],
                      'yrange': [absmin[i], absmax[i]]
                  },
                  {
                      'type': 'kde2D', 'label': content.label,
                      'datafile': context.data_path(content.path),
                      'variables': [variables[j], variables[i]],
                      'color': content.color,
                      'alpha' : 0.4,
                      'contours': ['lines', 'areas'],
                      'xrange': [absmin[j], absmax[j]],
                      'yrange': [absmin[i], absmax[i]]
                  }
                  ]
          })

figure = eos.figure.FigureFactory.from_dict(**figure_args_grid)
figure.draw(output='figures/corner_plot.pdf')
plt.savefig('figures/corner_plot.png', dpi=1000)