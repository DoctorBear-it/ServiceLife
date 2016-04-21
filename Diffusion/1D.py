# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:55:52 2015

@author: Timothy
"""

from fipy import*
from matplotlib import pylab as plt

nx = 50
dx = 1.0
mesh = Grid1D(nx=nx, dx=dx)

phi = CellVariable(name="solution variable", mesh=mesh, value = 0.0)

D = 1

valueLeft = 1.0
valueRight = 0.0

phi.constrain(valueRight, mesh.facesRight)
phi.constrain(valueLeft, mesh.facesLeft)

eqX = TransientTerm() == ExplicitDiffusionTerm(coeff=D)

timeStepDuration = 0.9 * dx**2 / (2 * D)
steps = 100

phiAnalytical = CellVariable(name = "analytical value", mesh = mesh)

viewer = Viewer(vars = (phi, phiAnalytical), datamin = 0., datamax = 1.)
viewer.plot()

x = mesh.cellCenters[0]
t = timeStepDuration*steps

try:
     from scipy.special import erf 
     phiAnalytical.setValue(1 - erf(x / (2 * numerix.sqrt(D * t)))) 
except ImportError:
     print "The SciPy library is not available to test the solution to \
 the transient diffusion equation"

for step in range(steps):
    eqX.solve(var=phi, dt=timeStepDuration)
    viewer.plot()
    
print phi.allclose(phiAnalytical, atol = 7e-4)
1

