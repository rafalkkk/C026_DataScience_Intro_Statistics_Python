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

print(df.describe())

fig, axes = plt.subplots(nrows=1,ncols=2)
df.boxplot('sepal_l', ax = axes[0], meanline=True) 
df.boxplot('sepal_w', ax = axes[1], meanline=True) 
plt.show()


Q1 = df['sepal_w'].quantile(0.25)
Q3 = df['sepal_w'].quantile(0.75)
IQR = Q3 - Q1
df = df[(Q1 - 1.5*IQR < df['sepal_w'])  &  (df['sepal_w'] < Q3 + 1.5*IQR)]

fig, axes = plt.subplots(nrows=1,ncols=2)
df.boxplot('sepal_l', ax = axes[0], meanline=True) 
df.boxplot('sepal_w', ax = axes[1], meanline=True) 
plt.show()
