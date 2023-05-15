import scipy.stats as stats
import statistics
import pandas as pd
import math
import random


# Two independent values and variance is known (sometimes "well known")
# H0: mean therapists - mean doctors <= 0  
# H1: mean therapitst - mean doctors > 0

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

alpha = 0.05
confidence_level = 1-alpha
z_critical = stats.norm.ppf(q=1-alpha)
print(f'Z-critical = {z_critical}') #1.644
z_score = ((mean_ther - mean_doc) - 0) / math.sqrt(st_dev_ther**2/count_ther + st_dev_doc**2/count_doc)
print(f'Z-score = {z_score}')

if z_critical < z_score :
    print('We reject H0')
else:
    print('We accept H0')

from statsmodels.stats.weightstats import ztest
z_stat, p_value = ztest(therapists, doctors, alternative='larger')
print(f'Z-test (p-value) = { p_value }')

if p_value < alpha:
    print('We reject H0')
else:
    print('We accept H0')


print('-'*60)
# Two independent values and variance is unknown and assumed to be equal
# H0: mean therapists - mean doctors <= 0  
# H1: mean therapitst - mean doctors > 0

alpha = 0.05
confidence_level = 1-alpha
t_critical = stats.t.ppf(q=1-alpha, df=count_doc+count_ther-2)
print(f'T-critical = {t_critical}') #1.6590851435825054
var_p = ((count_doc-1)*st_dev_doc**2 +(count_ther-1)*st_dev_ther**2)/(count_doc+count_ther-2)
t_score = ((mean_ther - mean_doc) - 0) / math.sqrt(var_p/count_doc + var_p/count_ther)
print(f'T-score = {t_score}')

if t_critical < t_score:
    print('We reject H0')
else:
    print('We accept H0')

from statsmodels.stats.weightstats import ttest_ind
t_stat, p_value, df = ttest_ind(therapists, doctors, alternative='larger')
print(f'T-test (p-value) = { p_value }')

if p_value < alpha:
    print('We reject H0')
else:
    print('We accept H0')