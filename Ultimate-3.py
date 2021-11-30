#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import linear_model
import seaborn as sns

df= pd.read_csv(r"C:./Desktop/all_matches.csv")
df.head(10)


# In[2]:


df.isnull().sum()


# In[3]:


df.shape


# In[4]:


df.columns


# In[13]:


print('\n all teams : ',df['batting_team'].unique())


# In[7]:


df['wicket_type'].unique()


# In[27]:


wicketkeeper_stumped=df[df['wicket_type']=='stumped']['bowling_team'].value_counts().reset_index()
wicketkeeper_stumped.style.hide_index()
wicketkeeper_stumped


# In[34]:


wicketkeeper_stumped.rename(columns={'index':'Teams','bowling_team':'Total_stumping'},inplace=True)
wicketkeeper_stumped


# In[46]:


s1 =wicketkeeper_stumped.head(25)
s1.plot.bar(x="Teams")


# In[54]:


wicketkeeper_bowled=df[df['wicket_type']=='bowled']['bowling_team'].value_counts().reset_index()
wicketkeeper_bowled.style.hide_index()
wicketkeeper_bowled.rename(columns={'index':'Teams','bowling_team':'bowled'},inplace=True)
s2 =wicketkeeper_bowled.head(25)
s2.plot.bar(x="Teams")


# In[55]:


wicketkeeper_lbw=df[df['wicket_type']=='lbw']['bowling_team'].value_counts().reset_index()
wicketkeeper_lbw.style.hide_index()
wicketkeeper_lbw.rename(columns={'index':'Teams','bowling_team':'lbw'},inplace=True)
s2 =wicketkeeper_lbw.head(25)
s2.plot.bar(x="Teams")


# In[58]:


wicketkeeper_caught=df[df['wicket_type']=='caught']['bowling_team'].value_counts().reset_index()
wicketkeeper_caught.style.hide_index()
wicketkeeper_caught.rename(columns={'index':'Teams','bowling_team':'caught out'},inplace=True)
s2 =wicketkeeper_caught.head(25)
s2.plot.bar(x="Teams")


# In[59]:


wicketkeeper_caught1=df[df['wicket_type']=='caught and bowled']['bowling_team'].value_counts().reset_index()
wicketkeeper_caught1.style.hide_index()
wicketkeeper_caught1.rename(columns={'index':'Teams','bowling_team':'caught and bowled '},inplace=True)
s2 =wicketkeeper_caught1.head(25)
s2.plot.bar(x="Teams")


# In[68]:


#Fielding analysis
df['extras'].unique()


# In[70]:


wicketkeeper_caught1=df[df['wicket_type']=='run out']['bowling_team'].value_counts().reset_index()
wicketkeeper_caught1.style.hide_index()
wicketkeeper_caught1.rename(columns={'index':'Teams','bowling_team':'run out '},inplace=True)
s2 =wicketkeeper_caught1.head(25)
s2.plot.bar(x="Teams")


# In[110]:


df['wicket_type'].value_counts()


# In[87]:


runs = df.groupby(['striker'])['runs_off_bat'].sum().reset_index()
runs.columns=['Batsman','Runs']
y = runs.sort_values(by='Runs',ascending=False ).head(15)
y


# In[93]:


import seaborn as sns
ax = plt.axes()
sns.barplot(x=y['Batsman'],y=y['Runs'],palette='rocket',saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('\n Player')
plt.ylabel('Total Runs')
plt.title('Top Runs scorers')


# # season with most matches

# In[3]:


import pandas as pd
df1= pd.read_csv(r"C:./Desktop/all_season_summary.csv")
df1.head(5)


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot(x='season', data=df1)
plt.show()


# # Most successful ipl team

# In[8]:


data = df1.winner.value_counts()
sns.barplot(y = data.index, x = data, orient='h');


# # Number of matches in each venue

# In[20]:


import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv(r"C:./Desktop/all_matches.csv")
sns.countplot(y='venue', data=df)
plt.xticks(rotation=90)
plt.show()


# # Score distribution of each team by innings
# 

# In[24]:



runs = df.groupby(['match_id','innings','batting_team'])['runs_off_bat'].sum().reset_index()
runs


# In[25]:


runs.drop('match_id',axis=1,inplace=True)


# In[27]:


# For first innings
innings1 = runs[runs['innings']==1]
innings1.drop('innings',axis=1,inplace=True)
innings1


# In[30]:


plt.figure(figsize=(12,6))
sns.boxplot(y='batting_team',x='runs_off_bat',data=innings1, palette='rainbow');


# # For 2nd innings
# 

# In[32]:


innings2 = runs[runs['innings']==2]
innings2.drop('innings',axis=1,inplace=True)
plt.figure(figsize=(12,6))
sns.boxplot(data=innings2, y='batting_team', x='runs_off_bat', palette='rainbow')


# In[42]:


matches = pd.read_csv(r"C:./Desktop/all_season_summary.csv")
matches['home_team'].unique()


# In[47]:


def comparison(team1,team2):
    compare = matches[((matches['home_team']==team1) | (matches['away_team']==team1)) & ((matches['home_team']==team2) | (matches['away_team']==team2))]
    return sns.countplot(x='season',hue='winner',data=compare)


# In[48]:


plt.figure(figsize=(10,5))
comparison('Mumbai Indians','Chennai Super Kings')


# # Innings wise batting performance of each team in ipl (2008-21)

# In[9]:


import pandas as pd
import seaborn as sns
df= pd.read_csv(r"C:./Desktop/all_matches.csv")
d=df
d=d[['batting_team','innings','runs_off_bat']]
x=d.pivot_table(values='runs_off_bat',index='batting_team',columns='innings',aggfunc='count')
sns.heatmap(x,cmap='summer')


# In[10]:


import pandas as pd
import seaborn as sns
df= pd.read_csv(r"C:./Desktop/all_matches.csv")
d=df
d=d[['batting_team','season','runs_off_bat']]
x=d.pivot_table(values='runs_off_bat',index='batting_team',columns='season',aggfunc='count')
sns.heatmap(x,cmap='summer')


# In[ ]:




