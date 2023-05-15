import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', 
        engine='auto', columns=['tip_amount'], storage_options=None, use_nullable_dtypes=False)

taxi.query('tip_amount > 0 and tip_amount <= 20', inplace=True)

min_tip = taxi['tip_amount'].min()
max_tip = taxi['tip_amount'].max()
number_of_bins = 10

# Manual calculation of good interval width
interval_width = (max_tip - min_tip) / number_of_bins
print(f'Good interval width for {number_of_bins} bins is {interval_width}')


# Automatic calculation of intervals
abs_frequency, intervals = np.histogram(taxi["tip_amount"], bins = number_of_bins)
print('Automatically calculated intervals', abs_frequency, intervals, len(abs_frequency), len(intervals))

# create borders of intervals
interval_range = pd.interval_range(start=0, freq=interval_width, end=max_tip, closed='right')
# assign each row to a bin
taxi['bin'] = pd.cut(taxi['tip_amount'], bins=interval_range)
print(taxi.head())
# calculate counts for each bin
freq_table = pd.crosstab(index=taxi["bin"], columns="tip_amount") 
print(freq_table)

# # ilustrate as bar chart
# freq_table.plot.bar(y='tip_amount', legend=False)
# plt.show()

# ilustrate as histogram
taxi.plot.hist(column="tip_amount", bins=number_of_bins)
# change labels on x-axis
plt.xticks([ i*2 for i in range(number_of_bins)], [ i*2 for i in range(number_of_bins)])
plt.show()



