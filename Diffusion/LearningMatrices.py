# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 19:51:29 2015

@author: Timothy
"""

import numpy as np
import matplotlib.pyplot as plt
#A note on numbers: a period at the end '1.' is a float64, no period '1' is int64

a = np.array([0, 1, 2, 3])
print(a)

print(a.ndim)
print(a.shape)
print(len(a))

b = np.arange(4)
print(b)

b2 = np.arange(1, 9, 2) # start, end (exclusive), step
print(b2)
z = np.linspace(0, 1, 6)   # start, end, num-points
print(z)
c = np.ones((3,3)) #3x3 is called a 'tuple'
print(c)
c2 = np.empty((3,3))
print(c2)
d = np.zeros((3,3))
print(d)
e = np.eye(3)
print(e)
f = np.diag(np.arange(1,15,1))
print(f)
g = np.random.rand(4)
print(g)

print(f[2,1]) #second line, first column

y = np.array([1,10,1])
x = np.array([1,10,1])

plt.plot(x,y)
plt.show()

plt.plot([1,2,3], [1,2,3], 'go-', label='line 1', linewidth=2)
plt.show()