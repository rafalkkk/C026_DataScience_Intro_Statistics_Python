import scipy.stats as stats
import statistics
import pandas as pd
import math
import random


# Two dependent values (regression: before and after)

df = pd.read_csv('./datasets/prices-singapore.csv')
df['diff'] = df['2020'] - df['2010']

print('Before:',df['2010'].mean(),df['2010'].std())
print('After:', df['2020'].mean(), df['2020'].std())

# alpha = 0.1
# alpha/2 = 0.05
# confidence level = 1 - alpha = 0.9
# T-critical (degree of freedom = 52-1, alpha/2 = 0.05) 

alpha = 0.1
alpha_2 = alpha/2
sample_size = len(df)
sample_mean = df['diff'].mean()
sample_stdev = df['diff'].std()
confidence_level = 1-alpha

t_critical = stats.t.ppf(q=confidence_level+alpha_2, df=sample_size-1) 
print(f'T-critical = {t_critical}')

margin_of_error = t_critical * sample_stdev/math.sqrt(sample_size)
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print(f"We are {confidence_level} sure that the mean difference for products' price falls between: {confidence_interval}")


# alpha = 0.05
# alpha/2 = 0.025
# confidence level = 1 - alpha = 0.95
# T-critical (degree of freedom = 29, alpha/2 = 0.025)

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

print(f"We are {confidence_level} sure that the mean difference for products' price falls between: {confidence_interval}")
