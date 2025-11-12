import eos

BASE_DIRECTORY='./data/'
af = eos.AnalysisFile('./analysis.yaml')


#### Nested Sampling

print('HQE210red-q-LQCD+UB+SU3')
eos.sample_nested(af, 'HQE210red-q-LQCD+UB+SU3',  base_directory=BASE_DIRECTORY, nlive=500, dlogz=0.5)

print('HQE321red-q-LQCD+UB+SU3')
eos.sample_nested(af, 'HQE321red-q-LQCD+UB+SU3',  base_directory=BASE_DIRECTORY, nlive=500, dlogz=0.5)

print('HQE210red-q-LQCD+UB')
eos.sample_nested(af, 'HQE210red-q-LQCD+UB',  base_directory=BASE_DIRECTORY, nlive=500, dlogz=0.5)

print('HQE321red-q-LQCD+UB')
eos.sample_nested(af, 'HQE321red-q-LQCD+UB',  base_directory=BASE_DIRECTORY, nlive=1000, dlogz=0.5)

print('HQE321-q-LQCD+UB+SR')
eos.sample_nested(af, 'HQE321-q-LQCD+UB+SR',  base_directory=BASE_DIRECTORY, nlive=500, dlogz=0.5)


#### Predictions

if True:
    posteriors = ['HQE210red-q-LQCD+UB+SU3','HQE321red-q-LQCD+UB+SU3','HQE210red-q-LQCD+UB','HQE321red-q-LQCD+UB','HQE321-q-LQCD+UB+SR']
    predictions_FF_u = ['BToD-f+','BToD-f0','BToD-fT','BToDstar-V','BToDstar-A0','BToDstar-A1','BToDstar-A12', 'BToDstar-T1','BToDstar-T2','BToDstar-T23']
    predictions_FF_s = ['BsToDs-f+', 'BsToDs-f0', 'BsToDs-fT', 'BsToDsstar-V', 'BsToDsstar-A0', 'BsToDsstar-A1', 'BsToDsstar-A12', 'BsToDsstar-T1', 'BsToDsstar-T2', 'BsToDsstar-T23']
    predictions_sat = ['saturations']
    predictions_LFU = ['LFU-ratios']
    predictions_BGL = ['BGL-coefficients-D', 'BGL-coefficients-Ds', 'BGL-coefficients-Dstar', 'BGL-coefficients-Dsstar']
    predictions_BGL_ratios = ['BGL-coefficients-ratios-S1', 'BGL-coefficients-ratios-V1', 'BGL-coefficients-ratios-fT', 'BGL-coefficients-ratios-A1', 'BGL-coefficients-ratios-A5', 'BGL-coefficients-ratios-V4', 'BGL-coefficients-ratios-P1', 'BGL-coefficients-ratios-T1', 'BGL-coefficients-ratios-T2', 'BGL-coefficients-ratios-T23']
    predictions_S6s = ['S6s']
    predictions_Ri = ['R1-ratio', 'R2-ratio', 'R0-ratio']
    predictions_FL = ['FL']

    predictions =  predictions_FF_u + predictions_FF_s + predictions_sat + predictions_LFU + predictions_BGL + predictions_BGL_ratios + predictions_Ri + predictions_FL

    for i in posteriors:
        for j in predictions:
            eos.predict_observables(af, i, j, base_directory=BASE_DIRECTORY)
