# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:55:32 2019

@author: Lisa
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import csv
import numpy as np

n=10

conflict_0=[]
conflict_20=[]
conflict_80=[]
conflict_100=[]
rows=[]
# csv file name 
filename = "assignment1_netlogo_final experiment-spreadsheet.csv"   
#data=pd.read_csv('assignment1_netlogo_final experiment-spreadsheetnew.txt', delimiter = ';')


f=open(filename,'r')
reader=csv.reader(f)
for row in reader:
    print(row)
    rows.append(row)

f.close()

   

conflict=rows[17][0].split(';')
print(conflict)

for i in range(len(conflict)-1):
    conflict[i]=float(conflict[i+1])
#    print(conflict)
conflict=conflict[:-1]


for i in range(n):
    conflict_0.append(conflict[i])
for i in range(n,2*n):
    conflict_20.append(conflict[i])
for i in range(2*n,3*n):
    conflict_80.append(conflict[i]) 
for i in range(3*n,4*n):
    conflict_100.append(conflict[i]) 

#confidence_interval=scipy.stats.sem
variation_coefficient0=scipy.stats.variation(conflict_0)
variation_coefficient20=scipy.stats.variation(conflict_20)
variation_coefficient80=scipy.stats.variation(conflict_80)
variation_coefficient100=scipy.stats.variation(conflict_100)
#
boxplotlist=[conflict_0, conflict_20, conflict_80, conflict_100]
x=[0 ,2 ,8, 10]

x=np.array(x)
plt.xlabel('Agent population, expressed in percentage type I')
plt.ylabel('Number of conflicts')
#plt.xlim(-40,140)
plt.boxplot(boxplotlist, positions=x)
