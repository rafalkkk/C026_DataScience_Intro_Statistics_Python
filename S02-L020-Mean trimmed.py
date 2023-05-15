import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', 
        engine='auto', columns=['trip_distance'], storage_options=None, use_nullable_dtypes=False)

taxi.query('trip_distance > 0 and trip_distance < 10', inplace=True)

print(taxi.describe())

taxi_mean = taxi.mean().iloc[0]
taxi_median = taxi.median().iloc[0]  # values[0]
taxi_mode = taxi.mode().iloc[0,0]
taxi_trim_mean = stats.trim_mean(taxi["trip_distance"], 0.1)

print('Mean:', taxi_mean)
print('Median', taxi_median)
print('Mode:', taxi_mode)
print('Skew:', taxi.skew())
print('Trim/Truncate mean:', taxi_trim_mean)

# show picture with histogram
taxi.plot.hist(column="trip_distance", bins=50)  #np.linspace(0, 100, 1))
plt.axvline(taxi_mean, color='blue', linestyle='dotted')
plt.axvline(taxi_median, color='red', linestyle='dotted')
plt.axvline(taxi_mode, color='green', linestyle='dotted')
plt.show()

'''
pip install pandas pyarrow IPython matplotlib
'''
import pandas as pd

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', 
        engine='auto', columns=None, storage_options=None, use_nullable_dtypes=False)

means=[]
medians=[]
modes=[]
trim_means = []
for f in range(1, 101):
    df_probe = taxi.sample(frac=(f/100))
    probe_mean = df_probe["trip_distance"].mean()
    probe_median = df_probe["trip_distance"].median()
    probe_mode = df_probe["trip_distance"].mode().iloc[0]
    probe_trim_mean = stats.trim_mean(df_probe['trip_distance'], 0.1)

    means.append(probe_mean)
    medians.append(probe_median)
    modes.append(probe_mode)
    trim_means.append(probe_trim_mean)
    print(f, probe_mean, probe_median, probe_mode, probe_trim_mean)

from matplotlib import pyplot as plt
plt.hlines(xmin=1, xmax=100, y=taxi['trip_distance'].mean(), linestyles='solid', colors='blue', linestyle='dotted')
plt.hlines(xmin=1, xmax=100, y=taxi['trip_distance'].median(), linestyles='solid', colors='orange', linestyle='dotted')
plt.hlines(xmin=1, xmax=100, y=taxi['trip_distance'].mode().iloc[0], linestyles='solid', colors='black', linestyle='dotted')
plt.hlines(xmin=1, xmax=100, y=stats.trim_mean(taxi['trip_distance'], 0.1), linestyles='solid', colors='purple', linestyle='dotted')


plt.plot(means, color='red')
plt.plot(medians, color='green')
plt.plot(modes, color='grey')
plt.plot(trim_means, color='pink')

plt.show()
