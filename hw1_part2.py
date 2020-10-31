#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import packages we need 
import os
import csv
import numpy as np
import pandas as pd


# In[5]:


#Bring excel file into python
df = pd.read_csv(r'C:\Users\gonza\Desktop\du-den-data-pt-08-2020-u-c\03-Python\Homework\Instructions\PyPoll\Resources\election_data.csv', low_memory = False,)
df.head(20)


# In[21]:


#total number of votes cast
vote = df.count(axis = 0)
count_row = df.shape[0]
print(count_row)


# In[13]:


#A complete list of candidates who received votes 
c = df.loc[:,'Candidate']
y = pd.DataFrame(c)
#y.head(25)
groups = y.apply(pd.Series.value_counts, axis=0)
print(groups)


# In[14]:


# % of votes each candidate won
p = df.loc[:,'Candidate']
per = pd.DataFrame(p)
per.head(25)
percantage = per.apply(pd.Series.value_counts, axis=0, normalize = True)
print(percantage)


# In[18]:


#Number of unique votes per candidate (used original df because it has all columns)
u = df.groupby('Candidate')['Voter ID'].nunique() 
print(u)


# In[24]:


#print/ summary
print(f'The total number of votes is {count_row}')
print(f'The voting looked like \n {percantage}')
print(f'The winner was Khan')


# In[ ]:




