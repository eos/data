import eos
import numpy as _np
from eos.analysis_file_context import AnalysisFileContext
import tabulate


def load_data(datafile):
    _datafile = eos.data.ImportanceSamples(datafile)

    _xvalues = _np.array([p['name'] for p in _datafile.varied_parameters])

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

    data = load_data('data/SM-fit/samples')

    table = []
    headers = ['parameter', r'lower', r'central value',r'upper','+','-']

    for entry in data:
        row = list(entry)
        row.append(entry[3]-entry[2])
        row.append(entry[1]-entry[2])
        table.append(row)

    print(tabulate.tabulate(table, headers=headers, tablefmt='latex_raw'))



    data = load_data('data/NP-fit-C7/samples')

    table = []
    headers = ['parameter', r'lower', r'central value',r'upper','+','-']

    for entry in data:
        row = list(entry)
        row.append(entry[3]-entry[2])
        row.append(entry[1]-entry[2])
        table.append(row)

    print(tabulate.tabulate(table, headers=headers, tablefmt='latex_raw'))

