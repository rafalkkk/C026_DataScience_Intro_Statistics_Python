from statistics import mean, median, mode

list1 = [1, 5, 9, 9, 9, 13, 17]
list2 = [1, 1, 9, 9, 9, 17, 17]

print(f'Mean:    list1 {mean(list1)}  list2 {mean(list2)}')
print(f'Median:  list1 {median(list1)}  list2 {median(list2)}')
print(f'Mode:    list1 {mode(list1)}  list2 {mode(list2)}')

from matplotlib import pyplot as plt
from random import randint, sample
from statistics import pvariance, variance

print('*** RANDOM LIST ***')
rand_list = [ randint(0, 100) for i in range(200)]

mean_population = mean(rand_list)
var_population = sum( [ (x - mean_population)**2  for x in rand_list ] ) / len(rand_list)

print(f"Population's variance {var_population} - {pvariance(rand_list)}")  

probe = sample(rand_list, 50)
mean_probe = mean(probe)
var_probe = sum( [ (x - mean_probe)**2  for x in probe ] ) / (len(probe) - 1)

print(f'Probe variance {var_probe} - {variance(probe)}')


pvariances=[]
variances=[]

for f in range(1, 101):
    probe = sample(rand_list, round(len(rand_list)*f/100))

    pvariances.append(pvariance(probe))
    variances.append(variance(probe))


# plt.hlines(xmin=1, xmax=100, y=var_population, linestyles='solid', colors='purple', linestyle='dotted')
# plt.plot(variances, color='blue')
# plt.plot(pvariances, color='red')
# plt.show()

list1 = [1, 5, 9, 9, 9, 13, 17]
list2 = [1, 1, 9, 9, 9, 17, 17]

print(f'Variance for list1 {pvariance(list1)}')
print(f'Variance for list2 {pvariance(list2)}')
