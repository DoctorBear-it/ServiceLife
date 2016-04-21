# -*- coding: utf-8 -*-
"""
Created on Fri Nov 06 17:32:38 2015

@author: Timothy
"""

from fipy import*
import math
import numpy as np
import matplotlib.pyplot as plt
import pprint
from fipy.tools import dump 
import timeit
from datetime import *
from dateutil.rrule import *
import calendar
import time as tme



castDate = date.today()             #Assumed cast date is current date 
time = Variable()                   
simDate = Variable()
simDate = castDate               #Initialize the simulation date
#deicerMonths = rrule(YEARLY, bymonth = (1,2,3,11,12), dtstart = castDate)
deicerMonth = [1,2,3,11,12]
Temp = Variable()
def salting(simDate):
    if simDate.month in deicerMonth:
        return 0.3
    else:
        return 0.

def annualTemp(simDate):
    def sinceEpoch(simDate):
        return tme.mktime(simDate.timetuple())
    s = sinceEpoch
    
    year = simDate.year
    yearStart = date(year = year, month = 1, day = 1)
    nextyearStart = date(year = year+1, month = 1, day = 1)
    
    yearElapsed = s(simDate) - s(yearStart) 
    yearDuration = s(nextyearStart) - s(yearStart)
    fraction = yearElapsed/yearDuration    
#    raction*12 + 0.5
    T = -13.*np.cos((fraction*12+0.5)*(np.pi/6))+284.7
    return T
    




#for simDate.month in deicerMonth:
#if simDate.month == deicerMonth:
#    valueLeft = 3.
##elif month < 2:
##    valueLeft = 3.
#else: 
#   valueLeft = 0.0 

#valueLeft = 1   
   
timeStepDuration = 24*60*60 #half day timestep
delta = timedelta(seconds = timeStepDuration)
while time() < timeStepDuration*365:    
    time.setValue(time() + timeStepDuration)
    simDate += delta
#    print(time)    
#    print(simDate.month)
    valueLeft = salting(simDate)
    Temp = annualTemp(simDate)
    print(Temp)
#    if simDate.month in deicerMonth:
#        valueLeft = 3.
#    else: 
#        valueLeft = 0.0 
#    
    
    
    plt.ion()
#    plt.plot(simDate, valueLeft, 'o-')
    plt.plot(simDate, Temp, 'o-')    
    plt.draw()
    