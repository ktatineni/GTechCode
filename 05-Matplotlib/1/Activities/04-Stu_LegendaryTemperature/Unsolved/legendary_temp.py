#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



x_axis = np.arange(1,13,1)

fahrenheit_temp = [39, 42, 51, 62, 72, 82, 86, 84, 77, 65, 55, 44]
celsius_temp =[]

for cel in fahrenheit_temp:
    var = cel - 32
    var = var * .56
    celsius_temp.append(int(var))
print(celsius_temp)



plt.plot(x_axis,fahrenheit_temp)
plt.
plt.show()
