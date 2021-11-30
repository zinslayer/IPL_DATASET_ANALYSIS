#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import linear_model
import seaborn as sns
df= pd.read_csv(r"C:./Desktop/all_matches.csv")
df.head(5)


# In[2]:


df.isnull().sum()


# In[3]:


df.shape


# In[4]:


df.columns


# In[5]:


print('\n all teams : ',df['batting_team'].unique())


# In[6]:


df['wicket_type'].unique()


# In[6]:


runs = df.groupby(['striker'])['runs_off_bat'].sum().reset_index()
runs.columns=['Batsman','Runs']
y = runs.sort_values(by='Runs',ascending=False ).head(15)
y


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns
ax = plt.axes()
sns.barplot(x=y['Batsman'],y=y['Runs'],palette='rocket',saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('\n Player')
plt.ylabel('Total Runs')
plt.title('Top Runs scorers')
plt.savefig('kk.png')


# In[9]:


player=(df['striker']=='V Kohli')
df_kohli=df[player]
df_kohli.head()


# In[10]:


df_kohli['wicket_type'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(14,8),shadow=True,rotatelabels=True)
plt.title('wicket type')
plt.show()
plt.savefig('kk1.png')


# In[14]:


def count(df_kohli,runs):
    return len(df_kohli[df_kohli[ 'runs_off_bat']==runs])*runs
print("Runs scored from 1's:",count(df_kohli,1))
print("Runs scored from 2's:",count(df_kohli,2))
print("Runs scored from 3's:",count(df_kohli,3))
print("Runs scored from 4's:",count(df_kohli,4))
print("Runs scored from 6's:",count(df_kohli,6))


# In[15]:


team=(df['batting_team']=='Royal Challengers Bangalore')
df_rcb=df[team]
df_rcb.head()


# In[17]:


df_rcb['wicket_type'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(16,10),shadow=True,rotatelabels=True)
plt.title('wicket type')
plt.show()


# In[18]:


bowling_wicket=df[df['bowling_team']=='Royal Challengers Bangalore']['wicket_type'].value_counts().reset_index()
bowling_wicket.style.hide_index()
bowling_wicket.rename(columns={'index':'Teams','bowling_team':'run out '},inplace=True)
s2 =bowling_wicket.head(25)
s2.plot.bar(x="Teams")


# In[21]:


batting_wicket=df[df['batting_team']=='Royal Challengers Bangalore']['wicket_type'].value_counts().reset_index()
batting_wicket.style.hide_index()
batting_wicket.rename(columns={'index':'Teams','batting_team':'run out '},inplace=True)
s2 =batting_wicket.head(25)
s2.plot.bar(x="Teams")


# In[22]:


runs1 = df.groupby(['batting_team'])['runs_off_bat'].sum().reset_index()
runs1.columns=['Batting team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(20)
y


# In[26]:


ax = plt.axes()
sns.barplot(x=y['Batting team'],y=y['Runs'],palette='rocket',saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('\n All teams')
plt.ylabel('Total Runs')
plt.title('Total Runs scored by all Teams')


# In[25]:


runs2 = df_rcb.groupby(['striker'])['runs_off_bat'].sum().reset_index()
runs2.columns=['Rcb Batsman','Runs']
y3 = runs2.sort_values(by='Runs',ascending=False ).head(20)
y3.plot.bar('Rcb Batsman','Runs')


# In[ ]:


team=(df['batting_team']=='Royal Challengers Bangalore')
df_rcb=df[team]
df_rcb.head()


# In[40]:


df_upto2020= pd.read_csv(r"C:./Desktop/all_season_summary.csv")
df_upto2020.head(5)


# In[47]:


temp=pd.DataFrame({'winner':df_upto2020['winner']})
count_wins=temp.value_counts()
#print(count_wins)
labels=[X[0]for X in count_wins.keys()]
bar,ax =plt.subplots(figsize=(20,12))
ax=plt.pie(x=count_wins,autopct='%.1f%%',labels=labels)
plt.title('Most Wins',fontsize=17)


# In[51]:


### Wins of RCB in different season
rcb_wins=df_upto2020[df_upto2020['winner']=='Royal Challengers Bangalore']['season'].value_counts().reset_index()
rcb_wins.rename(columns={'index':'Years'},inplace=True)
s9 =rcb_wins.head(25)
s9.plot.bar(x="Years")


# # Analysis of rcb in 2021

# In[ ]:


df= pd.read_csv(r"C:./Desktop/all_matches.csv")
rcb=(df['season']=='2021')
df_rcb0=df[rcb]
df_rcb0.head()


# In[82]:


#Analysis of rcb in 2021
dfk= pd.read_csv(r"C:./Desktop/ALL_2021_IPL_MATCHES_BALL_BY_BALL.csv")
dfk


# In[84]:


aruns = dfk.groupby(['batsman'])['batsman_run'].sum().reset_index()
aruns.columns=['Batsman','Runs']
y10 = aruns.sort_values(by='Runs',ascending=False ).head(15)
y10


# In[86]:


y10.plot.bar(x="Batsman")


# In[93]:


rcb_wins1=dfk[dfk['batting_team']=='Royal Challengers Bangalore']['batsman_run'].value_counts().reset_index()
rcb_wins1.rename(columns={'index':'Types of runs'},inplace=True)
s9 =rcb_wins1.head(25)
s9.plot.bar(x="Types of runs")


# In[136]:


#When rcb bowls
rcb_wins4=dfk[dfk['bowling_team']=='Royal Challengers Bangalore']['batsman_run'].value_counts().reset_index()
rcb_wins4.rename(columns={'index':'Types of runs'},inplace=True)
s9 =rcb_wins4.head(25)
s9.plot.bar(x="Types of runs")


# In[99]:


rcb=(df['batting_team']=='Royal Challengers Bangalore')
df_rcb0=df[rcb]
df_rcb0.head()


# In[118]:


rcb_wins2=dfk[dfk['bowling_team']=='Royal Challengers Bangalore']['player_out'].value_counts().reset_index()
rcb_wins2.rename(columns={'index':'Batsman out'},inplace=True)
s12 =rcb_wins2.head(30)
s12.plot.bar(x="Batsman out")


# In[135]:



temp1=pd.DataFrame({'player_out':dfk['player_out']})
count_outs=temp1.value_counts()
s13 =count_outs.head(15)
s13.plot.bar()


# In[3]:


import pandas as pd
delivery = pd.read_csv(r"C:./Desktop/ALL_2021_IPL_MATCHES_BALL_BY_BALL.csv")
sub_data11 = delivery.loc[:, ['batsman', 'batsman_run']]
sub_data = sub_data11.groupby('batsman', as_index = False).sum()
sub_data = sub_data.sort_values(by=['batsman_run'], ascending = False)
batsman = sub_data['batsman'].tolist()
runs = sub_data['batsman_run'].tolist()


# In[5]:


sub_data14 = delivery.loc[:, ['batsman', 'bowler', 'elimination_kind']]
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


# In[14]:


d13 = {'Player':bowler,'Wickets':wickets}
d23 = {'Player':batsman,'Runs':runs}
df13 = pd.DataFrame(d13)
df23 = pd.DataFrame(d23)
dff=df13.head(10)
dff


# In[17]:


dff.plot.bar(x='Player')


# In[20]:


sub_data14 = delivery.loc[:, ['batsman', 'bowling_team', 'elimination_kind']]
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


# In[22]:


d1 = {'Teams':bowler,'Wickets':wickets}
d2 = {'Teams':batsman,'Runs':runs}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
df1


# In[23]:


df1.plot.bar(x='Teams')#total wickets by each team in 2021


# In[28]:


import pandas as pd
df = pd.read_csv(r"C:./Desktop/ALL_2021_IPL_MATCHES_BALL_BY_BALL.csv")
rcb=(df['batting_team']=='Royal Challengers Bangalore')
df_rcb0=df[rcb]

delivery1 =df_rcb0
sub_data12 = delivery1.loc[:, ['batsman', 'batsman_run']]
sub_data = sub_data12.groupby('batsman', as_index = False).sum()
sub_data = sub_data.sort_values(by=['batsman_run'], ascending = False)
batsman = sub_data['batsman'].tolist()
runs = sub_data['batsman_run'].tolist()


# In[29]:


sub_data14 = delivery1.loc[:, ['batsman', 'bowler', 'elimination_kind']]
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


# In[47]:


d17 = {'Bowlers_aganist_rcb':bowler,'Wickets':wickets}
d27 = {'Rcb batsman':batsman,'Runs':runs}
df17 = pd.DataFrame(d1)
df27 = pd.DataFrame(d2)
df17
dfg=df17.head(10)
dfg.plot.bar(x='Teams')
dfh=df27.head(10)
dfh.plot.bar(x='Teams')


# # CSK 2020 & 2021

# # 2020 overall

# In[50]:



df= pd.read_csv(r"C:./Desktop/all_matches.csv")
csk=(df['season']=='2020/21')
df_csk0=df[csk]
df_csk0.head()


# In[51]:


runs1 = df_csk0.groupby(['batting_team'])['runs_off_bat'].sum().reset_index()
runs1.columns=['Batting team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(20)
y


# In[54]:


import matplotlib.pyplot as plt
import seaborn as sns
ax = plt.axes()
sns.barplot(x=y['Batting team'],y=y['Runs'],palette='rocket',saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('\n All teams')
plt.ylabel('Total Runs')
plt.title('Total Runs scored by all Teams in 2020')


# In[64]:


#top 10 run scorers in 2020 
runs1 = df_csk0.groupby(['striker'])['runs_off_bat'].sum().reset_index()
runs1.columns=['striker','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='striker')


# In[67]:


sub_data14 = df_csk0.loc[:, ['striker', 'bowler', 'wicket_type']]
dismissal_kinds = ['caught',
 'bowled',
 'run out',
 'lbw',
 'caught and bowled',
 'stumped',
 'hit wicket']
is_bowler = (sub_data14['wicket_type'] == 'bowled') | (sub_data14['wicket_type'] == 'caught') | (sub_data14['wicket_type'] == 'caught and bowled') | (sub_data14['wicket_type'] == 'stumped') | (sub_data14['wicket_type'] == 'lbw') | (sub_data14['wicket_type'] == 'hit wicket')
bowler_data = sub_data14[is_bowler].loc[:, ['bowler']]
bowler = bowler_data['bowler'].value_counts().keys().tolist()
wickets = bowler_data['bowler'].value_counts().tolist()


# In[72]:


d1 = {'Bowlers':bowler,'Wickets':wickets}
d2 = {'Bowlers':batsman,'Runs':runs}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
df1
dfg=df1.head(10)
dfg.plot.bar(x='Bowlers')


# In[74]:


sub_data14 = df_csk0.loc[:, ['striker', 'bowling_team', 'wicket_type']]
dismissal_kinds = ['caught',
 'bowled',
 'run out',
 'lbw',
 'caught and bowled',
 'stumped',
 'hit wicket']
is_bowler = (sub_data14['wicket_type'] == 'bowled') | (sub_data14['wicket_type'] == 'caught') | (sub_data14['wicket_type'] == 'caught and bowled') | (sub_data14['wicket_type'] == 'stumped') | (sub_data14['wicket_type'] == 'lbw') | (sub_data14['wicket_type'] == 'hit wicket')
bowler_data = sub_data14[is_bowler].loc[:, ['bowling_team']]
bowler = bowler_data['bowling_team'].value_counts().keys().tolist()
wickets = bowler_data['bowling_team'].value_counts().tolist()


# In[78]:


d1 = {'bowling_team':bowler,'Wickets':wickets}
df1 = pd.DataFrame(d1)
dfg=df1.head(10)
dfg.plot.bar(x='bowling_team')


# In[81]:


##Most runs concieved
runs1 = df_csk0.groupby(['bowling_team'])['runs_off_bat'].sum().reset_index()
runs1.columns=['Bowling team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(20)
y#runs against all teams
y.plot.bar(x='Bowling team')


# In[82]:


runs1 = df_csk0.groupby(['bowling_team'])['extras'].sum().reset_index()
runs1.columns=['Bowling team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(20)
y#top extras by all teams
y.plot.bar(x='Bowling team')


# In[92]:


def barplot(x_axis, y_axis, plot_data, title, x_label, y_label):
    """Bar plot using seaborn library"""
    plot = sns.barplot(x=x_axis, y=y_axis, data=plot_data)
    plot.set(xlabel=x_label, ylabel=y_label)
    plot.set_title(title)
    plt.xticks(rotation=90)
    plt.show()
    #number of 4s and 6s scored boundaries scored in each season
boundaries_per_season = df_csk0[(df_csk0['runs_off_bat']==4) | (df_csk0['runs_off_bat']==6)].groupby(['batting_team'])['runs_off_bat'].count().reset_index()
#barplot
barplot('batting_team', 'runs_off_bat', boundaries_per_season, 'Number of boundaries scored in 2020',
        'batting_team', 'Number of Boundaries')


# # As a batting team CSK performance in 2020

# In[105]:


df= pd.read_csv(r"C:./Desktop/all_matches.csv")
csk=(df['season']=='2020/21')
df_csk9=df[csk]

cskb=(df_csk9['batting_team']=='Chennai Super Kings')
df_csk10=df_csk9[cskb]
df_csk10.head()# matches by csk in 2020 as batting team


# In[106]:


#top 10 run scorers in 2020 
runs1 = df_csk10.groupby(['striker'])['runs_off_bat'].sum().reset_index()
runs1.columns=['striker','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='striker')


# In[111]:


#Most wickets against teams
sub_data14 = df_csk10.loc[:, ['striker', 'bowling_team', 'wicket_type']]
dismissal_kinds = ['caught',
 'bowled',
 'run out',
 'lbw',
 'caught and bowled',
 'stumped',
 'hit wicket']
is_bowler = (sub_data14['wicket_type'] == 'bowled') | (sub_data14['wicket_type'] == 'caught') | (sub_data14['wicket_type'] == 'caught and bowled') | (sub_data14['wicket_type'] == 'stumped') | (sub_data14['wicket_type'] == 'lbw') | (sub_data14['wicket_type'] == 'hit wicket')
bowler_data = sub_data14[is_bowler].loc[:, ['bowling_team']]
bowler = bowler_data['bowling_team'].value_counts().keys().tolist()
wickets = bowler_data['bowling_team'].value_counts().tolist()
d1 = {'bowling_team':bowler,'Wickets':wickets}
df1 = pd.DataFrame(d1)
dfg=df1.head(10)
dfg.plot.bar(x='bowling_team')


# In[112]:


#top runs by csk  in 2020
runs1 = df_csk10.groupby(['bowling_team'])['runs_off_bat'].sum().reset_index()
runs1.columns=['bowling_team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='bowling_team')


# In[115]:


def barplot(x_axis, y_axis, plot_data, title, x_label, y_label):
    """Bar plot using seaborn library"""
    plot = sns.barplot(x=x_axis, y=y_axis, data=plot_data)
    plot.set(xlabel=x_label, ylabel=y_label)
    plot.set_title(title)
    plt.xticks(rotation=90)
    plt.show()
    #number of 4s and 6s scored boundaries scored in each season
boundaries_per_season = df_csk10[(df_csk10['runs_off_bat']==4) | (df_csk10['runs_off_bat']==6)].groupby(['bowling_team'])['runs_off_bat'].count().reset_index()
#barplot
barplot('bowling_team', 'runs_off_bat', boundaries_per_season, 'Number of boundaries scored in 2020 by CSK',
        'bowling_team', 'Number of Boundaries')


# In[117]:


#batsman are out by wicket types-
df_csk10['wicket_type'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(14,8),shadow=True,rotatelabels=True)
plt.title('wicket type')
plt.show()


# # As a bowling team CSK in 2020

# In[119]:


df= pd.read_csv(r"C:./Desktop/all_matches.csv")
csk=(df['season']=='2020/21')
df_csk9=df[csk]

cskb=(df_csk9['bowling_team']=='Chennai Super Kings')
df_csk11=df_csk9[cskb]
df_csk11.head()# matches by csk in 2020 as bowling team


# In[120]:


#top 10 run scorers against csk in 2020 
runs1 = df_csk11.groupby(['striker'])['runs_off_bat'].sum().reset_index()
runs1.columns=['striker','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='striker')


# In[121]:


#top runs by teams against csk in 2020 
runs1 = df_csk10.groupby(['batting_team'])['runs_off_bat'].sum().reset_index()
runs1.columns=['batting_team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='batting_team')


# In[123]:


#Most wickets takers
sub_data14 = df_csk11.loc[:, ['striker', 'bowler', 'wicket_type']]
dismissal_kinds = ['caught',
 'bowled',
 'run out',
 'lbw',
 'caught and bowled',
 'stumped',
 'hit wicket']
is_bowler = (sub_data14['wicket_type'] == 'bowled') | (sub_data14['wicket_type'] == 'caught') | (sub_data14['wicket_type'] == 'caught and bowled') | (sub_data14['wicket_type'] == 'stumped') | (sub_data14['wicket_type'] == 'lbw') | (sub_data14['wicket_type'] == 'hit wicket')
bowler_data = sub_data14[is_bowler].loc[:, ['bowler']]
bowler = bowler_data['bowler'].value_counts().keys().tolist()
wickets = bowler_data['bowler'].value_counts().tolist()
d1 = {'bowler':bowler,'Wickets':wickets}
df1 = pd.DataFrame(d1)
dfg=df1.head(10)
dfg.plot.bar(x='bowler')


# In[125]:


#most extras by csk
runs1 = df_csk11.groupby(['batting_team'])['extras'].sum().reset_index()
runs1.columns=['batting_team','Runs']
y = runs1.sort_values(by='Runs',ascending=False ).head(10)
y.plot.bar(x='batting_team')


# In[126]:


#Wickets by csk bowlers
df_csk11['wicket_type'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(14,8),shadow=True,rotatelabels=True)
plt.title('wicket type')
plt.show()


# # overall 2021

# In[ ]:




