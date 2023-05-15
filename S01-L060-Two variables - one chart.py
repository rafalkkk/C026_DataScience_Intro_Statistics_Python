import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def time_of_day(hour):
    if hour < 6:
        return 'night'
    elif hour < 12:
        return 'morning'
    elif hour < 18:
        return 'afternoon'
    else:
        return 'evening'

def trip_comment(trip_distance):
    if trip_distance < 1:
        return '1-mile'
    elif trip_distance < 2:
        return '2-miles'
    elif trip_distance < 3:
        return '3-miles'
    else:
        return '3+ miles'

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', engine='auto', 
        columns=['trip_distance', 'tpep_pickup_datetime', "tip_amount", "fare_amount","RatecodeID"], 
        storage_options=None, use_nullable_dtypes=False)

taxi.query("tpep_pickup_datetime>='2021-05-09' and tpep_pickup_datetime<'2021-05-10'", 
    inplace=True)

taxi['time_of_day'] = taxi['tpep_pickup_datetime'].dt.hour.apply(time_of_day) 
taxi['trip_comment'] = taxi['trip_distance'].apply(trip_comment) 

taxi_s = pd.crosstab(taxi["time_of_day"], taxi['trip_comment']) 
print('--- initial cross table ---')
print(taxi_s)

taxi_s = taxi_s.reindex(['night','morning','afternoon','evening'])
taxi_s = taxi_s[['1-mile', '2-miles','3-miles', '3+ miles']]
print('--- after setting up order ---')
print(taxi_s)

taxi_s.plot.bar()
plt.show()


taxi.query("tip_amount<=100 and fare_amount>0 and RatecodeID==4", inplace=True) 

print(taxi.head())
print(taxi.count())

taxi.plot.scatter(x='fare_amount', y='tip_amount')
plt.show()
