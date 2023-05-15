import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import math

# H0 - mean speed of typing is <= 40 wpm
# H1 - mean speed of typing is > 40 wpm

speed_h0 = 40

speed_test = stats.norm.rvs(size=20, loc=45, scale=15)
speed_test = speed_test.astype(int)

speed_test_len = len(speed_test)
speed_test_mean = speed_test.mean()
speed_test_stdev = speed_test.std()

t_score = (speed_test_mean - speed_h0)/(speed_test_stdev/math.sqrt(speed_test_len))
print(f't-score={t_score}')

alpha = 0.05
confidence = 1 - alpha
t_critical = t_critical = stats.t.ppf(q=confidence, df=speed_test_len-1) 
print(f't-critical={t_critical}')

if t_score > t_critical:
    print('H0 should be rejected')
else:
    print('H0 should be accepted')



