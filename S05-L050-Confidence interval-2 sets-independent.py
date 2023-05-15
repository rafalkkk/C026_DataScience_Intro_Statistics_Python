import scipy.stats as stats
import statistics
import pandas as pd
import math
import random


# Two independent values and variance is known (sometimes "well known")

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

alpha = 0.1
alpha_2 = alpha/2
confidence_level = 1-alpha
z_critical = stats.norm.ppf(q=1-alpha_2)
print(f'Z-critical = {z_critical}') #1.6448536269514722
margin_of_error = z_critical * math.sqrt(st_dev_doc**2/count_doc + st_dev_ther**2/count_ther)
confidence_interval = ((mean_ther-mean_doc) - margin_of_error, (mean_ther-mean_doc) + margin_of_error)

print(f'We are {confidence_level} sure, that the difference between results of thereapists and doctors\
 falls into interval {confidence_interval}')



alpha = 0.05
alpha_2 = alpha/2
confidence_level = 1-alpha
z_critical = stats.norm.ppf(q=1-alpha_2)
print(f'Z-critical = {z_critical}') #1.959963984540054
margin_of_error = z_critical * math.sqrt(st_dev_doc**2/count_doc + st_dev_ther**2/count_ther)
confidence_interval = ((mean_ther-mean_doc) - margin_of_error, (mean_ther-mean_doc) + margin_of_error)

print(f'We are {confidence_level} sure, that the difference between results of thereapists and doctors\
 falls into interval {confidence_interval}')


# Two independent values and variance is unknown and assumed to be equal

alpha = 0.1
alpha_2 = alpha/2
confidence_level = 1-alpha
t_critical = stats.t.ppf(q=1-alpha_2, df=count_doc+count_ther-2)
print(f'T-critical = {t_critical}') #1.6590851435825054
var_p = ((count_doc-1)*st_dev_doc**2 +(count_ther-1)*st_dev_ther**2)/(count_doc+count_ther-2)
margin_of_error = t_critical * math.sqrt(var_p/count_doc + var_p/count_ther)
confidence_interval = ((mean_ther-mean_doc) - margin_of_error, (mean_ther-mean_doc) + margin_of_error)

print(f'We are {confidence_level} sure, that the difference between results of thereapists and doctors\
 falls into interval {confidence_interval}')


alpha = 0.05
alpha_2 = alpha/2
confidence_level = 1-alpha
t_critical = stats.t.ppf(q=1-alpha_2, df=count_doc+count_ther-2)
print(f'T-critical = {t_critical}') #1.982173483257451
var_p = ((count_doc-1)*st_dev_doc**2 +(count_ther-1)*st_dev_ther**2)/(count_doc+count_ther-2)
margin_of_error = t_critical * math.sqrt(var_p/count_doc + var_p/count_ther)
confidence_interval = ((mean_ther-mean_doc) - margin_of_error, (mean_ther-mean_doc) + margin_of_error)

print(f'We are {confidence_level} sure, that the difference between results of thereapists and doctors\
 falls into interval {confidence_interval}')
