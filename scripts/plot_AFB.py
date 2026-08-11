import eos
import numpy as np
import matplotlib.pyplot as plt

from eos.figure.item import *

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
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0.959, 1.122]   },
  'yaxis': {  'label': r'$\langle A_{\mathrm{FB}} \rangle_{\phi\mathrm{-region}}(q^2) \:/\:\mathrm{GeV}^{-2}$ ', 'range': [-0.55, 0.55] },
  'items':[]
  },{
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0.959, 1.122]   },
  'yaxis': { 'label': r'$\langle A_{\mathrm{FB}} \rangle$ ', 'range': [-0.22, 0.22]  },
  'items':
    []
  },],
  'shape': (1,2),
  'size' : (426.0*pt, 2.7),
  'padding' : (0.0,0.0),
}

colors = {'a': (0.247, 0.565, 0.855),
          'b': (1.000, 0.663, 0.055),
          'c': (0.741, 0.122, 0.004),
          'd': (0.580, 0.643, 0)}

items = []

alpha = 0.5

# NP contribution (uncertainty)

item = { 'type': 'uncertainty', 'interpolation' : 'cubic', 'band': ['area', 'median'], 'alpha' : alpha,
      'variable': 'q2', 'range': [0.959, 1.122], 'resolution': 1000, 'datafile': 'data/C10-unc/pred-AFB-q2',
      'label': r'$\mathcal{C}_{10} = 0.3$, $\delta_{\omega\mathrm{-}\rho} = \pi$', 'color': 'purple'}
items.append(item)

# NP contributions

standard_item = { 'type': 'uncertainty', 'interpolation' : 'cubic', 'band': ['area', 'median'], 'alpha' : alpha,
      'variable': 'q2', 'range': [0.959, 1.122], 'resolution': 1000, 'datafile': 'data/C10-unc/pred-AFB-q2',
      'label': r'$\mathcal{C}_{10} = 0.3$, $\delta_{\omega\mathrm{-}\rho} = \pi$'}

for val1,val2, name, style, id_p in [(0,0, r'0(0)','solid','a'),(np.pi,0,r'\pi(0)','dotted','b'),(0,np.pi,r'0(\pi)','dashed','c'),(0,np.pi/2,r'0(\pi/2)','dashdot','d')]:
    item = standard_item.copy()
    item['datafile'] = standard_item['datafile'].replace('unc',id_p)
    item['label'] = r'$\delta_{\rho(\phi\mathrm{-}\rho)} =' + name + r'$'
    item['linestyle'] = style
    item['color'] = colors[id_p]
    items.append(item)


figure_args_grid['plots'][0]['items'] = items

items = []


# NP contribution (uncertainty)

item = { 'type': 'uncertainty-binned', 'alpha' : alpha, 'band': ['area', 'median'],
      'variable': 'q2', 'range': [0.959, 1.122], 'datafile': 'data/C10-unc/pred-AFB-bin-c',
      'label': r'$\mathcal{C}_{10} = 0.3$, $\delta_{\omega\mathrm{-}\rho} = \pi$','color': 'purple'}
items.append(item)

# NP contributions

standard_item_binned = { 'type': 'uncertainty-binned', 'alpha' : alpha, 'band': ['area', 'median'],
      'variable': 'q2', 'range': [0.959, 1.122], 'datafile': 'data/C10-unc/pred-AFB-bin-c',
      'label': r'$\mathcal{C}_{10} = 0.3$, $\delta_{\omega\mathrm{-}\rho} = \pi$'}

for val1,val2, name, style, id_p in [(0,0, r'0(0)','solid','a'),(np.pi,0,r'\pi(0)','dotted','b'),(0,np.pi,r'0(\pi)','dashed','c'),(0,np.pi/2,r'0(\pi/2)','dashdot','d')]:
    item_bin = standard_item_binned.copy()
    item_bin['datafile'] = standard_item_binned['datafile'].replace('unc',id_p)
    item_bin['label'] = r'$\delta_{\rho(\phi\mathrm{-}\rho)} =' + name + r'$'
    item_bin['color'] = colors[id_p]
    item_bin['linestyle'] = style
    items.append(item_bin)

figure_args_grid['plots'][1]['items'] = items

figure = eos.figure.FigureFactory.from_dict(**figure_args_grid)
figure.draw(output='figures/thesis_AFB_general.pdf')

# Shrink current axis's height by 10% on the bottom
for ax in figure._figure.axes:
      box = ax.get_position()
      ax.set_position([box.x0, box.y0,
                       box.width, box.height * 0.87])


# Get handles and labels for legend

legend_entries = []
for item in figure.plots[0].items:
      legend_entries.extend(item.legend())

handles = [entry[0] for entry in legend_entries]
labels = [entry[1] for entry in legend_entries]

# add dummy line
l = plt.Line2D([0],[0],color="w")
handles.insert(1,l)
labels.insert(1,"")

leg = figure._figure.legend(handles, labels, loc='outside upper center', fontsize='small', ncol=3,frameon=False)
lhs = leg.legend_handles
lhs[0].set_alpha(0.6)
lhs[1].set_alpha(0.45)

plt.savefig('figures/thesis_AFB_general.pdf')
plt.savefig('figures/thesis_AFB_general.png', dpi=300)