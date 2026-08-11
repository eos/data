import eos
import numpy as np
import matplotlib.pyplot as plt

parameters = eos.Parameters.Defaults()

from matplotlib import rcParams

rcParams.update({'font.size': 9})
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9
rcParams['axes.labelsize'] = 9
pt = 1./72.27

figure_args = {'plot': {
  'legend': {'position': 'upper right'},
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0.04456, 1.83]   },
  'yaxis': { 'label': r'$F_{L}(q^2)$ ', 'range': [0,1] },
  'items':
    []
  },
  'size' : (426.0*pt, 3.0),
  'watermark' : {'preliminary': False, 'position': 'lower left'},
}

items = []


# NP contribution C7 = 0.15

item = { 'type': 'uncertainty', 'interpolation' : 'cubic', 'band': ['area', 'median'],
      'variable': 'q2', 'range': [0.04456, 1.83], 'resolution': 1000, 'datafile': 'data/NP-fit-C7/pred-FL-q2',
      'label': r'SM$\,+\,\mathcal{C}_{7} = 0.15$', 'color': 'purple'}
items.append(item)

# SM strong phases (without uncertainties)

standard_item = { 'type': 'observable', 'observable': r'Lambda_c->protonll::F_L(q2)', 'options': { 'l': 'mu', 'form-factors': 'BMRvD2022' },
      'variable': 'q2', 'range': [0.04456, 1.83], 'resolution': 1000, 'fixed_parameters_from_file': 'input/parameters_fixed.yaml',
      'color': 'black'}
p_standard = {"Lambda_c->proton::res_delta_rho@GHM2021": 0 , r'ucmumu::Re{c10}': 0.0, r'ucmumu::Re{c9}': 0.0, r'uc::Re{c7}': -346.8401235494036, r'uc::Im{c7}' : -919.8543681799476}

for val1,val2, name, style in [(np.pi,np.pi, r'\pi(\pi)','solid'),(0,0,r'0(0)','dotted'),(np.pi,0,r'\pi(0)','dashed'),(0,np.pi,r'0(\pi)','dashdot')]:
    item = standard_item.copy()
    p = p_standard.copy()
    p["Lambda_c->proton::res_delta_omega_m_rho@GHM2021"] = val1
    p["Lambda_c->proton::res_delta_phi_m_rho@GHM2021"] = val2
    item['fixed_parameters'] = p
    item['label'] = r'$\delta_{\omega(\phi)-\rho} =' + name + r'$'
    item['linestyle'] = style
    items.append(item)

# NP contribution C7p = 0.15

item = { 'type': 'uncertainty', 'interpolation' : 'cubic', 'band': ['area', 'median'],
     'variable': 'q2', 'range': [0.04456, 1.83], 'resolution': 1000, 'datafile': 'data/NP-fit-C7p/pred-FL-q2',
     'label': r'SM$\,+\,\mathcal{C}_{7}^\prime = 0.15$', 'color': 'green'}
items.append(item)

# SM strong phases with uncertainties

item = { 'type': 'uncertainty', 'interpolation' : 'cubic', 'band': ['area', 'median'],
      'variable': 'q2', 'range': [0.04456, 1.83], 'resolution': 1000, 'datafile': 'data/SM-fit/pred-FL-q2',
      'label': r'resonant SM', 'color': 'orange'}
items.append(item)




figure_args['plot']['items'] = items
figure = eos.figure.FigureFactory.from_dict(**figure_args)
figure.draw(output='figures/NP_FL_q2.pdf')

legend_entries = []
for item in figure.plot.items:
      legend_entries.extend(item.legend())
handles = [entry[0] for entry in legend_entries]
labels = [entry[1] for entry in legend_entries]

leg = plt.legend(handles, labels, loc='upper right', fontsize='small',frameon=False)
leg.legend_handles[0].set_alpha(0.6)
plt.savefig('figures/NP_FL_q2.pdf')
plt.savefig('figures/NP_FL_q2.png', dpi=300)