import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('Bestsellers with categories.csv')
print(df.head())

print(df.isnull().any())

ten_percent_division = df['Price'].quantile(0.1)
print(ten_percent_division)

q1= df['Price'].quantile(0.25)
q2= df['Price'].quantile(0.5)
q3= df['Price'].quantile(0.75)

print('quantiles for price are: ')
print('Q1: ', q1)
print('Q2: ', q2)
print('Q3: ', q3)

q1_user_rating = df['User Rating'].quantile(0.25)
q2_user_rating = df['User Rating'].quantile(0.5)
q3_user_rating = df['User Rating'].quantile(0.75)

print('quantiles for user rating are: ')
print('Q1: ', q1_user_rating)
print('Q2: ', q2_user_rating)
print('Q3: ', q3_user_rating)

plt.boxplot(df['Price'])
plt.title('Boxplot of Price')
plt.show()

plt.boxplot(df['User Rating'])
plt.title('Boxplot of User Rating')
plt.show()