# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:26:16 2020

@author: cellnote
"""
from sympy import *
init_session()
from sympy.stats import *
import matplotlib.pyplot as plt
import numpy as np

#exercise 3.14


#exponential distribution
l=0.003 #failure/cycle

#a)what is the mean number of cycles to failure for this product?
x=l*exp(-l*t)
MCTF=integrate(t*x,(t,0,oo))
print(MCTF) #result 333,333, ou 1/lambda, como previsto

#b)if a component survives 300 cycles  what is the probability it will fail sometime after 500 cycles?
failure_300=integrate(x,(t,0,300))
print('chance to survive 300= '+str(1-failure_300))
failure_500=integrate(x,(t,0,500))
print('chance to survive 500=  '+str(1-failure_500))
answer_b=(1-failure_500)/(1-failure_300)
#print(answer_b)




#b part 2 )if 1000 components have survived 300 cycles, how many will be expected to fail after 500?
print(answer_b*1000)


