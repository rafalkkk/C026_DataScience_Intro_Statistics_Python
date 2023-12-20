import random as r
import statistics as stat
import math

my_list = [r.randint(0,100) for i in range(200)]

my_list_1 = [i + 2 for i in my_list]
my_list_2 = [i * 2 for i in my_list]
my_list_3 = [i * 2 + 2 for i in my_list]
my_list_4 = [math.sqrt(i) for i in my_list]

print('Population variance - random numbers', stat.pvariance(my_list))
print('Population variance - plus 2        ', stat.pvariance(my_list_1))
print('Population variance - multi 2       ', stat.pvariance(my_list_2))
print('Population variance - multi 2 plus 2', stat.pvariance(my_list_3))
print('Population variance - root square   ', stat.pvariance(my_list_4))

my_sample = r.sample(my_list, 20)
my_sample_1 = r.sample(my_list_1, 20)
my_sample_2 = r.sample(my_list_2, 20)
my_sample_3 = r.sample(my_list_3, 20)
my_sample_4 = r.sample(my_list_4, 20)

print('Probe variance - random numbers',stat.variance(my_sample))
print('Probe variance - plus 2        ',stat.variance(my_sample_1))
print('Probe variance - multi 2       ',stat.variance(my_sample_2))
print('Probe variance - multi 2 plus 2',stat.variance(my_sample_3))
print('Probe variance - root square   ',stat.variance(my_sample_4))
