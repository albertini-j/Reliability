# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:20:29 2020

@author: cellnote
"""
from sympy import *
init_session()
from sympy.stats import *
import matplotlib.pyplot as plt
import numpy as np

#Modarres exercise 3.12
interval=np.array([0,100,200,300,400,500])
failures=np.array([0,10,7,3,3,2])
units =np.sum(failures)

cumulative=np.cumsum(failures)
survivors=np.subtract(units,cumulative)
#pdf
pdf_denom=np.multiply(units,np.array([100]))
pdf=np.divide(failures,pdf_denom)
plt.figure(3)
plt.title('failure pdf')
plt.plot(interval,pdf)
#hazard rate

hazard_denom = np.multiply(survivors,np.array([100]))
hazard=np.divide(cumulative,hazard_denom)
plt.figure(2)
plt.title('hazard plot')
plt.plot(interval,hazard)



#reliability
reliability=np.divide(survivors,units)
plt.figure(1)
plt.title('reliability plot')
plt.plot(interval,reliability)