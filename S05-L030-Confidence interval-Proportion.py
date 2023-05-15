import scipy.stats as stats
import math

# alfa = 0.10 = 10%
# alfa/2 = 0.05 = 5%
# confidence level = 1 - alfa = 0.9 = 90%
# z-score taken from Z-statistics table for value of  1 - alfa/2 = 1 - 0.05 = 0.95
# 1.64

z_critical = stats.norm.ppf(0.95)      # Record z-critical value
print(f'z_critical={z_critical}')

p = 200/1000                           # Point estimate of proportion
n = 1000                               # Sample size

margin_of_error = z_critical * math.sqrt((p*(1-p))/n)
confidence_interval = (p - margin_of_error, p + margin_of_error) 
print(f'We are 90% confident that the ratio of population falls into this interval: {confidence_interval}')

confidence_interval = stats.norm.interval(confidence=0.95,               # Confidence level             
                                          loc=p,                         # Point estimate of proportion
                                          scale=math.sqrt((p*(1-p))/n))  # Scaling factor
print(f'We are 90% confident that the ratio of population falls into this interval: {confidence_interval}')

