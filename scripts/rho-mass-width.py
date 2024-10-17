import eos

data3 = eos.data.ImportanceSamples("data/FF-fp-I1-order3/samples")
data4 = eos.data.ImportanceSamples("data/FF-fp-I1-order4/samples")
data5 = eos.data.ImportanceSamples("data/FF-fp-I1-order5/samples")

plot_args = {
    'plot': {
        'x': {'label': r'$M_\rho$', 'unit': 'MeV', 'range': [758, 765.2]},
        'y': {'label': r'$\Gamma_\rho$', 'unit': 'MeV', 'range': [141, 151]},
        'legend': {'location': 'upper right', 'columns': 2},
    },
    'contents': [
        {
            'type': 'kde2D', 'color': 'C4', 'label': 'N=5',
            'levels': [68, 95], 'contours': ['lines','areas'], 'bandwidth':3,
            'data': { 'samples': 1000*data5.samples[:, (0,1)], 'weights': data5.weights }
        },
        {
            'type': 'errorbar', 'color': 'black', 'label': 'PDG T-Matrix Pole',
            'x': 763, 'y': 145, 'xerr': 2, 'yerr': 3
        },
        {
            'type': 'kde2D', 'color': 'C5', 'label': 'N=4',
            'levels': [68, 95], 'contours': ['lines','areas'], 'bandwidth':3,
            'data': { 'samples': 1000*data4.samples[:, (0,1)], 'weights': data4.weights }
        },
        {
            'type': 'kde2D', 'color': 'C6', 'label': 'N=3',
            'levels': [68, 95], 'contours': ['lines','areas'], 'bandwidth':3,
            'data': { 'samples': 1000*data3.samples[:, (0,1)], 'weights': data3.weights }
        },
        {
            'type': 'watermark',
            'position': ['right', 'bottom']
        }
    ]
}
fig, _ = eos.plot.Plotter(plot_args).plot()
fig.savefig("figures/rho-mass-width.pdf")
fig.savefig("figures/rho-mass-width.png")
