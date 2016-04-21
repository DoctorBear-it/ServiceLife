# -*- coding: utf-8 -*-
"""
Created on Fri Nov 06 01:52:16 2015

@author: Timothy
"""

import random
import numpy as np
import scipy
import scipy.stats
import matplotlib.pyplot as plt


compressiveStrengthMax = 33 #MPa
elasticModulusMax = 27.5*1000 #Mpa
tensileStrengthMax = 5 #MPa

time = 0 #time of simulation in days
timeSet = 0.3 #time of set in days
timeDry = 0 #time of drying in days
C1 = 2.0 #units in 1/day for each coeff
C2 = 0.3
C3 = 15.
C4 = 30.
humidityInternal = 0.95
humidityAmbient = 0.50

volumeAggregates = 0.708
betaShrinkage = 3000 #microstrain
n = 1.2
strainMax = betaShrinkage*(1-volumeAggregates)**n*(1-humidityAmbient**3)

elasticModulusTime = elasticModulusMax*C1*(time-timeSet)/(1+C1*(time-timeSet))

tensileStrengthTime = tensileStrengthMax*C2*(time-timeSet)/(1+C2*(time-timeSet))

strainAutogenous = strainMax*(1-humidityInternal**3)*np.tanh((time-timeSet)/C3)

strainDrying = strainMax*(humidityInternal**3-humidityAmbient**3)*np.tanh((time-timeDry)/C4)

strainThermal = 0.

strainTotal = strainAutogenous + strainDrying + strainThermal



