import numpy as np
import scipy.stats as stats
import math


population = stats.norm.rvs(size=100000, loc=45, scale=5)
population_mean = population.mean()
population_stdev = population.std()

sample_size = 50
sample = np.random.choice(a=population, size=sample_size)
sample_mean = sample.mean()
sample_stdev = sample.std()

# calculate confidence interval for 80% confidence level with Z-distribution
z_critical = stats.norm.ppf(q=0.90)  # 1-alpha/2 = 1-0.2/2 = 1-0.1 = 0.9
margin_of_error = z_critical * (population_stdev/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)  
print(f"80%-Confidence interval Z (basing on one sample): {confidence_interval}")

# calculate confidence interval for 90% confidence level with Z-distribution
z_critical = stats.norm.ppf(q=0.95)  # 1-alpha/2 = 1-0.1/2 = 1-0.05 = 0.95
margin_of_error = z_critical * (population_stdev/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)  
print(f"90%-Confidence interval Z (basing on one sample): {confidence_interval}")

# calculate confidence interval for 95% confidence level with Z-distribution
z_critical = stats.norm.ppf(q=0.975)  # 1-alpha/2 = 1-0.05/2 = 1-0.025 = 0.975
margin_of_error = z_critical * (population_stdev/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)  
print(f"95%-Confidence interval Z (basing on one sample): {confidence_interval}")

