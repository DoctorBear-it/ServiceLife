# -*- coding: utf-8 -*-
"""
Created on Sat Nov 07 20:47:05 2015

@author: Timothy
"""

from datetime import datetime as dt
import time as t

def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return t.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return fraction*12 + 1
    
    
delta = toYearFraction(dt(2015,1,15))
print(delta)