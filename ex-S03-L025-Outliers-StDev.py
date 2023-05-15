import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd


# import data
iris = datasets.load_iris()
X = iris.data[:, :2]  # take only the first two columns
y = iris.target
df = pd.DataFrame(X, columns=['sepal_l','sepal_w'])
df['species'] = iris.target

# scatter plot
plt.figure(2, figsize=(8, 6))
plt.scatter(df['sepal_l'], df['sepal_w'], c=df['species'], cmap=plt.cm.get_cmap('gist_rainbow'), label=df['species'])
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
#plt.colorbar()
plt.show()

df = df[df['species']==0]
print(df)

sepal_length_mean = df['sepal_l'].mean()
sepal_length_stdev = df['sepal_l'].std()
sepal_width_mean = df['sepal_w'].mean()
sepal_witdth_stdev = df['sepal_w'].std()

sepal_length_lower = sepal_length_mean - 2 * sepal_length_stdev
sepal_length_upper = sepal_length_mean + 2 * sepal_length_stdev
sepal_width_lower = sepal_width_mean - 2 * sepal_witdth_stdev
sepal_width_upper = sepal_width_mean + 2 * sepal_witdth_stdev

fig, axes = plt.subplots(nrows=1,ncols=2)
df.boxplot('sepal_l', ax = axes[0], meanline=True) 
df.boxplot('sepal_w', ax = axes[1], meanline=True) 
plt.show()

outliers = df.query(f"(sepal_l<{sepal_length_lower} or sepal_l>{sepal_length_upper}) or "+
                    f"(sepal_w<{sepal_width_lower} or sepal_w>{sepal_width_upper})") 
df.query(f"(sepal_l>={sepal_length_lower} and sepal_l<={sepal_length_upper}) and "+
         f"(sepal_w>={sepal_width_lower} and sepal_w<={sepal_width_upper})",inplace=True) 
print(outliers)

fig, axes = plt.subplots(nrows=1,ncols=2)
df.boxplot('sepal_l', ax = axes[0], meanline=True) 
df.boxplot('sepal_w', ax = axes[1], meanline=True) 
plt.show()


plt.scatter(df['sepal_l'], df['sepal_w'], color='blue')
plt.scatter(outliers['sepal_l'], outliers['sepal_w'], color='red')
plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sklearn import datasets
# import data
iris = datasets.load_iris()
X = iris.data[:, :2]  # take only the first two columns
y = iris.target
df = pd.DataFrame(X, columns=['sepal_l','sepal_w'])
df['species'] = iris.target
df = df[df['species']==0]


ransac = RANSACRegressor(estimator=LinearRegression(),
                         max_trials=100,
                         loss='squared_error', random_state=42,
                         residual_threshold=0.1)

ransac.fit(df['sepal_l'].to_numpy().reshape(-1,1), df['sepal_w'].to_numpy().reshape(-1,1))

inliers_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inliers_mask)

plt.scatter(df['sepal_l'][inliers_mask], df['sepal_w'][inliers_mask],
            c='blue', edgecolor='white', marker='o', label='Inliers')

plt.scatter(df['sepal_l'][outlier_mask], df['sepal_w'][outlier_mask],
             c='red', edgecolor='white', marker='s', label='Outliers')            

plt.show()
