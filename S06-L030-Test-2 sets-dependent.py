import scipy.stats as stats
import pandas as pd
import math


# Two dependent values (pills)

# H1:  mean before < mean after
# H0:  mean before >= mean after

# H1:  mean before - mean after < 0
# H0 - mean before - mean after >= 0


size = 30
results_before = stats.norm.rvs(size=size, loc=14, scale=1)
change = stats.norm.rvs(size=size, loc=0.2, scale=0.5)
results_after = [x+y for (x,y) in zip(results_before, change)]

df = pd.DataFrame(list(zip(results_before, results_after)), columns=['before', 'after'])
df['diff'] = df['after'] - df['before']
print(df)

print('Before:',df['before'].mean(),df['before'].std())
print('After:', df['after'].mean(), df['after'].std())
print('Difference:', df['diff'].mean(), df['diff'].std())

# alpha = 0.05
# confidence level = 1 - alpha = 0.95
# T-critical (degree of freedom = 29, alpha = 0.05) = 1,699

alpha = 0.05
sample_size = len(df)
sample_mean = df['diff'].mean()
sample_stdev = df['diff'].std()
confidence_level = 1-alpha

t_critical = stats.t.ppf(q=confidence_level, df=sample_size-1)  #1.699
t_score = (sample_mean - 0)/(sample_stdev/math.sqrt(sample_size))
print(f't-critical = {t_critical}, T-score = {t_score}')

if t_critical < t_score:
    print('We reject H0')
else:
    print('We accept H0')


from statsmodels.stats.weightstats import ztest
test_stat, p_value = ztest(df["before"], df["after"], value=0, alternative='larger')
print(f'Z-test (p-value) = { p_value }')

if p_value < alpha:
    print('H0 is rejected')
else:
    print('H0 is accepted')
