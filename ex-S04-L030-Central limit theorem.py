import pandas as pd
import statistics as stat
from matplotlib import pyplot as plt
import seaborn as sns

sleep = pd.read_csv('./datasets/sleep/sleep.csv', 
                    usecols=['Date', 'Minutes.Asleep', 'Number.of.Awakenings'])

sample_size = 30
sample_number = 20

means_sleep = []
means_awaken = []

sleep_mean = sleep["Minutes.Asleep"].mean()
awaken_mean = sleep["Number.of.Awakenings"].mean()

for i in range(sample_number):
    sample = sleep.sample(sample_size)
    means_sleep.append(sample["Minutes.Asleep"].mean())
    means_awaken.append(sample["Number.of.Awakenings"].mean())

plt.subplot(2, 1, 1)   
plt.xlim(0, max(means_sleep))
sns.histplot(means_sleep, stat="density", kde=True) 

plt.subplot(2, 1, 2)   
plt.xlim(0, max(means_awaken))
sns.histplot(means_awaken, stat="density", kde=True) 

print(f"Sleep time: Real mean = {sleep_mean}, estimated mean = {stat.mean(means_sleep)}")
print(f"Awakenings: Real mean = {awaken_mean}, estimated mean = {stat.mean(means_awaken)}")

plt.show()

