# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:55:32 2019

@author: Lisa
"""

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import scipy
import csv
import numpy as np


confidence=0.95
n=10

def calc_confidence_interval(data,n,confidence):
    m=scipy.mean(data)
    stand_error=scipy.stats.sem(data)
    h = stand_error * scipy.stats.t.ppf((1 + confidence) / 2, n - 1)
    return [m-h,m+h]

conflict_0=[]
conflict_20=[]
conflict_80=[]
conflict_100=[]
rows=[]
# csv file name 
filename = "assignment1_netlogo_final experiment-spreadsheet-10-2.csv"   
#data=pd.read_csv('assignment1_netlogo_final experiment-spreadsheetnew.txt', delimiter = ';')


f=open(filename,'r')
reader=csv.reader(f)
for row in reader:
    rows.append(row)

f.close()

   

conflict=rows[17]#.split(';')


for i in range(len(conflict)-1):
    conflict[i]=float(conflict[i+1])
conflict=conflict[:-1]

for i in range(n):
    conflict_0.append(conflict[i])
for i in range(n,2*n):
    conflict_20.append(conflict[i])
for i in range(2*n,3*n):
    conflict_80.append(conflict[i]) 
for i in range(3*n,4*n):
    conflict_100.append(conflict[i]) 

#variation coefficient of data set

var_coeffA2=scipy.stats.variation(conflict_0)
var_coeffB2=scipy.stats.variation(conflict_20)
var_coeffB1=scipy.stats.variation(conflict_80)
var_coeffA1=scipy.stats.variation(conflict_100)
 
confi_A2= calc_confidence_interval(conflict_0,n,confidence)
confi_B2= calc_confidence_interval(conflict_20,n,confidence)
confi_B1= calc_confidence_interval(conflict_80,n,confidence)
confi_A1= calc_confidence_interval(conflict_100,n,confidence)

print('variation coefficient', var_coeffA2,var_coeffA1,var_coeffB1,var_coeffB2)
print ('confidence interval', confi_A2,confi_A1,confi_B1,confi_B2)
#




boxplotlist=[conflict_0, conflict_20, conflict_80, conflict_100]
x=[0 ,2 ,8, 10]

x=np.array(x)
plt.xlabel('Agent population, expressed in percentage type I')
plt.ylabel('Number of conflicts')
#plt.xlim(-40,140)
plt.boxplot(boxplotlist, positions=x)
