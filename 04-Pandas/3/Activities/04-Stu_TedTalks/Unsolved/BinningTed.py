#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Dependencies
import pandas as pd


# In[ ]:


# Create a path to the csv and read it into a Pandas DataFrame
csv_path = "/Users/krishna/Documents/School/GeorgiaTech/GTATL201902DATA3/04-Pandas/3/Activities/04-Stu_TedTalks/Unsolved/Resources/ted_talks.csv"
ted_df = pd.read_csv(csv_path)

print(ted_df.head())
print(ted_df.columns)


# In[ ]:


# Figure out the minimum and maximum views for a TED Talk
max_views = ted_df['views'].max()
min_views = ted_df['views'].min()
print(min_views)
print(max_views)
# In[ ]:

# Create bins in which to place values based upon TED Talk views
bins = [50443,20000000,47227110]

# Create labels for these bins
labels = ['low views', 'high views']

# In[ ]:


# Slice the data and place it into bins
bin_df = pd.cut(ted_df,bins,labels=labels)


# In[ ]:


# Place the data series into a new column inside of the DataFrame


# In[ ]:


# Create a GroupBy object based upon "View Group"


# Find how many rows fall into each bin


# Get the average of each column within the GroupBy object
