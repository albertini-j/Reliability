# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:19:36 2020

@author: cellnote
"""

from sympy import *
init_session()
from sympy.stats import *

F, a, b, R, mttf, l =symbols('F a b R mttf l')

#f= Piecewise((l*exp(-l*x),x>0),(0, x<=0))
f= l*exp(-l*x)
#pprint(f)
#plot(f.subs(l,1), (x,0,2))

F=integrate(f,(x,a, oo))
#pprint(F.subs(a,a).subs(l,2.2).doit())
pprint(simplify(exp(-l*(a+b))/exp(-l*(a))))