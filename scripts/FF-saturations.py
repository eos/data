import eos
import matplotlib.pyplot as plt
import numpy as np

posteriors = [
    'TH-all', 'SM-all', 'CKM-all'
]
saturations = [
    '0mA', '0pV', '1pA', '1mV', '1mT', '1pT5'
]
labels = [
    '$0^-$', '$0^+$', '$1^+$', '$1^-$', '$1^-$ (T)', '$1^+$ (T5)'
]
samples = {}
weights = {}
xmax    = {
    '0mA': 1.3, '0pV': 1.3, '1pA':  1.3, '1mV':  1.3, '1mT': 1.3, '1pT5': 1.3
}
ymax    = {
    '0mA': 5.0, '0pV': 3.0, '1pA': 10.0, '1mV': 18.0, '1mT': 6.0, '1pT5': 7.0
}
norm    = {
    '0mA': 1.0, '0pV': 1.0, '1pA':  3.0, '1mV':  3.0, '1mT': 3.0, '1pT5': 3.0
}
# Read in data
for p in posteriors:
    for s in saturations:
        pred = eos.data.Prediction(f'data/{p}/pred-saturation-{s}')
        samples[(p, s)] = np.sum(pred.samples, axis=1) / norm[s]
        weights[(p, s)] = pred.weights

for s, l in zip(saturations, labels):
  plot_args = {
    'plot': {
      'x': {
        'label': fr'saturation {l}',
        'range': [ 0.00, xmax[s] ]
      },
      'y': {
        'range': [ 0.00, ymax[s] ]
      },
      'legend': {
        'location': 'upper center'
      }
    },
    'contents': [
      {
        'label': 'theory only',
        'type': 'kde',
        'color': 'C4',
        'data': { 'samples': samples[('TH-all', s)], 'weights': weights[('TH-all', s)] },
      },
      {
        'label': 'SM posterior',
        'type': 'kde',
        'color': 'C6',
        'data': { 'samples': samples[('SM-all', s)], 'weights': weights[('SM-all', s)] },
      },
      {
        'label': 'CKM posterior',
        'type': 'kde',
        'color': 'C9',
        'data': { 'samples': samples[('CKM-all', s)], 'weights': weights[('CKM-all', s)] },
      },
      {
        'label': 'bound',
        'type': 'band',
        'x': [ 1.00, xmax[s] ],
        'color': 'gray',
        'alpha': 0.5
      }
    ]
  }
  eos.plot.Plotter(plot_args, f'figures/FF-saturation-{s}.pdf').plot()
  eos.plot.Plotter(plot_args, f'figures/FF-saturation-{s}.png').plot()