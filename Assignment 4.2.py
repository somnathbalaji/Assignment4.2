
# coding: utf-8

# @author: Somnath Balaji
# # Find the variance for the following set of data representing trees in California (heights in feet):
# # 3, 21, 98, 203, 17, 9

# In[7]:


# Importing the libraries
import numpy as np                                              
import pandas as pd 
import statistics

# Creating a list from the given data
l = [3, 21, 98, 203, 17, 9]

# Using the inbuilt variance library to calculate the variance and printing it
v=statistics.variance(l)
print("Variance for the Given Data :",v) 

