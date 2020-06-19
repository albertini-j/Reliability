# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:20:29 2020

@author: cellnote
"""
from sympy import *
init_session()
from sympy.stats import *
import matplotlib.pyplot as plt
import numpy as np

#Modarres exercise 3.12
interval=np.array[0,100,200,300,400,500]
failures=np.array[0,10,7,3,3,2]
units =np.sum(failures)


#pdf


#hazard rate




#reliability
cumulative=np.cumsum(failures)
print(cumulative)
