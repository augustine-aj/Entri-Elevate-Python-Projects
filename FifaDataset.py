import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/augus/Downloads/fifa_data.csv")


# Which country has the most number of players

country_name = df['Nationality'].value_counts().idxmax()
print(country_name)


# Plot a bar chart of 5 top countries with the most number of players.

country_list = df['Nationality'].value_counts().nlargest(5)

plt.figure(figsize=(10, 6))
country_list.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('No.of players')
plt.title('Top 5 countries with players')
plt.xticks(rotation=0)

plt.show()


# Which player has the highest salary

df['Wage'] = df['Wage'].str.replace('€', '').str.replace('K', '000').str.replace('M', '000000').astype(float)
highest_salary = df.loc[df['Wage'].idxmax(), ['Wage', 'Name']]

print('\nplayer with highest salary :\n', highest_salary)


# Plot a histogram to get the salary range of the players.

plt.figure(figsize=(10, 6))
plt.hist(df['Wage'], color='skyblue')
plt.xlabel('Wages')
plt.ylabel('No.of players')
plt.title('Wages of players')

plt.show()


# Who is the tallest player in the fifa

df['Height'] = df['Height'].str.replace("'", '.').astype(float)
tallest_player = df.loc[df['Height'].idxmax(), ['Name', 'Height']]
print(f"\nThe tallest player is : {tallest_player['Name']}, And his height is : {tallest_player['Height']}")


# Which club has the most number of players

players_club = df['Club'].value_counts().idxmax()
print('\nThe club has most most players is : ', players_club)


# Which foot is most preferred by the players?Draw a bar chart for preferred foot

preferable_foot = df['Preferred Foot'].value_counts().idxmax()
print('\nThe preferred foot by most players is : ', preferable_foot)

