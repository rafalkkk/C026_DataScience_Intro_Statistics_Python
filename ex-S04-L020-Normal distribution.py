# https://dataverse.harvard.edu/dataverse/r4r

import pandas as pd
from matplotlib import pyplot as plt

sleep = pd.read_csv('./datasets/sleep/sleep.csv', 
                    usecols=['Date', 'Minutes.Asleep', 'Number.of.Awakenings'])

plt.hist(sleep['Minutes.Asleep'], bins=20)
plt.title('Minutes asleep')
plt.show()

sleep = sleep[sleep["Number.of.Awakenings"]>0]

plt.hist(sleep['Number.of.Awakenings'], bins=20)
plt.title('Number of awakenings')
plt.show()

sleep_mean = sleep['Number.of.Awakenings'].mean()
sleep_stdev = sleep['Number.of.Awakenings'].std()
sleep["sleep-z-score"] = (sleep['Number.of.Awakenings'] - sleep_mean) / sleep_stdev
plt.hist(sleep['sleep-z-score'], bins=20)
plt.show()
