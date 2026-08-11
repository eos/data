import eos
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams

parameters = eos.Parameters.Defaults()

rcParams.update({'font.size': 9})
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['axes.labelsize'] = 9
pt = 1./72.27

figure_args_grid = {'type':'grid',
  'plots': [
  {
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0.045, 1.817]   },
  'yaxis': { 'label': r'$\langle \mathcal{B} \rangle$ ', 'range': [7e-10, 1e-6], 'scale': 'log'  },
  'items':
    []
  },
  {
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0., 1.0]   },
  'yaxis': {  'label': r'', 'range': [7e-10, 1e-6], 'scale': 'log' },
  'items':[]
  },
  {
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0.045, 1.817]   },
  'yaxis': { 'label': r'$\langle F_{L} \rangle$ ', 'range': [0.35, .75]  },
  'items':
    []
  },
  {
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0., 1.0]   },
  'yaxis': { 'label': r'', 'range': [0.35, .75]  },
  'items':[]
  },],
  'shape': (2,2),
  'size' : (426.0*pt, 3.0),
  'padding' : (3.0,3.0),
  'watermark' : {'preliminary': False, 'position': 'lower left'},
  'watermark_plot':(1,0),
}


alpha = 0.6

items = []

colors = {'a': (0.247, 0.565, 0.855),
          'b': (1.000, 0.663, 0.055),
          'c': (0.741, 0.122, 0.004),
          'd': (0.580, 0.643, 0)}

# SM contribution

i = 0
for obs in ['BR', 'FL']:
  item = { 'type': 'uncertainty-binned','band': ['area', 'median'],
      'variable': 'q2', 'range': [0.045, 1.817], 'datafile': f'data/SM-fit/pred-{obs}_full',
      'label': 'resonant SM\nfull-$q^2$', 'color':'black','alpha': 0.3}
  figure_args_grid['plots'][i]['items'].append(item)
  item = { 'type': 'uncertainty-binned','band': ['area', 'median'],
      'variable': 'q2', 'range': [0.045, 1.817], 'datafile': f'data/SM-fit/pred-{obs}_bin',
      'label': 'resonant SM\nbinned', 'color':'orange','alpha': alpha}
  figure_args_grid['plots'][i]['items'].append(item)
  i+=2

i = 1
for obs in ['BR', 'FL']:
  item = { 'type': 'uncertainty-binned','band': ['area', 'median'],
      'variable': 'q2_3', 'range': [0.0, 1.0], 'datafile': f'data/SM-fit/pred-{obs}_bin_combined',
      'label': r'resonant', 'color':'orange','alpha': alpha}
  figure_args_grid['plots'][i]['items'].append(item)
  i+=2

figure = eos.figure.FigureFactory.from_dict(**figure_args_grid)
figure.draw(output=f'figures/SM_obs_binned.pdf')



axs = figure._figure.get_axes()

axs[1].text(0.25, 1.7e-9, r'low-$m$\,\&'+'\n'+r'high-$m$',ha='center',va='center')
axs[1].text(0.75, 1.7e-9, r'$\rho$',ha='center',va='center')
axs[3].text(0.25, 0.40, r'low-$m$\,\&'+'\n'+r'high-$m$',ha='center',va='center')
axs[3].text(0.75, 0.40, r'$\rho$',ha='center',va='center')
for ax in [axs[1], axs[3]]:
    ylims = ax.get_ylim()
    ax.vlines(0.5, *ylims,color='gray',linewidth=0.8)
    ax.set_ylim(ylims)
    ax.get_xaxis().set_visible(False)
    for ylabel_i in ax.get_yticklabels():
        ylabel_i.set_fontsize(0.0)
        ylabel_i.set_visible(False)

legend_entries = []
for item in figure.plots[0].items:
      legend_entries.extend(item.legend())
handles = [entry[0] for entry in legend_entries]
labels = [entry[1] for entry in legend_entries]

lg = axs[3].legend(handles, labels, loc='center left', fontsize='medium', bbox_to_anchor=(1.0, 1.0),frameon=False)
figure._gridspec.tight_layout(figure._figure,pad=0.1)
figure._gridspec.set_width_ratios([0.7, 0.3])
figure._gridspec.update(wspace=0.0, hspace=0.0)

plt.savefig('figures/SM_obs_binned.pdf')
plt.savefig('figures/SM_obs_binned.png', dpi=300)