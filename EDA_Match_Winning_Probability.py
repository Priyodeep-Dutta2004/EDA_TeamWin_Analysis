import pandas as pd
x=pd.read_csv('C:\\Users\chott\Downloads\FifaDataset.csv')
#print(x.to_string())
print(x.info())


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.express as px

#Step1: Data preprocesssing(Loading of data)
x=pd.read_csv('C:\\Users\chott\Downloads\FifaDataset.csv')
#print(x.info())

#Data type conversion
#x[['Overall','Potential']]=x[['Overall','Potential']].astype('float64')

#Data cleaning(dropping rows with missing value & filling an empty cell with some value )
'''x['Club'].fillna("Not Known",inplace=True)
y=x.drop(['Loaned from'],axis=1)
#print(y.tail(50))
print(y)
'''

#Step2: Exploratory data analysis
#Calculation of summary statistics
'''average_score=x['Potential'].mean()
team_rankings=x.groupby('Club')['Overall'].sum().sort_values(ascending=False)
#Visualization of team-rankings
plt.figure(figsize=(10, 6))
sn.barplot(x=team_rankings.index, y=team_rankings.values)
plt.xlabel('Team')
plt.ylabel('Points')
plt.title('Team Rankings')
plt.xticks(rotation=90)
plt.show()
'''

#Step3: Player Analysis
#Analyzing player performance using individual player statistics
'''player_stats = x.groupby('Name')[['Dribbling','Stamina','Skill Moves','Finishing']].mean()
plt.figure(figsize=(8, 6))
categories = list(player_stats)
values = player_stats.loc['L. Messi'].values.tolist()
values += values[:1] # Repeat the first value to close the circle
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]
plt.polar(angles, values)
plt.fill(angles, values, alpha=0.25)
plt.xticks(angles[:-1], categories)
plt.title('Player Performance Comparison(L.Messi)')
plt.show()
'''

#Top performer and player with potential for improvement
'''top_play=x[['Name','Overall','Dribbling','Club','Potential']]
top_play.sort_values(by='Overall',ascending=False,inplace=True)
top_30_play=top_play[:100]
fig=px.scatter(top_30_play,x='Name',y='Overall',color='Potential',size='Overall',hover_data=['Name','Club','Potential'],title='Top Football Players in the FIFA 21 ')
fig.show()
'''

#Step5: Game analysis
#Analysisng game outcome and game specific statistics
game_outcomes = x['Value'].value_counts()
club=x['Club'].value_counts()
z= club.head(10)
y= game_outcomes.head(10)
# Visualize game outcomes using pie chart
plt.figure(figsize=(6,6))
plt.pie(z.values, labels=z.index, autopct='%1.1f%%')
plt.title('Game Outcomes of top 10 clubs')
plt.show()


