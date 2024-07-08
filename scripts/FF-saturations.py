import eos
import matplotlib.pyplot as plt
import numpy as np

posteriors = [
    'TH-all', 'SM-all', 'CKM-all'
]
saturations = [
    '0mA', '0pV', '1pA-long', '1pA-perp', '1mV-long', '1mV-perp', '1mT-long', '1mT-perp', '1pT5-long', '1pT5-perp'
]
labels = [
    '$0^-$', '$0^+$', '$1^+$ (long)', '$1^+$ (perp)', '$1^-$ (long)', '$1^-$ (perp)', '$1^-$ (long, T)', '$1^-$ (perp, T)', '$1^+$ (long, T5)', '$1^+$ (perp, T5)'
]
samples = {}
weights = {}
xmax    = {
    '0mA': 1.3, '0pV': 1.3, '1pA-long':  1.3, '1pA-perp': 1.3, '1mV-long': 1.3, '1mV-perp': 1.3, '1mT-long': 1.3, '1mT-perp': 1.3, '1pT5-long': 1.3, '1pT5-perp': 1.3
}
ymax    = {
    '0mA': 5.0, '0pV': 3.0, '1pA-long': 16.0, '1pA-perp': 3.0, '1mV-long': 6.0, '1mV-perp': 6.0, '1mT-long': 4.0, '1mT-perp': 5.0, '1pT5-long': 5.0, '1pT5-perp': 5.0
}
# Read in data
for p in posteriors:
    for s in saturations:
        pred = eos.data.Prediction(f'data/{p}/pred-saturation-{s}')
        samples[(p, s)] = np.sum(pred.samples, axis=1)
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