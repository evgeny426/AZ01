import pandas as pd

# Задание 1
df = pd.read_csv('2019.csv')
print(df.head())
print(df)
print(df.info())
print(df.describe())

# Задание 2
df = pd.read_csv('dz.csv')

group = df.groupby('City')['Salary'].mean()
print(group)
