# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:19:18 2020

@author: cellnote
"""

from sympy import *
init_session()
from sympy.stats import *
f=exp(2*sqrt(t))/sqrt(t) #f(t)
print('failure pdf')
pprint(f)
print('F(t)')
g=integrate(f,t) #cdf
pprint(g)
k=E(f) #mttf
print('mttf')
pprint(k)