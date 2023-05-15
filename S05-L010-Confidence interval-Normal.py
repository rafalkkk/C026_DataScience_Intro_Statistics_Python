import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats
import math


population = stats.norm.rvs(size=100000, loc=45, scale=5)
population_mean = population.mean()
population_stdev = population.std()

# h,_,_ = plt.hist(x=population, bins=50)
# plt.vlines(x=population_mean, colors='red', ymin=0, ymax=h.max())
# plt.title('Histogram for population')
# plt.show()


sample_size = 50
sample = np.random.choice(a=population, size=sample_size)
sample_mean = sample.mean()
sample_stdev = sample.std()

# calculate confidence interval for 95% confidence level with Z-distribution
z_critical = stats.norm.ppf(q=0.975) 
margin_of_error = z_critical * (population_stdev/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)  
print(f"Confidence interval Z (basing on one sample): {confidence_interval} (z-critical {z_critical} population stdev {population_stdev})")


interval = stats.norm.interval(confidence= 0.95,      
                 loc = sample_mean,    
                 scale = population_stdev/math.sqrt(sample_size)) 
print('Z:', interval)


intervals = []
sample_means = []

for sample in range(50):
    sample = np.random.choice(a=population, size=sample_size)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)

    z_critical = stats.norm.ppf(q=0.975) 
    margin_of_error = z_critical * (population_stdev/math.sqrt(sample_size))
    confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)    
    intervals.append(confidence_interval)

plt.figure()
plt.title('Is the population mean indeed in the confidence interval? Z-distribution')
plt.errorbar(x=np.arange(0, 50, 1), 
             y=sample_means, 
             yerr=[(end-begin)/2 for begin,end in intervals],
             fmt='o')
plt.hlines(xmin=0, xmax=50,
           y=population_mean, 
           linewidth=2.0,
           color="red")
plt.show()
