#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
#
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:

# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "/Users/krishna/Documents/School/GeorgiaTech/HW/HW4/Instructions/HeroesOfPymoli/Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
print(purchase_data.head())
print(purchase_data.columns)
#print(purchase_data.info())

# ## Player Count
player_count = purchase_data['Purchase ID'].count()
print('Total number of player:',player_count)

# * Display the total number of players
#



# In[2]:

# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
unique_items = purchase_data['Item Name'].value_counts()
print(unique_items)

avg_price = purchase_data['Price'].mean()
print('The average price:' ,avg_price)

num_of_purchase = purchase_data[purchase_data['Price']>0].count()
print(num_of_purchase)
#
#
# * Create a summary data frame to hold the results
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display the summary data frame
#

# In[3]:





# ## Gender Demographics

# * Percentage and Count of Male Players
#
#
# * Percentage and Count of Female Players
#
#
# * Percentage and Count of Other / Non-Disclosed
#
#
#

# In[4]:





#
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
#
#
#
#
# * Create a summary data frame to hold the results
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display the summary data frame

# In[5]:





# ## Age Demographics

# * Establish bins for ages
#
#
# * Categorize the existing players using the age bins. Hint: use pd.cut()
#
#
# * Calculate the numbers and percentages by age group
#
#
# * Create a summary data frame to hold the results
#
#
# * Optional: round the percentage column to two decimal points
#
#
# * Display Age Demographics Table
#

# In[6]:





# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
#
#
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
#
#
# * Create a summary data frame to hold the results
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display the summary data frame

# In[7]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
#
#
# * Create a summary data frame to hold the results
#
#
# * Sort the total purchase value column in descending order
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display a preview of the summary data frame
#
#

# In[8]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
#
#
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
#
#
# * Create a summary data frame to hold the results
#
#
# * Sort the purchase count column in descending order
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display a preview of the summary data frame
#
#

# In[9]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
#
#
# * Optional: give the displayed data cleaner formatting
#
#
# * Display a preview of the data frame
#
#

# In[10]:
