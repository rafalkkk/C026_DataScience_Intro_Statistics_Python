import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
'''
taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', engine='auto', 
        columns=['trip_distance', 'tpep_pickup_datetime', "tip_amount", "fare_amount","RatecodeID"], 
        storage_options=None, use_nullable_dtypes=False)

taxi.query("tpep_pickup_datetime>='2021-05-09' and tpep_pickup_datetime<'2021-05-10'", 
    inplace=True)

taxi.query("tip_amount<=100 and fare_amount>0 and RatecodeID==4 and tip_amount>0", inplace=True) 

print(taxi.describe())

# taxi.plot.scatter(x='fare_amount', y='tip_amount')
# plt.show()

fare_amount_mean = taxi['fare_amount'].mean()
fare_amount_stdev = taxi['fare_amount'].std()

tip_amount_mean = taxi['tip_amount'].mean()
tip_amount_stdev = taxi['tip_amount'].std()

fare_amount_lower = fare_amount_mean - 3 * fare_amount_stdev
fare_amount_upper = fare_amount_mean + 3 * fare_amount_stdev

tip_amount_lower = tip_amount_mean - 3 * tip_amount_stdev
tip_amount_upper = tip_amount_mean + 3 * tip_amount_stdev

outliers = taxi.query(f"(fare_amount<{fare_amount_lower} or fare_amount>{fare_amount_upper}) or "+
                      f"(tip_amount<{tip_amount_lower} or tip_amount>{tip_amount_upper})") 
taxi.query(f"(fare_amount>={fare_amount_lower} and fare_amount<={fare_amount_upper}) and "+
           f"(tip_amount>={tip_amount_lower} and tip_amount<={tip_amount_upper})",inplace=True) 
print(outliers)

fig, axes = plt.subplots(nrows=1,ncols=2)
taxi.boxplot('fare_amount', ax = axes[0], meanline=True) 
taxi.boxplot('tip_amount', ax = axes[1], meanline=True) 
plt.show()


taxi.plot.scatter(x='fare_amount', y='tip_amount')
plt.show()

print(taxi.describe())
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression

taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', engine='auto', 
        columns=['trip_distance', 'tpep_pickup_datetime', "tip_amount", "fare_amount","RatecodeID"], 
        storage_options=None, use_nullable_dtypes=False)

taxi.query("tpep_pickup_datetime>='2021-05-09' and tpep_pickup_datetime<'2021-05-10'", 
    inplace=True)

taxi.query("tip_amount<=100 and fare_amount>0 and RatecodeID==4 and tip_amount>0", inplace=True) 

ransac = RANSACRegressor(estimator=LinearRegression(),
                         #min_samples=50, 
                         max_trials=100,
                         loss='squared_error', random_state=42,
                         residual_threshold=10)

ransac.fit(taxi['fare_amount'].to_numpy().reshape(-1,1), taxi['tip_amount'].to_numpy().reshape(-1,1))

inliers_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inliers_mask)

plt.scatter(taxi['fare_amount'][inliers_mask], taxi['tip_amount'][inliers_mask],
            c='blue', edgecolor='white', marker='o', label='Inliers')

plt.scatter(taxi['fare_amount'][outlier_mask], taxi['tip_amount'][outlier_mask],
             c='red', edgecolor='white', marker='s', label='Outliers')            

plt.show()
