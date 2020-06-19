# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:55:39 2020

@author: cellnote
"""

#ex 3.16
n=10
mean=102.5
sd=9.45
confidence=0.8

#t_student_10%(9 degrees of freedom)= 1.3830
t=1.3830
lower=N(mean-t*sd/sqrt(n))
upper=N(mean+t*sd/sqrt(n))

print('o intervalo de confiança da média é  Pr( '+str(lower)+'< mi < '+str(upper)+' )= 0.8')

#ChiSquared_1-alfa/2 (n-1)=14.6837
#ChiSquared_alfa/2 (n-1)=4.1684
chi_lower=14.6837
chi_upper=4.1684

sd_lower=N(sqrt((n-1)*sd**2/chi_lower))
sd_upper=N(sqrt((n-1)*sd**2/chi_upper))

print('o intervalo de confiança do desvio padrão é  Pr( '+str(sd_lower)+'< sigma < '+str(sd_upper)+' )= 0.8')
