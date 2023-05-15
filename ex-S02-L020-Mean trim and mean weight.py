import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', 
        engine='auto', columns=['tip_amount','passenger_count'], storage_options=None, use_nullable_dtypes=False)

taxi.query('tip_amount > 0 and tip_amount <= 20 and passenger_count > 0', inplace=True)

print(taxi.describe())

taxi_mean = taxi.mean().iloc[0]
taxi_median = taxi.median().iloc[0]  # values[0]
taxi_mode = taxi.mode().iloc[0,0]
taxi_skew = taxi.skew()
taxi_trim_mean = stats.trim_mean(taxi["tip_amount"], 0.05)
taxi_weight_mean = np.average(taxi["tip_amount"], weights=taxi["passenger_count"])
print('Mean:', taxi_mean)
print('Median', taxi_median)
print('Mode:', taxi_mode)
print('Skew:', taxi_skew)
print('Trim weight:', taxi_trim_mean)
print('Weight mean', taxi_weight_mean)


taxi.plot.hist(column="tip_amount", bins=50) 
plt.axvline(taxi_mean, color='pink', linestyle='dotted')
plt.axvline(taxi_median, color='red', linestyle='dotted')
plt.axvline(taxi_mode, color='black', linestyle='dotted')
plt.axvline(taxi_trim_mean, color='yellow', linestyle='dotted')
plt.axvline(taxi_weight_mean, color='blue', linestyle='solid')
plt.show()



