import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', 
        engine='auto', columns=['tip_amount'], storage_options=None, use_nullable_dtypes=False)

taxi.query('tip_amount > 0 and tip_amount <= 20', inplace=True)

print(taxi.describe())

taxi_mean = taxi.mean().iloc[0]
taxi_median = taxi.median().iloc[0]  # values[0]
taxi_mode = taxi.mode().iloc[0,0]
taxi_skew = taxi.skew()
print('Mean:', taxi_mean)
print('Median', taxi_median)
print('Mode:', taxi_mode)
print('Skew:', taxi_skew)


taxi.plot.hist(column="tip_amount", bins=50) 
plt.axvline(taxi_mean, color='pink', linestyle='dotted')
plt.axvline(taxi_median, color='red', linestyle='dotted')
plt.axvline(taxi_mode, color='black', linestyle='dotted')
plt.show()



