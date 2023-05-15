import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

houses = pd.read_csv("./datasets/housing/Housing.csv")

print(houses.head(5))
print(houses.columns)
print(len(houses))

print('Covariance between number of bathrooms and price')
print(houses["bathrooms"].cov(houses["price"]))

print('Correlation between number of bathrooms and price')
print(houses["bathrooms"].corr(houses["price"]))

covariance_tab = houses.cov(numeric_only=True)
print("Covariance table")
print(covariance_tab)

correlation_tab = houses.corr(numeric_only=True)
print('Correlation table')
print(correlation_tab)

# https://seaborn.pydata.org/generated/seaborn.heatmap.html
# https://seaborn.pydata.org/tutorial/color_palettes.html
sns.heatmap(correlation_tab, cmap="Spectral", annot=True)
plt.show()
