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
  'yaxis': { 'label': r'$\langle F_{L} \rangle$ ', 'range': [0.15, .95]  },
  'items':
    []
  },
  {
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0., 1.5]   },
  'yaxis': { 'label': r'', 'range': [0.15, .95]  },
  'items':[]
  },],
  'shape': (1,2),
  'size' : (426.0*pt, 2.3 ),
  'padding' : (3.0,3.0),
  'watermark' : {'preliminary': False, 'position': 'upper left'},
  'watermark_plot':(0,0),
}


alpha = 0.6

items = []

colors = {'a': (0.247, 0.565, 0.855),
          'b': (1.000, 0.663, 0.055),
          'c': (0.741, 0.122, 0.004),
          'd': (0.580, 0.643, 0)}

obs = 'FL'

colors_bin = {'SM-fit': 'orange', 'NP-fit-C7': 'purple', 'NP-fit-C7p': 'green'}
colors_full = {'SM-fit': 'orange', 'NP-fit-C7': 'purple', 'NP-fit-C7p': 'green'}
labels = {'SM-fit': 'resonant SM', 'NP-fit-C7': r'SM + $\mathcal{C}_7=0.15$', 'NP-fit-C7p': r'SM + $\mathcal{C}_7^\prime=0.15$'}

for posterior in ['SM-fit','NP-fit-C7','NP-fit-C7p']:

    item = { 'type': 'uncertainty-binned','band': ['area', 'median'],
        'variable': 'q2_3', 'range': [0.0, 1.5], 'datafile': f'data/{posterior}/pred-{obs}_full_NP',
        'color':colors_full[posterior],'alpha': alpha}
    figure_args_grid['plots'][1]['items'].append(item)
    item = { 'type': 'uncertainty-binned','band': ['area', 'median'],
        'variable': 'q2', 'range': [0.045, 1.817], 'datafile': f'data/{posterior}/pred-{obs}_bin',
        'label': labels[posterior], 'color': colors_bin[posterior],'alpha': alpha}
    figure_args_grid['plots'][0]['items'].append(item)

    item = { 'type': 'uncertainty-binned','band': ['area', 'median'],
        'variable': 'q2_3', 'range': [0.0, 1.5], 'datafile': f'data/{posterior}/pred-{obs}_bin_combined',
        'color': colors_bin[posterior],'alpha': alpha}
    figure_args_grid['plots'][1]['items'].append(item)

figure = eos.figure.FigureFactory.from_dict(**figure_args_grid)
figure.draw(output=f'figures/NP_FL_binned.pdf')

axs = figure._figure.get_axes()

axs[1].text(0.25, 0.75, r'low-$m$\,\&'+'\n'+r'high-$m$',ha='center',va='center')
axs[1].text(0.75, 0.75, r'$\rho$',ha='center',va='center')
axs[1].text(1.25,  0.75, r'full',ha='center',va='center')
ax = axs[1]
ylims = ax.get_ylim()
ax.vlines(0.5, *ylims,color='gray',linewidth=0.8)
ax.vlines(1.0, *ylims,color='gray',linewidth=0.8)
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

lg = axs[1].legend(handles, labels, loc='center left', fontsize='medium', bbox_to_anchor=(1.0, 0.5),frameon=False)
figure._gridspec.tight_layout(figure._figure,pad=0.1)
figure._gridspec.set_width_ratios([0.6, 0.4])
#figure._gridspec.update(wspace=0.0, hspace=0.45)
figure._gridspec.update(wspace=0.0, hspace=0.0)

plt.savefig('figures/NP_FL_binned.pdf')
plt.savefig('figures/NP_FL_binned.png', dpi=300)