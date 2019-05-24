# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:54:57 2019

@author: APL14
"""

import matplotlib.pyplot as plt
import os
import csv

directory = '20190524'
x = os.listdir(directory)
y = []

for file in x:
    with open(directory+"/"+file, 'r') as csvFile:
        data = [row for row in csv.reader(csvFile)]
        y.append(float(data[48][5]))

x = [float(xOne.split('.')[0].replace('_', '.')) for xOne in x]
x_axis = [idx for idx,elem in enumerate(y)]

plt.plot(x_axis,y)
plt.xlabel('time')
plt.ylabel('price')

plt.show()