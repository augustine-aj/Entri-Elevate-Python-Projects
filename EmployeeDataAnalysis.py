import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/augus/Downloads/myexcel - myexcel.csv.csv")

df['height'] = np.random.randint(150, 181, df.shape[0])
print(df.info())

if df.isnull().values.any():
    df = df.dropna()

print("\nDataFrame info after dropping missing values:")
print(df.info())

team_distribution = df['Team'].value_counts()
percentage = (team_distribution / len(df)) * 100
print('\nTeam distribution.')
print(team_distribution)
print('\nTeam distribution percentage.\n', percentage)

position_distribution = df['Position'].value_counts()
print('\nPosition distribution.')
print(position_distribution)

age_group = pd.cut(df['Age'], bins=[18, 25, 35, 45, 55], right=True)
age_group_distribution = age_group.value_counts()
print('\nAge group.')
print(age_group)
print('\nAge group distribution.\n', age_group_distribution)

team_salary = df.groupby('Team')['Salary'].sum().idxmax()
position_salary = df.groupby('Position')['Salary'].sum().idxmax()
print('\nTeam salary.')
print(team_salary)
print('\nPosition salary.\n', position_salary)

correlation_age_salary = df['Age'].corr(df['Salary'])
print('\nCorrelation age salary.\n')
print(correlation_age_salary)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.countplot(x='Team', data=df)
plt.title('Distribution of employees across teams')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Position', data=df)
plt.title('Position distribution')
plt.show()


plt.figure(figsize=(10, 6))
age_group_distribution.plot(kind='bar')
plt.title('Predominant age group')
plt.xlabel('Age group')
plt.ylabel('No.of Employees')
plt.show()

plt.figure(figsize=(10, 6))
team_salary = df.groupby('Team')['Salary'].sum().sort_values()
team_salary.plot(kind='bar')
plt.title('Salary expenditure by team')
plt.ylabel('Total salary expenditure')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
team_salary = df.groupby('Position')['Salary'].sum().sort_values()
team_salary.plot(kind='bar')
plt.title('Salary expenditure by position')
plt.ylabel('Total salary expenditure')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title('Correlation between age and salary')
plt.show()