# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:28:41 2020

@author: cellnote
"""

from sympy import *
init_session()
from sympy.stats import *

F=symbols('F') #F(t)
F=Piecewise((1-100/t,t>=100),(0, t<100))
print('F(t)')
pprint(F)
print('f(t)')
f=diff(F,t)#f(t)
pprint(f)
g=E(f)#mttf
print('mttf')
pprint(g)