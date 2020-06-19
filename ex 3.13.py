# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 13:09:09 2020

@author: cellnote
"""

from sympy import *
init_session()
from sympy.stats import *
import matplotlib.pyplot as plt
import numpy as np

#Modarres exercise 3.13
#what is the probability that estimated failure rate is not greater than 4.6*10**-5/h
T=50000 #hours
r=1 #fault
limit=4.6*10**-5
#Type II test - Fault terminated
#Table 3.3 formula
ChiiSquared=limit*2*T
print(ChiSquared)
#resultado 4.6

#Chi Quadrado da propabilidade que procuramos é 4.6, consultando a tabela do
#observamos que o Chi de 90% é 4.6, então a chance da taxa de falha não ser maior
#que 4.6*10**-5 é 90%.

