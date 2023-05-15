import pandas as pd
import random

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', 
        engine='auto', columns=None, storage_options=None, use_nullable_dtypes=False)

probe_size=100

sample_indexes = random.sample(range(len(taxi.index)), probe_size)

taxi_probe = pd.DataFrame(data=None, columns=taxi.columns)
for i in range(probe_size):
    taxi_probe.loc[i] = taxi.loc[sample_indexes[i]]

print(taxi_probe['trip_distance'].mean())
