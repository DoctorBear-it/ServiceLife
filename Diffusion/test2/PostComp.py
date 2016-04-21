# -*- coding: utf-8 -*-
"""
Created on Thu Nov 05 23:15:24 2015

@author: Timothy
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.loadtxt('x.txt', delimiter = ",")
concentration = np.loadtxt('c.txt', delimiter = ",")

plt.plot(x, concentration, '-', linewidth = 2)
plt.show()

t = np.loadtxt('t.txt', delimiter = ",")
a = np.loadtxt('CAR.txt', delimiter = ",")

plt.plot(t, a, '-', linewidth = 2)
plt.show()



