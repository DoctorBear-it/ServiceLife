# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:56:30 2016

@author: Timothy
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x,a,b,c):
    return a*np.exp(-b*x)+c

xdata = np.linspace(0,4,50)
y = func(xdata,2.5,1.3,0.5)
ydata = y+0.2*np.random.normal(size=len(xdata))
popt,pcov = curve_fit(func,xdata,ydata)

DOS = np.linspace(0,1,101)
n = 3.28
phi = 0.15
gel_cond = 0.22
F_S = ((1/(1+(DOS/(1-phi))**(-4*n)))+gel_cond)*(1-gel_cond)*(1+(1/(1-phi))**(-4*n))

def newSaturationFunction(S,n,phi,gel_cond):
    return ((1/(1+(S/(1-phi))**(-4*n)))+gel_cond)*(1-gel_cond)*(1+(1/(1-phi))**(-4*n))
xdata1 = DOS
ydata1 = F_S
popt1,pcov1 = curve_fit(newSaturationFunction,xdata1,ydata1,bounds=(0,[5,0.25,0.25]))
perr = np.sqrt(np.diag(pcov1)) #Standard deviation!
#pcov diagonals provide the variance of the parameter estimates
S=DOS
plt.plot(S,F_S,S,newSaturationFunction(S,popt1[0],popt1[1],popt1[2]))