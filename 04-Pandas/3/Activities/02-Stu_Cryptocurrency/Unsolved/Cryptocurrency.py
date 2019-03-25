#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Dependencies
import pandas as pd


bitcoin_csv = "/Users/krishna/Documents/School/GeorgiaTech/GTATL201902DATA3/04-Pandas/3/Activities/02-Stu_Cryptocurrency/Unsolved/Resources/bitcoin_cash_price.csv"
dash_csv = "/Users/krishna/Documents/School/GeorgiaTech/GTATL201902DATA3/04-Pandas/3/Activities/02-Stu_Cryptocurrency/Unsolved/Resources/dash_price.csv"


# In[ ]:


bitcoin_df = pd.read_csv(bitcoin_csv)
dash_df = pd.read_csv(dash_csv)



# In[ ]:


print(bitcoin_df.head())


# In[ ]:


print(dash_df.head())


# In[ ]:


# Merge the two DataFrames together based on the Dates they share
crypto_df = pd.merge(bitcoin_df,dash_df,on ='Date', suffixes = (' Bit', ' Dash'))
print(crypto_df.head())
print(crypto_df.columns)



# In[ ]:


# Rename columns so that they are differentiated
#crypto_df = crypto_df.rename(columns = {
#'Open_x':'Bitcoin Open','High_x':'Bitcoin High', 'Low_x': ' Bitcoin Low', 'Close_x':'Bitcoin Close', 'Volume_x':'Bitcoin Volume', 'Market Cap_x':'Bitcoin Market Cap'
#})

print(crypto_df.columns)

# In[ ]:


# alternatively you can set your suffixes when the merge occurs


# In[ ]:


# Collecting best open for Bitcoin and Dash
#bitcoin_dash_bestopen = crypto_df[['Open Bit']].max()
temp_col = crypto_df[crypto_df["Open Bit"]==crypto_df["Open Bit"].max()]
print(temp_col['Date'])






# Collecting best close for Bitcoin and Dash


# Collecting the total volume for Bitcoin and Dash


# In[ ]:


# Creating a summary DataFrame using above values
