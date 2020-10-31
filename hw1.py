#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Import packages we need 
import os
import csv
import numpy as np
import pandas as pd


# In[7]:


#Bring excel file into python
df = pd.read_csv(r'C:\Users\gonza\Desktop\du-den-data-pt-08-2020-u-c\03-Python\Homework\Instructions\PyBank\Resources\budget_data.csv', low_memory = False,)
#df.head(50)
print(df)


# In[6]:


#Get total number of months included... count up the unique dates
df.Date.value_counts() = m
#Our output says 86 different dates


# In[8]:


#Net total profit/loss of data
t = df['Profit/Losses'].sum()
print(t)


# In[9]:


#average changes in p/l
average = df["Profit/Losses"].mean()
print(average)


# In[11]:


#greatest increase
most = df['Profit/Losses'].max()
print(most)


# In[27]:


#greatest increase/decrease in profit, convert column to list so we can do list comprehension to get values needed
total_profit = []
total_profit = df.iloc[1]
month_profit_change = []
month_profit_change= df.loc[0]
pd.to_numeric(total_profit)
pd.to_numeric(month_profit_change)
for i in range(len(total_profit)-1):
    month_profit_change.append(total_profit[i+1] - total_profit[i])
    max_increase_value = max(month_profit_change)
    max_decrease_value = min(month_profit_change)

# Correlate max and min to the proper month using month list and index from max and min, create list as well. then replace values
max_increase_month = month_profit_change.index(max(month_profit_change)) + 1
max_decrease_month = month_profit_change.index(min(month_profit_change)) + 1


# In[ ]:


#print and export
f= open("answer.txt","w+")
f.write(
print(f'net total of profits/losses is {t}')
print(f'net total of months is {m}')
print(f'average changes in P/L is {average}')
print(f'The biggest profit came in {max_increase_month}')
print(f'The lowest profit came during {min_increase_month}'))
f.close()


# In[ ]:




