# https://dataverse.harvard.edu/dataverse/r4r

import pandas as pd
from matplotlib import pyplot as plt

blood = pd.read_csv('./datasets/blood_pressure.csv', 
                    usecols=['DayofWk', 'Meal_Time', 'Sys(mmHg)','Pulse(bpm)'])

# plt.hist(blood['Sys(mmHg)'], bins=9)
# plt.title('Blood presure')
# plt.show()

# breakfast = blood.query('Meal_Time == "Breakfast"')

# plt.hist(breakfast['Sys(mmHg)'], bins=9)
# plt.title('Breakfast')
# plt.show()

# lunch = blood.query('Meal_Time == "Lunch"')

# plt.hist(lunch['Sys(mmHg)'], bins=9)
# plt.title('Lunch')
# plt.show()

# dinner = blood.query('Meal_Time == "Dinner"')

# plt.hist(dinner['Sys(mmHg)'], bins=9)
# plt.title('Dinner')
# plt.show()

# snacks = blood.query('Meal_Time == "Snacks"')

# plt.hist(snacks['Sys(mmHg)'], bins=9)
# plt.title('Snacks')
# plt.show()

blood_mean = blood['Sys(mmHg)'].mean()
blood_stdev = blood['Sys(mmHg)'].std()
blood["sys-z-score"] = (blood['Sys(mmHg)'] - blood_mean) / blood_stdev
# plt.hist(blood['sys-z-score'], bins=9)
# plt.show()

sys_z_score_mean = blood['sys-z-score'].mean()
sys_z_score_stdev = blood['sys-z-score'].std()

print(sys_z_score_mean, sys_z_score_stdev)