import eos
import numpy as _np
from eos.analysis_file_context import AnalysisFileContext
import tabulate


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

    labels = ['low-$q^2$',r'low-$\rho$',r'$\omega$',r'high-$\rho$',r'$\phi$','high-$q^2$',  r'low\,\&\,high-$q^2$', r'$\rho$','full $q^2$']
    exp = [r'$<0.93$',r'-', r'$7.3\pm2.9$','-',r'$30.2\pm4.5$',r'$<3.0$',r'$<2.9$',r'$6.9\pm2.0$','-']

    _data = {'BR':[], 'FL':[]}

    for obs in ['BR', 'FL']:
        item = { 'variable': 'q2', 'datafile': f'data/SM-fit/pred-{obs}_bin' }
        data = load_data(item['datafile'], item['variable'])
        _data[obs].extend(data)
    for obs in ['BR', 'FL']:
        item = { 'variable': 'q2_3', 'datafile': f'data/SM-fit/pred-{obs}_bin_combined' }
        data = load_data(item['datafile'], item['variable'])
        _data[obs].extend(data)
    for obs in ['BR', 'FL']:
        item = { 'variable': 'q2', 'datafile': f'data/SM-fit/pred-{obs}_full' }
        data = load_data(item['datafile'], item['variable'])
        _data[obs].extend(data)

    table = []
    headers = ['bin', r'$\langle\mathcal{B}\rangle_{\mathrm{exp.}}\:/\:10^{-8}$', r'$\langle\mathcal{B}\rangle_{\mathrm{SM,theo.}}\:/\:10^{-8}$',r'$\langle F_L\rangle_{\mathrm{SM,theo.}}$']

    for i in range(len(labels)):
        BR_central = _data['BR'][i][2]*1e8
        BR_error_low = (_data['BR'][i][2] - _data['BR'][i][1])*1e8
        BR_error_high = (_data['BR'][i][3] - _data['BR'][i][2])*1e8
        FL_central = _data['FL'][i][2]
        FL_error_low = (_data['FL'][i][2] - _data['FL'][i][1])
        FL_error_high = (_data['FL'][i][3] - _data['FL'][i][2])
        prec = {'BR':{},'FL':{}}
        prec['BR']['h'] = int(abs(int(_np.log10(BR_error_high)))+2) if _np.log10(BR_error_high) < 0 else int(abs(int(_np.log10(BR_error_high)))-1)
        prec['BR']['l'] = int(abs(int(_np.log10(BR_error_low)))+2) if _np.log10(BR_error_low) < 0 else int(abs(int(_np.log10(BR_error_low)))-1)
        prec['FL']['h'] = int(abs(int(_np.log10(FL_error_high)))+2)
        prec['FL']['l'] = int(abs(int(_np.log10(FL_error_low)))+2)

        for key in ['BR','FL']:
            if prec[key]['h'] < 0:
                prec[key]['h'] = 1
            if prec[key]['l'] < 0:
                prec[key]['l'] = 1
            prec[key]['c'] = max(prec[key]['h'],prec[key]['l'])

        row = [labels[i],
               exp[i],
               f'${BR_central:.{prec['BR']['c']}f}^{{+{BR_error_high:.{prec['BR']['h']}f}}}_{{-{BR_error_low:.{prec['BR']['l']}f}}}$',
               f'${FL_central:.{prec['FL']['c']}f}^{{+{FL_error_high:.{prec['FL']['h']}f}}}_{{-{FL_error_low:.{prec['FL']['l']}f}}}$']
        table.append(row)

    print(tabulate.tabulate(table, headers=headers, tablefmt='latex_raw'))
