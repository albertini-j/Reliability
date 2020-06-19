# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 02:03:08 2020

@author: cellnote
"""
from sympy import *
init_session()
from sympy.stats import *
import matplotlib.pyplot as plt
import numpy as np


F, a, b, R, mttf, l =symbols('F a b R mttf l')
data=[37.5, 46, 48, 51.5, 53, 54.5]

test_time=60
failures=6
l=failures/test_time


Rlist=[]
Rlist_inv=[]
Rlist_inv_ln=[]
n=10
for i in range(6):
    #Ri=1-i/10
    Ri=(n-(i+1)+0.625)/(n+0.25)
    Rlist.append(Ri)
    inverso=1/Rlist[i]
    Rlist_inv.append(inverso)
    logn_r=ln(inverso)
    Rlist_inv_ln.append(logn_r)    
print(Rlist)
print(Rlist_inv)

X_axis = np.array(data)
Y_axis = np.array(Rlist_inv_ln)



plt.scatter(X_axis,Y_axis)


slope = (len(X_axis) * np.sum(X_axis*Y_axis) - np.sum(X_axis) * np.sum(Y_axis)) / (len(X_axis)*np.sum(X_axis*X_axis) - np.sum(X_axis) ** 2)
	
bias = (np.sum(Y_axis) - slope *np.sum(X_axis)) / len(X_axis)
print('fitted slope')
print(slope)
print('fitted bias')
print(bias)
range_variable_start=35 #definir a faixa de plotagem
range_variable_end=60 #definir a faixa de plotagem conforme a faixa dos dados

def predict(range_variable):
    return slope*range_variable+bias


vector=np.arange(range_variable_start,range_variable_end)


plt.xlabel('test time')
plt.ylabel('ln(1/R)')
plt.title('Exponential distribution probability plotting')            
plt.legend()
plt.scatter(X_axis,Y_axis, label='data')
plt.plot(vector,predict(vector), label='fitted line')


