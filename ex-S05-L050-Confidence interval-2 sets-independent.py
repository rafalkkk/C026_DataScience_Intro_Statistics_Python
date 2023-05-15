import scipy.stats as stats
import statistics
import pandas as pd
import math

# Two independent values and variance is known (sometimes "well known")

pizza_Naples = stats.norm.rvs(size=20, loc=8, scale=1)
pizza_Rome = stats.norm.rvs(size=15, loc=12, scale=5)

mean_Naples = statistics.mean(pizza_Naples)
mean_Rome = statistics.mean(pizza_Rome)
st_dev_Naples = statistics.stdev(pizza_Naples)
st_dev_Rome = statistics.stdev(pizza_Rome)
count_Naples = len(pizza_Naples)
count_Rome = len(pizza_Rome)

alpha = 0.1
alpha_2 = alpha/2
confidence_level = 1-alpha
z_critical = stats.norm.ppf(q=1-alpha_2)
print(f'Z-critical = {z_critical}') 
margin_of_error = z_critical * math.sqrt(st_dev_Naples**2/count_Naples + st_dev_Rome**2/count_Rome)
confidence_interval = ((mean_Rome-mean_Naples) - margin_of_error, (mean_Rome-mean_Naples) + margin_of_error)

print(f'We are {confidence_level} sure, that the pizza in Rome is more expensive then \
 in Naples by: {confidence_interval}')


# Two independent values and variance is unknown and assumed to be equal

pizza_Naples = stats.norm.rvs(size=20, loc=8, scale=1)
pizza_Rome = stats.norm.rvs(size=15, loc=12, scale=1)

mean_Naples = statistics.mean(pizza_Naples)
mean_Rome = statistics.mean(pizza_Rome)
st_dev_Naples = statistics.stdev(pizza_Naples)
st_dev_Rome = statistics.stdev(pizza_Rome)
count_Naples = len(pizza_Naples)
count_Rome = len(pizza_Rome)

alpha = 0.1
alpha_2 = alpha/2
confidence_level = 1-alpha
t_critical = stats.t.ppf(q=1-alpha_2, df=count_Naples+count_Rome-2)
print(f'T-critical = {t_critical}') 
var_p = ((count_Naples-1)*st_dev_Naples**2 +(count_Rome-1)*st_dev_Rome**2)/(count_Naples+count_Rome-2)
margin_of_error = t_critical * math.sqrt(var_p/count_Naples + var_p/count_Rome)
confidence_interval = ((mean_Rome-mean_Naples) - margin_of_error, (mean_Rome-mean_Naples) + margin_of_error)

print(f'We are {confidence_level} sure, that the pizza in Rome is more expensive then \
 in Naples by: {confidence_interval}')

