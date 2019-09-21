# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:55:32 2019

@author: Lisa
"""

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('behaviourspace_test.csv',)

conflicts = data["conflict"]

print (conflicts)
#for i in range(number_of_experiments):
#    conflicts_agent2=conflicts[number_of_experiments]
#conflicts_agent2=[1,2,3,4,1,2,3,45,6,5,4,3,2,1,6,5,4,3,5,6,7,8,90,90,80,70,9]


plt.xlabel('agent population')
plt.ylabel('Number of conflicts')
plt.boxplot(conflicts_agent2)
plt.show()