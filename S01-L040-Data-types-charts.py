import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import PercentFormatter


taxi = pd.read_parquet('./datasets/yellow_tripdata_2021-05.parquet', 
        engine='auto', columns=['tpep_pickup_datetime'], 
        storage_options=None, use_nullable_dtypes=False)

taxi = taxi.query("tpep_pickup_datetime >= '2021-05-02' and tpep_pickup_datetime < '2021-05-30'")
cat_weekdays = [ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cat_type = CategoricalDtype(categories=cat_weekdays, ordered=True)
taxi['dayofweek'] = taxi['tpep_pickup_datetime'].dt.day_name().astype(cat_type)

taxi = taxi.groupby(['dayofweek'],as_index=False).count()
print(taxi)

taxi.rename(columns={'tpep_pickup_datetime':'count'}, inplace=True)
print(taxi)

taxi.set_index('dayofweek', inplace=True)
print(taxi)

taxi.plot.bar(y='count', legend=False)
plt.show()

taxi.plot.pie(y='count', legend=False, counterclock=False, autopct='%1.1f%%')
# plt.ylabel("")
plt.show()

# PARETO by weekday

taxi.sort_values(by='count', ascending=False, inplace=True)
taxi["cummulative_percent"] = taxi["count"].cumsum()/taxi["count"].sum()*100

print(taxi)

fig, ax = plt.subplots()
ax.bar(taxi.index, taxi["count"], color="C0")
ax2 = ax.twinx()
ax2.plot(taxi.index, taxi["cummulative_percent"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
plt.show()
