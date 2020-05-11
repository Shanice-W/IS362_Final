#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[31]:


crime_data = pd.read_csv(r'C:\Users\shani\Downloads\atlcrime.csv')
crime_data.head(20)


# This is the total number of crimes committed in ATL 

# In[35]:


number_of_crimes = crime_data.crime.count()
print(number_of_crimes)


# Types of Crimes committed

# In[39]:


type_of_crime = crime_data.groupby('crime').count()
print(type_of_crime)


# In[42]:


type_of_crime.plot.bar()
plt.title('Rate of Crime')
plt.xlabel('Type')
plt.ylabel('Quantity')


# Larceny from Vehicle and Larceny from Non Vehicles are the most popular crimes

# In[58]:


most_crimes = crime_data.groupby(['neighborhood', 'location']) 
print(most_crimes)

