#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#x-axis = np.arrange(1,13,1)


Fahrenheit_temp = [39, 42, 51, 62, 72, 82, 86, 84, 77, 65, 55, 44]
Celsius_temp =[]

for cel in Celsius_temp:
    var = cel - 32
    var = var * .56
    Celsius_temp.append(var)
    print(Celsius_temp)
