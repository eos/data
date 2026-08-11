import eos
import numpy as _np
from eos.analysis_file_context import AnalysisFileContext
import tabulate
import numpy as np

def load_data(datafile,variable):
    context = AnalysisFileContext()

    _datafile = eos.data.Prediction(context.data_path(datafile))
    try:
        _xvalues = _np.array([(p['kinematics'][variable + '_min'], p['kinematics'][variable + '_max']) for p in _datafile.varied_parameters])
    except KeyError as e:
        raise RuntimeError(f'both \'{variable}_min\' and \'{variable}_max\' must be present in the kinematics of each prediction in the data file') from e

    ovalues_lower   = []
    ovalues_central = []
    ovalues_higher  = []
    for i in range(len(_xvalues)):
        lower, central, higher = _np.quantile(_datafile.samples[:, i], [0.15865, 0.5, 0.84135], weights=_datafile.weights, method='inverted_cdf')
        ovalues_lower.append(lower)
        ovalues_central.append(central)
        ovalues_higher.append(higher)

    return list(zip(_xvalues, ovalues_lower, ovalues_central, ovalues_higher))


if __name__ == '__main__':

    labels = [r'optimized low $\omega/\rho$',r'low $\omega/\rho$',r'high $\omega/\rho$'
              ,r'$\rho$ part $2$',r'$\phi$', r'low $\phi$', r'high $\phi$', r'optimized high $\phi$', r'$\sqrt{q^2} > 1.25\,\mathrm{GeV}$']


    obs = 'BR_AFB'
    item = { 'variable': 'q2', 'datafile': f'data/C10-unc/pred-{obs}_bins' }
    data = load_data(item['datafile'], item['variable'])

    table = []
    headers = ['bin', r'$\langle\mathcal{B}\rangle\:/\:10^{-8}$',
               r'$\langle A_{\mathrm{FB}}^\ell \rangle$']

    data_len = int(len(data)/2)
    for i in range(data_len):
        BR_central = data[i][2]*1e8
        BR_error_low = (data[i][2] - data[i][1])*1e8
        BR_error_high = (data[i][3] - data[i][2])*1e8
        AFB_central = data[i+data_len][2] * 100
        AFB_error_low = (data[i+data_len][2] - data[i+data_len][1]) * 100
        AFB_error_high = (data[i+data_len][3] - data[i+data_len][2]) * 100
        if np.isnan(AFB_central):
            continue
        prec = {'BR':{},'AFB':{}}
        prec['BR']['h'] = int(abs(int(_np.log10(BR_error_high)))+2) if _np.log10(BR_error_high) < 0 else int(abs(int(_np.log10(BR_error_high)))-1)
        prec['BR']['l'] = int(abs(int(_np.log10(BR_error_low)))+2) if _np.log10(BR_error_low) < 0 else int(abs(int(_np.log10(BR_error_low)))-1)
        prec['AFB']['h'] = int(abs(int(_np.log10(AFB_error_high)))+2)
        prec['AFB']['l'] = int(abs(int(_np.log10(AFB_error_low)))+2)

        for key in ['BR','AFB']:
            if prec[key]['h'] < 0:
                prec[key]['h'] = 1
            if prec[key]['l'] < 0:
                prec[key]['l'] = 1
            prec[key]['c'] = max(prec[key]['h'],prec[key]['l'])

        row = [labels[i],
               f'${BR_central:.{prec['BR']['c']}f}^{{+{BR_error_high:.{prec['BR']['h']}f}}}_{{-{BR_error_low:.{prec['BR']['l']}f}}}$',
               f'${AFB_central:.{prec['AFB']['c']}f}^{{+{AFB_error_high:.{prec['AFB']['h']}f}}}_{{-{AFB_error_low:.{prec['AFB']['l']}f}}}$']
        table.append(row)

    print(tabulate.tabulate(table, headers=headers, tablefmt='latex_raw'))
