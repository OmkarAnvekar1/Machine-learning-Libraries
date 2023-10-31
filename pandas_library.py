#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np


# In[2]:


dict = {
   " name" :[ "Omkar ","Chand","Meenu","Shubham"],
    "roll_no " : [50,22,45,31],
    "dept" : ['ECE',"CSE","ECE","ECE"]
}


# In[3]:


df = pd.DataFrame(dict)


# In[4]:


df


# In[5]:


df.to_csv('friends.csv')


# In[6]:


# to remove index 


# In[7]:


df.to_csv('friends.csv',index=False)


# In[8]:


df.head(2)


# In[9]:


df.tail(2)


# In[10]:


df.describe()


# In[11]:


new = pd.read_csv(r"C:\Users\omkar\Downloads\College ML\game.csv")


# In[12]:


new


# In[13]:


new['match']


# In[14]:


new['text']


# In[15]:


new['text'][0]


# In[16]:


new['text'][4]


# In[17]:


new['text'][0] = 100000


# In[18]:


new


# In[19]:


new.to_csv('game.csv')


# In[20]:


#new.index = ['first','second','third']


# In[21]:


# series object and dataframes  (single column [uniform data type]and full table)


# In[22]:


series = pd.Series(np.random.rand)


# In[23]:


series


# In[24]:


series = pd.Series(np.random.rand(25))
series


# In[25]:


type(series)


# In[26]:


# create new data frame


# In[27]:


new_dataframe = pd.DataFrame(np.random.rand(50,4) , index = np.arange(50))
new_dataframe


# In[28]:


new_dataframe.describe()


# In[29]:


new_dataframe.head(1)


# In[30]:


new_dataframe[0][0] = "12345"
new_dataframe.head(1)


# In[31]:


new_dataframe.index


# In[32]:


new_dataframe.columns


# In[33]:


new_dataframe.to_numpy()


# In[34]:


new_dataframe.T


# In[35]:


new_dataframe.sort_index(axis = 0, ascending = False)


# In[36]:


# axis=0 rows
# axis=1 columns


# In[37]:


new_dataframe[0]


# In[38]:


new_dataframe[1]


# In[39]:


new_dataframe.head(5)


# In[40]:


# copying (pseudo)      'VIEW CONCEPT'


# In[41]:


modern_dataframe =  new_dataframe


# In[42]:


modern_dataframe.head()   # here "new_dataframe " is not copied but just "modern_dataframe " point to "new_dataframe "


# In[43]:


modern_dataframe[0][0] = 999999


# In[44]:


modern_dataframe.head()  #proof that 2nd points 1st that like "view"


# In[45]:


# modern (naya wala ) ko change kia toh pahila wala bhi change hoga that is , 
#"View " ho raha hai 


# In[46]:


Actual_copy_dataframe = new_dataframe.copy()


# In[47]:


Actual_copy_dataframe[0][0] = 9379910111


# In[48]:



Actual_copy_dataframe.head(1)


# In[50]:


new_dataframe.head()  #original one not changing


# In[ ]:


# loc function


# In[51]:


new_dataframe.loc[0,0] = 99


# In[52]:


new_dataframe.head(2)


# In[53]:


new_dataframe.columns = list("ABCD")


# In[55]:


new_dataframe.head()


# In[58]:


new_dataframe.loc[0,"A"] = 909


# In[59]:


new_dataframe.head(2)


# In[60]:


new_dataframe.loc[0,0] = 99


# In[70]:


new_dataframe.head(2)


# In[71]:


new_dataframe.loc[0,0] = 'newcolumn'


# In[72]:


new_dataframe.head(2)


# In[73]:


new_dataframe = new_dataframe.drop(0,axis = 1)  #column drop


# In[74]:


new_dataframe.head(1)


# In[78]:


new_dataframe.loc[[1,2],["C","D"]] # temporary access some parts


# In[79]:


new_dataframe.loc[:,["C","D"]] 


# In[82]:


new_dataframe.loc[(new_dataframe["A"]<0.33)]  # 0th column par 0.3 se kam values 


# In[83]:


new_dataframe.loc[(new_dataframe["A"]<0.33) & (new_dataframe["A"]>0.1)] 


# In[86]:


new_dataframe.head(3)


# In[89]:


new_dataframe.iloc[0,2]   # target through index can use no. to index instead of letters, letters are only used to access columns "loc function - for columns"


# In[88]:


new_dataframe.iloc[[0,2],[1,2]]


# In[90]:


new_dataframe.head(5)


# In[93]:


new_dataframe = new_dataframe.drop(0,axis = 1)


# In[94]:


new_dataframe.head(2)


# In[95]:


# new_dataframe.drop(0,axis = 1, inplace = True)


# In[97]:


new_dataframe.reset_index()


# In[100]:


new_dataframe.reset_index(drop = True, inplace = True)


# In[102]:


# remove null from csv's : "pandas.dataframes.dropna"
# remove duplicates from csv's : "pandas.dataframes.drop_duplicates"


# In[103]:


new_dataframe['A'].isnull()


# In[104]:


new_dataframe['B'] = None


# In[105]:


new_dataframe.head()


# In[106]:


new_dataframe.loc[:,'B'] = None


# In[107]:


new_dataframe.head(10)


# In[108]:


df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})


# In[109]:


df


# In[110]:


df.dropna()


# In[111]:


df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, np.nan, np.nan],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})


# In[112]:


df.dropna(how = 'all', axis = 1)


# In[113]:


#drop duplicates


# In[114]:


df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Alfred'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})


# In[115]:


df.drop_duplicates(subset = ['name'], keep = "first")


# In[117]:


df.shape


# In[118]:


df.info()


# In[119]:


df["name"].value_counts(dropna = False)


# In[120]:


df.notnull()


# In[121]:


df.mean()
df.corr()
df.count()
df.max()
df.median()
df.std()


# In[ ]:




