import scipy.stats as stats
import statistics
import pandas as pd
import math
import random


# Two independent values and variance is known (sometimes "well known")
# H0: mean pizza Rome - mean pizza Naples <= 0  
# H1: mean pizza Rome - mean pizza Naples > 0

pizza_Naples = stats.norm.rvs(size=20, loc=8, scale=1)
pizza_Rome = stats.norm.rvs(size=15, loc=12, scale=5)

mean_Naples = statistics.mean(pizza_Naples)
mean_Rome = statistics.mean(pizza_Rome)
st_dev_Naples = statistics.stdev(pizza_Naples)
st_dev_Rome = statistics.stdev(pizza_Rome)
count_Naples = len(pizza_Naples)
count_Rome = len(pizza_Rome)

alpha = 0.05
confidence_level = 1-alpha
z_critical = stats.norm.ppf(q=1-alpha)
print(f'Z-critical = {z_critical}') 
z_score = ((mean_Rome - mean_Naples) - 0) / math.sqrt(st_dev_Rome**2/count_Rome + st_dev_Naples**2/count_Naples)
print(f'Z-score = {z_score}')

if z_critical < z_score :
    print('We reject H0')
else:
    print('We accept H0')

from statsmodels.stats.weightstats import ztest
z_stat, p_value = ztest(pizza_Rome, pizza_Naples, alternative='larger')
print(f'Z-test (p-value) = { p_value }')

if p_value < alpha:
    print('We reject H0')
else:
    print('We accept H0')


print('-'*60)
# Two independent values and variance is unknown and assumed to be equal
# H0: mean pizza Rome - mean pizza Naples <= 0  
# H1: mean pizza Rome - mean pizza Naples > 0

alpha = 0.05
confidence_level = 1-alpha
t_critical = stats.t.ppf(q=1-alpha, df=count_Rome+count_Naples-2)
print(f'T-critical = {t_critical}') 
var_p = ((count_Rome-1)*st_dev_Rome**2 +(count_Naples-1)*st_dev_Naples**2)/(count_Rome+count_Naples-2)
t_score = ((mean_Rome - mean_Naples) - 0) / math.sqrt(var_p/count_Rome + var_p/count_Naples)
print(f'T-score = {t_score}')

if t_critical < t_score:
    print('We reject H0')
else:
    print('We accept H0')

from statsmodels.stats.weightstats import ttest_ind
t_stat, p_value, df = ttest_ind(pizza_Rome, pizza_Naples, alternative='larger')
print(f'T-test (p-value) = { p_value }')

if p_value < alpha:
    print('We reject H0')
else:
    print('We accept H0')