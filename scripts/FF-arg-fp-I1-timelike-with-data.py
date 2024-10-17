import numpy as np
import eos

plot_args = {
    'plot': {
        'x': {'label': '$q^2$', 'unit': '$\\textnormal{GeV}^2$', 'range': [0.0, 2.0]},
        'y': {'label': '$\\mathrm{arg} F_\\pi(I=1)$', 'range': [0.0, 3.5]},
    },
    'contents': [
        {
            'type': 'uncertainty',
            'data-file': 'data/FF-fp-I1-order5/pred-FF-arg-fp-I1-timelike',
            'label': '$N=5$ fit', 'color': 'C4', 'opacity': 0.5,
            'band': ['outer', 'area'],
            'range': [0.0, 1.0]
        },
        {
            'type': 'uncertainty',
            'data-file': 'data/FF-fp-I1-order5/pred-FF-arg-fp-I1-timelike',
            'color': 'C4', 'opacity': 0.5,
            'style': 'dashed',
            'band': ['outer'],
            'range': [1.0, 2.0]
        },
        {
            'type': 'band',
            'color': 'gray', 'opacity': 0.25,
            'x': [1.0, 2.0], 'y': [0, 4.0]
        },
        {
            'type': 'watermark',
            'position': ['right', 'bottom']
        }
    ]
}
fig, ax = eos.plot.Plotter(plot_args).plot()

q2_over_mpisquared, phase, err = np.loadtxt("scripts/d11-central.txt", skiprows=1, unpack=True)
mpi = eos.Parameters()["mass::pi^+"].evaluate()
q2 = q2_over_mpisquared * mpi**2

ax.fill_between(q2, phase-err, phase+err, label="CHS 2018", alpha=0.5)
ax.legend(loc="upper left")

fig.savefig("figures/FF-arg-fp-I1-timelike-with-data.png")
fig.savefig("figures/FF-arg-fp-I1-timelike-with-data.pdf")
