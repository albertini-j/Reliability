# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:18:35 2020

@author: cellnote
"""

#3.17 MOdarres

strength=np.array([660,460,540,580,550]) #lb
n=strength.size
mean=np.mean(strength)
sd=np.std(strength,ddof=1)
print('mean= '+str(mean))
print('sd= '+str(sd))

#t_student_2.5%(4 degrees of freedom)= 2.7764
t=2.7764
lower=N(mean-t*sd/sqrt(n))
upper=N(mean+t*sd/sqrt(n))

print('o intervalo de confiança da média é  Pr( '+str(lower)+' < mi < '+str(upper)+' ) = 0.95')


#Z(-1.64)=0,05

#1.64=(x-mean)/sd
x=-1.64*sd+mean
print('a força que rompe apenas 5% das cordas: '+str(x)+' lbs')


#o intervalo de confiança 90% do desvio padrão


#ChiSquared_95%(4 degrees)=9.4877
#ChiSquared_5%(4 degrees of freedom)= 0.7107


chi_lower=9.4877
chi_upper=0.7170

sd_lower=N(sqrt((n-1)*sd**2/chi_lower))
sd_upper=N(sqrt((n-1)*sd**2/chi_upper))



print('o intervalo de confiança do desvio padrão é  Pr( '+str(sd_lower)+'< sigma < '+str(sd_upper)+' )= 0.90')

