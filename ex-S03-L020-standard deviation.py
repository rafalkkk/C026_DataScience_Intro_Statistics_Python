import random as r
import statistics as stat
import math
import pandas as pd

my_list = [r.randint(0,100) for i in range(200)]

my_list_1 = [i + 2 for i in my_list]
my_list_2 = [i * 2 for i in my_list]
my_list_3 = [i * 2 + 2 for i in my_list]
my_list_4 = [math.sqrt(i) for i in my_list]

df = pd.DataFrame(columns=["List", "Variance", "Stdev","Coefficient of variation"])
df.loc[len(df)] = ['my_list', stat.pvariance(my_list),   
                   stat.stdev(my_list), stat.stdev(my_list)/stat.mean(my_list)]
df.loc[len(df)] = ['my_list + 2', stat.pvariance(my_list_1), 
                   stat.stdev(my_list_1), stat.stdev(my_list_1)/stat.mean(my_list_1)]
df.loc[len(df)] = ['my_list * 2', stat.pvariance(my_list_2), stat.stdev(my_list_2), 
                   stat.stdev(my_list_2)/stat.mean(my_list_2)]
df.loc[len(df)] = ['my_list * 2 + 2', stat.pvariance(my_list_3), 
                   stat.stdev(my_list_3), stat.stdev(my_list_3)/stat.mean(my_list_3)]
df.loc[len(df)] = ['sqrt my_list', stat.pvariance(my_list_4), 
                   stat.stdev(my_list_4), stat.stdev(my_list_4)/stat.mean(my_list_4)]
print(df)
