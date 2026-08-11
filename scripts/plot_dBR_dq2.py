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
  'xaxis': { 'label': r'$q^2\:/\:\mathrm{GeV}^2$', 'range': [0.0446, 1.83]   },
  'yaxis': { 'label': r'$\mathrm{d}\mathcal{B}(\Lambda_c\to p \mu^+\mu^-)/\mathrm{d}q^2 \:/\:\mathrm{GeV}^{-2}$ ', 'range': [4e-11, 5e-5], 'scale': 'log'  },
  'items':
    []
  },
  'size' : (426.0*pt, 3.0),
  'watermark' : {'preliminary': False, 'position': 'lower left'},
}

items = []

# SM strong phases with uncertainties

item = { 'type': 'uncertainty', 'interpolation' : 'cubic', 'band': ['area', 'median'],
      'variable': 'q2', 'range': [0.0446, 1.83], 'resolution': 1000, 'datafile': 'data/SM-fit/pred-dBR-dq2-full', 'levels': [68.27,95.44997361036416,99.73002039367398],
      'label': r'resonant SM', 'color': 'orange'}
items.append(item)

# SM strong phases (without uncertainties)

standard_item = { 'type': 'observable', 'observable': r'Lambda_c->protonll::dBR/dq2', 'options': { 'l': 'mu', 'form-factors': 'BMRvD2022' },
      'variable': 'q2', 'range': [0.0446, 1.83], 'resolution': 1000, 'fixed_parameters_from_file': 'input/parameters_fixed.yaml',
      'color': 'black'}
p_standard = {"Lambda_c->proton::res_delta_rho@GHM2021": 0, r'ucmumu::Re{c10}': 0.0, r'ucmumu::Re{c9}': 0.0, r'uc::Re{c7}':0.0}

for val1,val2, name, style in [(np.pi,np.pi, r'\pi(\pi)','solid'),(0,0,r'0(0)','dotted'),(np.pi,0,r'\pi(0)','dashed'),(0,np.pi,r'0(\pi)','dashdot')]:
    item = standard_item.copy()
    p = p_standard.copy()
    p["Lambda_c->proton::res_delta_omega_m_rho@GHM2021"] = val1
    p["Lambda_c->proton::res_delta_phi_m_rho@GHM2021"] = val2
    item['fixed_parameters'] = p
    item['label'] = r'$\delta_{\omega(\phi)\mathrm{-}\rho} =' + name + r'$'
    item['linestyle'] = style
    items.append(item)

figure_args['plot']['items'] = items
figure = eos.figure.FigureFactory.from_dict(**figure_args)
figure.draw(output='figures/dBR_dq2.pdf')

legend_entries = []
for item in figure.plot.items:
      legend_entries.extend(item.legend())
handles = [entry[0] for entry in legend_entries]
labels = [entry[1] for entry in legend_entries]

leg = plt.legend(handles, labels, loc='upper right', fontsize='small',frameon=False)
plt.savefig('figures/dBR_dq2.pdf')
plt.savefig('figures/dBR_dq2.png', dpi=300)