#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import linear_model
import seaborn as sns
dfk= pd.read_csv(r"C:./Desktop/ALL_2021_IPL_MATCHES_BALL_BY_BALL.csv")
dfk


# In[5]:


aruns = dfk.groupby(['batting_team'])['batsman_run'].sum().reset_index()
aruns.columns=['batting team','Runs']
y10 = aruns.sort_values(by='Runs',ascending=False ).head(15)
y10
y10.plot.bar(x="batting team")


# In[6]:


aruns = dfk.groupby(['batsman'])['batsman_run'].sum().reset_index()
aruns.columns=['batsman','Runs']
y10 = aruns.sort_values(by='Runs',ascending=False ).head(15)
y10
y10.plot.bar(x="batsman")


# In[10]:


sub_data14 = dfk.loc[:, ['batsman', 'bowler', 'elimination_kind']]
dismissal_kinds = ['caught',
 'bowled',
 'run out',
 'lbw',
 'caught and bowled',
 'stumped',
 'hit wicket']
is_bowler = (sub_data14['elimination_kind'] == 'bowled') | (sub_data14['elimination_kind'] == 'caught') | (sub_data14['elimination_kind'] == 'caught and bowled') | (sub_data14['elimination_kind'] == 'stumped') | (sub_data14['elimination_kind'] == 'lbw') | (sub_data14['elimination_kind'] == 'hit wicket')
bowler_data = sub_data14[is_bowler].loc[:, ['bowler']]
bowler = bowler_data['bowler'].value_counts().keys().tolist()
wickets = bowler_data['bowler'].value_counts().tolist()


# In[12]:


d1 = {'Bowlers':bowler,'Wickets':wickets}
df1 = pd.DataFrame(d1)
df1
dfg=df1.head(10)
dfg.plot.bar(x='Bowlers')


# In[13]:


sub_data14 = dfk.loc[:, ['batsman', 'bowling_team', 'elimination_kind']]
dismissal_kinds = ['caught',
 'bowled',
 'run out',
 'lbw',
 'caught and bowled',
 'stumped',
 'hit wicket']
is_bowler = (sub_data14['elimination_kind'] == 'bowled') | (sub_data14['elimination_kind'] == 'caught') | (sub_data14['elimination_kind'] == 'caught and bowled') | (sub_data14['elimination_kind'] == 'stumped') | (sub_data14['elimination_kind'] == 'lbw') | (sub_data14['elimination_kind'] == 'hit wicket')
bowler_data = sub_data14[is_bowler].loc[:, ['bowling_team']]
bowler = bowler_data['bowling_team'].value_counts().keys().tolist()
wickets = bowler_data['bowling_team'].value_counts().tolist()


# In[16]:


d1 = {'Bowlers':bowler,'Wickets':wickets}
df1 = pd.DataFrame(d1)
df1
dfg=df1.head(10)
dfg.plot.bar(x='Bowlers')


# In[18]:


#Most runs concieved
runs1 = dfk.groupby(['bowling_team'])['total_runs'].sum().reset_index()
runs1.columns=['Bowling team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(20)
y#runs against all teams
y.plot.bar(x='Bowling team')


# In[20]:


runs1 = dfk.groupby(['bowling_team'])['extra_runs'].sum().reset_index()
runs1.columns=['Bowling team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(20)
y#top extras by all teams
y.plot.bar(x='Bowling team')


# In[21]:


def barplot(x_axis, y_axis, plot_data, title, x_label, y_label):
    """Bar plot using seaborn library"""
    plot = sns.barplot(x=x_axis, y=y_axis, data=plot_data)
    plot.set(xlabel=x_label, ylabel=y_label)
    plot.set_title(title)
    plt.xticks(rotation=90)
    plt.show()
    #number of 4s and 6s scored boundaries scored in each season
boundaries_per_season = dfk[(dfk['batsman_run']==4) | (dfk['batsman_run']==6)].groupby(['batting_team'])['batsman_run'].count().reset_index()
#barplot
barplot('batting_team', 'batsman_run', boundaries_per_season, 'Number of boundaries scored in 2021',
        'batting_team', 'Number of Boundaries')


# # As a batting team csk in 2021

# In[22]:




cskb=(dfk['batting_team']=='Chennai Super Kings')
df_csk10=dfk[cskb]
df_csk10.head()# matches by csk in 2020 as batting team


# In[23]:


#top 10 run scorers in 2021 
runs1 = df_csk10.groupby(['batsman'])['batsman_run'].sum().reset_index()
runs1.columns=['striker','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='striker')


# In[26]:


#Most wickets by against team
sub_data14 = df_csk10.loc[:, ['batsman', 'bowling_team', 'elimination_kind']]
dismissal_kinds = ['caught',
 'bowled',
 'run out',
 'lbw',
 'caught and bowled',
 'stumped',
 'hit wicket']
is_bowler = (sub_data14['elimination_kind'] == 'bowled') | (sub_data14['elimination_kind'] == 'caught') | (sub_data14['elimination_kind'] == 'caught and bowled') | (sub_data14['elimination_kind'] == 'stumped') | (sub_data14['elimination_kind'] == 'lbw') | (sub_data14['elimination_kind'] == 'hit wicket')
bowler_data = sub_data14[is_bowler].loc[:, ['bowling_team']]
bowler = bowler_data['bowling_team'].value_counts().keys().tolist()
wickets = bowler_data['bowling_team'].value_counts().tolist()


# In[27]:


d1 = {'bowling_team':bowler,'Wickets':wickets}
df1 = pd.DataFrame(d1)
dfg=df1.head(10)
dfg.plot.bar(x='bowling_team')


# In[28]:


#top runs by csk  in 2020
runs1 = df_csk10.groupby(['bowling_team'])['batsman_run'].sum().reset_index()
runs1.columns=['bowling_team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='bowling_team')


# In[30]:


def barplot(x_axis, y_axis, plot_data, title, x_label, y_label):
    """Bar plot using seaborn library"""
    plot = sns.barplot(x=x_axis, y=y_axis, data=plot_data)
    plot.set(xlabel=x_label, ylabel=y_label)
    plot.set_title(title)
    plt.xticks(rotation=90)
    plt.show()
    #number of 4s and 6s scored boundaries scored in each season
boundaries_per_season = df_csk10[(df_csk10['batsman_run']==4) | (df_csk10['batsman_run']==6)].groupby(['bowling_team'])['batsman_run'].count().reset_index()
#barplot
barplot('bowling_team', 'batsman_run', boundaries_per_season, 'Number of boundaries scored in 2021 by CSK',
        'bowling_team', 'Number of Boundaries')


# In[32]:


#batsman are out by wicket types-
df_csk10['elimination_kind'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(14,8),shadow=True,rotatelabels=True)
plt.title('elimination_kind')
plt.show()


# # As a bowling team CSK in 2021

# In[35]:


cskb=(dfk['bowling_team']=='Chennai Super Kings')
df_csk11=dfk[cskb]
df_csk11.head()


# In[36]:


#top 10 run scorers against csk in 2021 
runs1 = df_csk11.groupby(['batsman'])['batsman_run'].sum().reset_index()
runs1.columns=['striker','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='striker')


# In[37]:


#top runs by teams against csk in 2020 
runs1 = df_csk11.groupby(['batting_team'])['batsman_run'].sum().reset_index()
runs1.columns=['batting_team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='batting_team')


# In[39]:


#Most wickets takers
sub_data14 = df_csk11.loc[:, ['batsman', 'bowler', 'elimination_kind']]
dismissal_kinds = ['caught',
 'bowled',
 'run out',
 'lbw',
 'caught and bowled',
 'stumped',
 'hit wicket']
is_bowler = (sub_data14['elimination_kind'] == 'bowled') | (sub_data14['elimination_kind'] == 'caught') | (sub_data14['elimination_kind'] == 'caught and bowled') | (sub_data14['elimination_kind'] == 'stumped') | (sub_data14['elimination_kind'] == 'lbw') | (sub_data14['elimination_kind'] == 'hit wicket')
bowler_data = sub_data14[is_bowler].loc[:, ['bowler']]
bowler = bowler_data['bowler'].value_counts().keys().tolist()
wickets = bowler_data['bowler'].value_counts().tolist()
d1 = {'bowler':bowler,'Wickets':wickets}
df1 = pd.DataFrame(d1)
dfg=df1.head(10)
dfg.plot.bar(x='bowler')


# In[41]:


#most extras by csk
runs1 = df_csk11.groupby(['batting_team'])['extra_runs'].sum().reset_index()
runs1.columns=['batting_team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='batting_team')


# In[42]:


#Wickets by csk bowlers
df_csk11['elimination_kind'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(14,8),shadow=True,rotatelabels=True)
plt.title('wicket type')
plt.show()


# In[ ]:




