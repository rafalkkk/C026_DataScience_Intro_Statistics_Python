import matplotlib.pyplot as plt
import statistics
from statsmodels.stats.weightstats import ztest
import scipy.stats as stats
import pandas as pd
import math

# H0 - mean speed of typing is <= 40 wpm
# H1 - mean speed of typing is > 40 wpm

speed_h0 = 40

speed_test = [41, 42, 34, 37, 40, 15, 46, 27, 35, 55, 52, 64, 51, 57, 49, 38, 76, 45, 65, 57, 68, 79, 44, 43,
               23, 58, 53, 56, 15, 32, 37, 54, 43, 47, 55, 38, 50, 48, 55, 71, 78, 46, 54, 36, 44, 40, 31, 13,
               55, 45, 40, 21, 27, 72, 54, 15, 30, 24, 20, 63, 18, 45, 48, 36, 42, 52, 55, 34, 47, 47, 11, 39,
               47, 59, 52, 33, 36, 38, 63, 47, 40, 43, 20, 65, 43, 61, 29, 64, 64, 46, 53, 59, 34, 47, 41, 24,
               51, 54, 60, 39]

speed_test_len = len(speed_test)
speed_test_mean = statistics.mean(speed_test)
speed_test_stdev = statistics.stdev(speed_test)

z_score = (speed_test_mean - speed_h0)/(speed_test_stdev/math.sqrt(speed_test_len))

for i in range(100, 1, -1):

    alpha = i/10000
    confidence = 1 - alpha
    z_critical = stats.norm.ppf(q=confidence) 

    if z_score > z_critical:
        print(f'{alpha} - H0 should be rejected ({z_score} > {z_critical})')
    else:
        print(f'{alpha} - H0 should be accepted ({z_score} <= {z_critical})')


print(ztest(speed_test, value=speed_h0, alternative='larger'))
