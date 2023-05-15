import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', 
        engine='auto', columns=['trip_distance'], storage_options=None, use_nullable_dtypes=False)

taxi.query('trip_distance > 0 and trip_distance < 10', inplace=True)

print(taxi.describe())

taxi_mean = taxi.mean().iloc[0]
taxi_median = taxi.median().iloc[0]  # values[0]
taxi_mode = taxi.mode().iloc[0,0]
taxi_skew = taxi.skew()
print('Mean:', taxi_mean)
print('Median', taxi_median)
print('Mode:', taxi_mode)
print('Skew:', taxi_skew)


taxi.plot.hist(column="trip_distance", bins=50) 
plt.axvline(taxi_mean, color='pink', linestyle='dotted')
plt.axvline(taxi_median, color='red', linestyle='dotted')
plt.axvline(taxi_mode, color='black', linestyle='dotted')
plt.show()


means=[]
medians=[]
modes=[]
for f in range(1, 101):
    df_probe = taxi.sample(frac=(f/100))
    probe_mean = df_probe["trip_distance"].mean()
    probe_median = df_probe["trip_distance"].median()
    probe_mode = df_probe["trip_distance"].mode().iloc[0]

    means.append(probe_mean)
    medians.append(probe_median)
    modes.append(probe_mode)
    print(f, probe_mean, probe_median, probe_mode)

plt.hlines(xmin=1, xmax=100, y=taxi_mean, linestyles='solid', colors='pink', linestyle='dotted')
plt.hlines(xmin=1, xmax=100, y=taxi_median, linestyles='solid', colors='green', linestyle='dotted')
plt.hlines(xmin=1, xmax=100, y=taxi_mode, linestyles='solid', colors='black', linestyle='dotted')
plt.plot(means, color='red')
plt.plot(medians, color='green')
plt.plot(modes, color='blue')
plt.show()

