import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import seaborn as sns
import math

delays = pd.read_csv('./datasets/bus-breakdown-and-delays.csv', usecols=['How_Long_Delayed'])
delays['Delay'] = delays['How_Long_Delayed'].str.extract('(\d+)')
delays['is_canceled'] = delays['Delay'].isnull()
delays = delays[~ delays['is_canceled']][['Delay']]
delays['Delay'] =  pd.to_numeric(delays['Delay'])
# print(delays.head(10))

target_mean = delays['Delay'].mean()
target_stdev = stat.stdev(delays['Delay'])
sample_sizes = [5, 10, 20, 30, 50, 100]
sample_number = 100
idx = 1

for ss in sample_sizes:
    means = []
    for i in range(sample_number):
        sample = delays.sample(ss)
        sample_mean = sample['Delay'].mean()
        means.append(sample_mean)

    print('Sample size:', ss)
    print('Target mean:', target_mean)
    print('Mean of means:', stat.mean(means), 'Standard deviation/Standard error:', target_stdev/math.sqrt(ss) )

    plt.subplot(math.ceil(len(sample_sizes)/2), 2, idx)   
    plt.xlim(0, max(means))
    plt.ylabel('Sample size '+str(ss))
    sns.histplot(means, stat="density", kde=True) 
    idx+=1

plt.show()