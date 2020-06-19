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
ln_data=[]
for i in range(len(data)):
    ln_data.append(N(ln(data[i]),10))
print('ln data:')    
print(ln_data)
test_time=60
failures=6



Rlist=[]
Rlist_inv=[]
Rlist_inv_ln=[]
n=10
for i in range(6):
    #Ri=1-i/10
    Ri=1-(i+1-0.375)/(n+0.25)
    Rlist.append(Ri)
    inverso=1/Rlist[i]
    Rlist_inv.append(inverso)
    logn_logn_r_inverso=ln(ln(inverso))
    Rlist_inv_ln.append(logn_logn_r_inverso)    #inclui ln(ln(1/R(ti)))
print(Rlist)
print(Rlist_inv)

X_axis = np.array(ln_data)
Y_axis = np.array(Rlist_inv_ln)
R0368= np.array([0.368])





slope = (len(X_axis) * np.sum(X_axis*Y_axis) - np.sum(X_axis) * np.sum(Y_axis)) / (len(X_axis)*np.sum(X_axis*X_axis) - np.sum(X_axis) ** 2)
	
bias = (np.sum(Y_axis) - slope *np.sum(X_axis)) / len(X_axis)

a=slope
b=bias
expr= a*x+b-y
solve(y.subs(y,0.368),x)
print('R(0.368)=')
print(solve(y.subs(y,0.368),x))



print('fitted slope')
print(slope)
print('fitted bias')
print(bias)
range_variable_start=3.6 #definir a faixa de plotagem
range_variable_end=4.2 #definir a faixa de plotagem conforme a faixa dos dados

xaxis = np.arange(range_variable_start,range_variable_end,0.01)
yaxis = slope*xaxis+bias

fig, ax = plt.subplots()
ax.plot(xaxis, yaxis)
ax.scatter(ln_data,Rlist_inv_ln)
ax.set(xlabel='ln(test time)', ylabel='ln(ln(1/R(t)))',
       title='Weibull plot')
ax.grid()

fig.savefig("test.png")
plt.show()

