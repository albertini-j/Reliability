# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:55:02 2020

@author: cellnote
"""

#Modarres 3.15

from sympy import *
init_session()
from sympy.stats import *
import matplotlib.pyplot as plt
import numpy as np

mu=0.102
sigma=0.005
n=25
x=sigma/sqrt(n)
#print(x) #0.001

#z(1.65)=0.95
interval_estimate=mu+1.65*0.001
print('a resposta do exercício é Pr(mi < '+str(interval_estimate)+' )= 0.95')