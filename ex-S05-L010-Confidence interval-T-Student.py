import scipy.stats as stats
import math
import numpy as np


population = stats.t.rvs(size=100000, loc=45, scale=5)

sample_size = 30
sample = np.random.choice(a=population, size=sample_size)
sample_mean = sample.mean()
sample_stdev = sample.std()

# calculate confidence interval for 80% confidence level with Z-distribution
t_critical = stats.t.ppf(q=0.90, df=sample_size-1)  # 1-alpha/2 = 1-0.2/2 = 1-0.1 = 0.9
margin_of_error = t_critical * (sample_stdev/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)  
print(f"80%-Confidence interval T (basing on one sample): {confidence_interval}")

# calculate confidence interval for 90% confidence level with Z-distribution
t_critical = stats.t.ppf(q=0.95, df=sample_size-1)  # 1-alpha/2 = 1-0.1/2 = 1-0.05 = 0.95
margin_of_error = t_critical * (sample_stdev/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)  
print(f"90%-Confidence interval T (basing on one sample): {confidence_interval}")

# calculate confidence interval for 95% confidence level with Z-distribution
t_critical = stats.norm.ppf(q=0.975, df=sample_size-1)  # 1-alpha/2 = 1-0.05/2 = 1-0.025 = 0.975
margin_of_error = t_critical * (sample_stdev/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)  
print(f"95%-Confidence interval T (basing on one sample): {confidence_interval}")

