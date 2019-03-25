import pandas as pd



# The path to our CSV file
path = '/Users/krishna/Documents/School/GeorgiaTech/GTATL201902DATA3/04-Pandas/3/Activities/06-Stu_CleaningKickstarter/Unsolved/Resources/KickstarterData.csv'


# Read our Kickstarter data into pandas
df_data = pd.read_csv(path)
print(df_data.head())
print(df_data.columns)

# Extract "name", "goal", "pledged", "state", "country", "staff_pick",
# "backers_count", and "spotlight"

new_df = df_data[['name', 'goal', 'pledged', 'state', 'country', 'staff_pick',"backers_count","spotlight"]]
# Remove projects that made no money at all
nm_df= new_df[new_df['goal']>0]
print(nm_df.columns)


# Collect only those projects that were hosted in the US
us_df = nm_df[nm_df['country']=='US']
print(us_df['country'].head())

# Create a new column that finds the average amount pledged to a project



# In[ ]:


# First convert "average_donation", "goal", and "pledged" columns to float
# Then Format to go to two decimal places, include a dollar sign, and use comma notation


# In[ ]:


# Calculate the total number of backers for all US projects


# In[ ]:


# Calculate the average number of backers for all US projects


# In[ ]:


# Collect only those US campaigns that have been picked as a "Staff Pick"


# In[ ]:


# Group by the state of the campaigns and see if staff picks matter (Seems to matter quite a bit)
