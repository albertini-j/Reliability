# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 23:46:23 2020

@author: cellnote
"""

from sympy import *
init_session()
from sympy.stats import *

F, a, b, R, mttf =symbols('F a b R mttf')

f= t*exp((-t**2)/(2*a**2))/(a**2)
print('f(t)')
pprint(f)

F=integrate(f,t)
print('F(t)')
pprint(F)
R=1-F
h=simplify(-diff(ln(R),t))
print('h(t)')
pprint(h)
mttf=E(f)
print('mttf')
pprint(simplify(mttf))


#plot(h.subs(a,0.5), (t, 0, 10))
#plot(h.subs(a,1), (t, 0, 10))
#plot(h.subs(a,2), (t, 0, 10))
plot(h.subs(a,5), (t, 0, 50))