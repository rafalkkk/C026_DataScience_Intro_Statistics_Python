import scipy.stats as stats
import statistics
import pandas as pd
import math
import random


# Two dependent values (regression: before and after)

size = 30
results_before = stats.norm.rvs(size=size, loc=14, scale=1)
change = stats.norm.rvs(size=size, loc=0.2, scale=0.5)
results_after = [x+y for (x,y) in zip(results_before, change)]

df = pd.DataFrame(list(zip(results_before, results_after)), columns=['before', 'after'])
df['diff'] = df['after'] - df['before']
print(df)

print('Before:',df['before'].mean(),df['before'].std())
print('After:', df['after'].mean(), df['after'].std())



# alpha = 0.1
# alpha/2 = 0.05
# confidence level = 1 - alpha = 0.9
# T-critical (degree of freedom = 29, alpha/2 = 0.05) = 1,699

alpha = 0.1
alpha_2 = alpha/2
sample_size = len(df)
sample_mean = df['diff'].mean()
sample_stdev = df['diff'].std()
confidence_level = 1-alpha

t_critical = stats.t.ppf(q=confidence_level+alpha_2, df=sample_size-1) # 1.699
print(f'T-critical = {t_critical}')

margin_of_error = t_critical * sample_stdev/math.sqrt(sample_size)
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print(f'We are {confidence_level} sure that the effect in the population will be in interval {confidence_interval}')


# alpha = 0.05
# alpha/2 = 0.025
# confidence level = 1 - alpha = 0.95
# T-critical (degree of freedom = 29, alpha/2 = 0.025) = 2.045

alpha = 0.05
alpha_2 = alpha/2
sample_size = len(df)
sample_mean = df['diff'].mean()
sample_stdev = df['diff'].std()
confidence_level = 1-alpha

t_critical = stats.t.ppf(q=confidence_level+alpha_2, df=sample_size-1)
print(f'T-critical = {t_critical}')
margin_of_error = t_critical * sample_stdev/math.sqrt(sample_size)
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error) 

print(f'We are {confidence_level} sure that the effect in the population will be in interval {confidence_interval}')



# Two independent values and variance is known (sometimes "well known")
print('-'*80)

doctors = stats.norm.rvs(size=70, loc=65, scale=10)
therapists = stats.norm.rvs(size=40, loc=75, scale=10)

print(min(doctors), max(doctors))
print(min(therapists), max(therapists))

mean_doc = statistics.mean(doctors)
mean_ther = statistics.mean(therapists)
st_dev_doc = statistics.stdev(doctors)
st_dev_ther = statistics.stdev(therapists)
count_doc = len(doctors)
count_ther = len(therapists)
