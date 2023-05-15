from statistics import mean, median, mode, pvariance, variance, pstdev, stdev

list1 = [1, 5, 9, 9, 9, 13, 17]
list2 = [1, 1, 9, 9, 9, 17, 17]

print(f'Mean:    list1 {mean(list1)}  list2 {mean(list2)}')
print(f'Median:  list1 {median(list1)}  list2 {median(list2)}')
print(f'Mode:    list1 {mode(list1)}  list2 {mode(list2)}')
print(f'Variance for list1 {pvariance(list1)}')
print(f'Variance for list2 {pvariance(list2)}')
print(f'Standard deviation for list1 {pstdev(list1)}')
print(f'Standard deviation for list2 {pstdev(list2)}')

from matplotlib import pyplot as plt
from random import randint, sample
from math import sqrt

print('*** RANDOM LIST ***')
rand_list = [ randint(0, 100) for i in range(200)]

mean_population = mean(rand_list)
var_population = sum( [ (x - mean_population)**2  for x in rand_list ] ) / len(rand_list)
stdev_population = sqrt(var_population)

print(f"Population's variance {var_population} - {pvariance(rand_list)}")  
print(f"Population's standard variance {stdev_population} - {pstdev(rand_list)}")  

probe = sample(rand_list, 50)
mean_probe = mean(probe)
var_probe = sum( [ (x - mean_probe)**2  for x in probe ] ) / (len(probe) - 1)
stdev_probe = sqrt(var_probe)

print(f'Probe variance {var_probe} - {variance(probe)}')
print(f'Probe standard deviation {stdev_probe} - {stdev(probe)}')



packages_kg = [2, 12, 6, 2, 1, 4, 1, 20, 8, 4, 1, 2, 10, 9]
packages_lbs = [x * 2.20462262185 for x in packages_kg]
print(packages_kg, "\n", packages_lbs)

import pandas as pd

df = pd.DataFrame(columns=["Function", "KG", "LBS"])
df.loc[len(df)] = ['Mean', mean(packages_kg), mean(packages_lbs)]
df.loc[len(df)] = ['Variance', variance(packages_kg), variance(packages_lbs)]
df.loc[len(df)] = ['St Dev', stdev(packages_kg), stdev(packages_lbs)]
df.loc[len(df)] = ['Coef var', stdev(packages_kg)/mean(packages_kg), stdev(packages_lbs)/mean(packages_lbs)]
print(df)
