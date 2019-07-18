#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import sqlite3 as sqldatabase


# In[2]:


# create a connector
connector = sqldatabase.connect('store.db')


# In[3]:


# Select all columns of the table consumer
query = 'SELECT first_name, last_name '
query += 'FROM consumer '
query += "WHERE gender= 'Male'"
df_result = pd.read_sql(query, connector)
display(df_result)


# In[4]:


query = "SELECT *"
query += " FROM Consumer"
query += " WHERE age > 40"
df_result = pd.read_sql(query, connector)
display(df_result)


# In[5]:


query = "SELECT *"
query += " FROM Consumer"
query += " WHERE age > 10000"  # just gets the attributes of the table
df_result = pd.read_sql(query, connector)
display(df_result)


# In[6]:


query = "SELECT *"
query += " FROM Consumer" 
query += " WHERE age >= 20 AND age <= 30"  # use of AND statement
df_result = pd.read_sql(query, connector)
df_result


# In[7]:


query = "SELECT *"
query += " FROM Consumer"
query += " WHERE last_name = 'Clemes'"
df_result = pd.read_sql(query,connector)
df_result


# In[8]:


query = "SELECT *"
query += " FROM Consumer"
query += " WHERE age > 40"
query += " ORDER BY age"  # add DESC for descending order
df_result = pd.read_sql(query,connector)
df_result


# In[9]:


query = "SELECT gender, AVG(age), count(*)"
query += " FROM Consumer"
query += " GROUP BY gender"
query += " HAVING count(*) < 500"  # HAVING function
df_result = pd.read_sql(query,connector)
df_result


# In[10]:


query = "SELECT C.last_name, C.age"
query += " FROM Consumer C"
query += " WHERE C.age > 30"
df_result = pd.read_sql(query,connector)
df_result


# In[11]:


query = "SELECT Purchase.*, Consumer.last_name, Consumer.age"
query += " FROM Consumer INNER JOIN Purchase"
query += " ON Consumer.id=Purchase.consumer_id"
df_result = pd.read_sql(query,connector)
df_result


# In[12]:


query = "SELECT *"
query += " FROM Consumer"
query += " WHERE age > 40"  # HAVING function

query += " INTERSECT"  # we can use intersects!
query += " SELECT *"
query += " FROM Consumer"
query += " WHERE age < 60"  # HAVING function

df_result = pd.read_sql(query,connector)
df_result


# In[13]:


query = "SELECT  last_name as 'LAST NAME', age, Gender, AVG(price) AS 'Avg. price of Purchased Products', SUM(price*quantity) AS 'Total amount spent in store' "
query += " FROM Consumer c INNER JOIN Purchase p INNER JOIN Product pro"
query += " ON c.id = p.consumer_id AND pro.id=p.product_id"
query += " GROUP BY c.id"
df_result = pd.read_sql(query,connector)
df_result

