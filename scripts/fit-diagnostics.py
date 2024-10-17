import eos
import numpy as np
import yaml

def weighted_average(values, weights, axis=0):
    average = np.average(values, weights=weights, axis=axis)
    variance = np.average((values-average)**2, weights=weights, axis=axis)
    return np.array((average, np.sqrt(variance)))

for i in range(1,6):
    base_path = f"data/FF-fp-I1-order{i}"
    with open(f"{base_path}/mode-default/description.yaml") as f:
        mode_data = yaml.safe_load(f)

    param_data = eos.data.ImportanceSamples(f"{base_path}/samples")
    (mass_mean, width_mean), (mass_err, width_err) = weighted_average(1000*param_data.samples[:,(0,1)], param_data.weights)

    rpisq_data = eos.data.Prediction(f"{base_path}/pred-FF-fp-I1-pion-charge-radius-squared")
    rpisq_mean, rpisq_err = weighted_average(rpisq_data.samples, weights=rpisq_data.weights)[:,0]

    saturation_data = eos.data.Prediction(f"{base_path}/pred-FF-fp-I1-dispersive-bound")
    saturation_upper95 = np.quantile(saturation_data.samples[:,0], weights=saturation_data.weights, q=[0.95], method="inverted_cdf")[0]

    print(fr"{i} & ${mode_data['global_chi2']:.4g}$ & ${mode_data['dof']}$ & ${100*mode_data['pvalue']:.4g}$ & "
          fr"${rpisq_mean:.4g} \pm {rpisq_err:.4g}$ & ${mass_mean:.4g} \pm {mass_err:.4g}$ & ${width_mean:.4g} \pm {width_err:.4g}$ & "
          fr"${saturation_upper95:.4g}$ \\")
