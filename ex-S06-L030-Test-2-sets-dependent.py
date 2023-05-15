import pandas as pd
import scipy.stats as stats
import math
from statsmodels.stats.weightstats import ztest

year_1 = [51.54147388, 66.37933735, 86.06956843, 61.21211192, 70.97453697, 67.818349
, 74.61029388, 64.15260126, 64.04404262, 73.20343147, 84.00388888, 71.76197586
, 81.92905628, 59.79383455, 69.76258392, 67.26433896, 76.15317597, 74.63963851
, 69.54745953, 81.37239488, 66.75573044, 65.68174176, 72.39491011, 94.49928345
, 50.02791987, 85.30256927, 73.19244005, 68.75115665, 70.17895383, 72.74099816]

year_2 = [87.10363669, 75.94465019, 63.60003755, 67.54621323, 78.9299618, 85.09730193
, 76.9517496, 75.36388527, 80.60139972, 80.61204067, 86.94199771, 65.38143752
, 84.08922726, 94.28436019, 77.85826007, 73.84883098, 69.77960042, 78.94087383
, 83.0521829, 56.88821237, 79.48768691, 82.4386409, 82.94123142, 89.38153559
, 65.55075576, 75.03079448, 78.38170544, 57.94891699, 82.68846853, 88.63010176]

# H0 - Mean delay is <= 5
# H1 - Mean delay is > 5

h0_difference = 5
df = pd.DataFrame(list(zip(year_1, year_2)), columns=['y1', 'y2'])
df['diff'] = df['y2'] - df['y1']

alpha = 0.10
sample_size = len(df)
sample_mean = df['diff'].mean()
sample_stdev = df['diff'].std()
confidence_level = 1-alpha

t_critical = stats.t.ppf(q=confidence_level, df=sample_size-1)  #1.699
print(f'T-critical = {t_critical}')

t_score = (sample_mean - h0_difference)/(sample_stdev/math.sqrt(sample_size))
print(f'T-score = {t_score}')

if t_critical < t_score:
    print('H0 is rejected')
else:
    print('H0 is accepted')


test_stat, p_value = ztest(df["y2"], df["y1"], value=h0_difference, alternative='larger')
print(f'Z-test (p-value) = { p_value }')

if p_value < alpha:
    print('H0 is rejected')
else:
    print('H0 is accepted')
