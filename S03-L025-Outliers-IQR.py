import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', engine='auto', 
        columns=['trip_distance', 'tpep_pickup_datetime', "tip_amount", "fare_amount","RatecodeID"], 
        storage_options=None, use_nullable_dtypes=False)

taxi.query("tpep_pickup_datetime>='2021-05-09' and tpep_pickup_datetime<'2021-05-10'", 
    inplace=True)

taxi.query("tip_amount<=100 and fare_amount>0 and RatecodeID==4 and tip_amount>0", inplace=True) 

# taxi.plot.scatter(x='fare_amount', y='tip_amount')
# plt.show()

# taxi.boxplot(['fare_amount', 'tip_amount'])
# plt.show()

# fig, axes = plt.subplots(nrows=1,ncols=2)
# taxi.boxplot('fare_amount', ax = axes[0], meanline=True) 
# taxi.boxplot('tip_amount', ax = axes[1], meanline=True) 
# plt.show()

fare_amount_q1 = taxi['fare_amount'].quantile(0.25)
fare_amount_q3 = taxi['fare_amount'].quantile(0.75)
fare_amount_iqr = fare_amount_q3 - fare_amount_q1
fare_amount_lower = fare_amount_q1 - 1.5 * fare_amount_iqr
fare_amount_upper = fare_amount_q3 + 1.5 * fare_amount_iqr

tip_amount_q1 = taxi['tip_amount'].quantile(0.25)
tip_amount_q3 = taxi['tip_amount'].quantile(0.75)
tip_amount_iqr = tip_amount_q3 - tip_amount_q1
tip_amount_lower = tip_amount_q1 - 1.5 * tip_amount_iqr
tip_amount_upper = tip_amount_q3 + 1.5 * tip_amount_iqr

outliers = taxi.query(f"(fare_amount<{fare_amount_lower} or fare_amount>{fare_amount_upper}) or "+
                      f"(tip_amount<{tip_amount_lower} or tip_amount>{tip_amount_upper})") 
taxi.query(f"(fare_amount>={fare_amount_lower} and fare_amount<={fare_amount_upper}) and "+
                      f"(tip_amount>={tip_amount_lower} and tip_amount<={tip_amount_upper})",inplace=True) 
print(outliers)

# taxi.plot.scatter(x='fare_amount', y='tip_amount')
# plt.show()

fig, axes = plt.subplots(nrows=1,ncols=2)
taxi.boxplot('fare_amount', ax = axes[0], meanline=True) 
taxi.boxplot('tip_amount', ax = axes[1], meanline=True) 
plt.show()

print(taxi.describe())
