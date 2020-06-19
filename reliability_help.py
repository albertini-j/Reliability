from sympy import *
init_session()
from sympy.stats import *
import matplotlib.pyplot as plt
import numpy as np

F, a, b, R, mttf, l =symbols('F a b R mttf l')

def ztable_inverse(cdf_point):
    z=Normal('z', 0, 1)
    b_z=0
    a_z=-5
    while b_z<cdf_point:
        a_z=a_z+0.1
        b_z=N(cdf(z)(a_z))
    while b_z>cdf_point:
        a_z=a_z-0.0001
        b_z=N(cdf(z)(a_z))
    return N(a_z,6)

def ztable(point): 
    z=Normal('z', 0, 1)    
    return N(cdf(z)(point),6)

def paralelo(*reliabilities):
    temporary=np.array(reliabilities)
    temporary=np.subtract(1,temporary)
    temporary=np.prod(temporary)
    return 1-temporary

def serie(*reliabilities):
    temporary = np.array(reliabilities)
    return np.prod(temporary)

def loadshare(RhL,RfL,fhL): #all inputs must be in function of "t"
    return RhL**2+2*integrate(fhL.subs({t:t1})*RhL.subs({t:t1})*RfL.subs({t:(t-t1)}),(t1,0,t))

def perfect_ss(R1S,R2S,f1S): #all inputs must be in function of "t"
    return R1S+integrate(f1S.subs({t:t1})*R2S.subs({t:(t-t1)}),(t1,0,t))

print("Reliability help loaded.")