# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:15:37 2015

@author: Timothy
"""
from fipy import*

nx = 50
dx = 0.5
L = nx * dx
mesh = Grid1D(nx = nx, dx = dx)

D0 = 1.

time = Variable()
valueLeft = 0.5 * (1 + numerix.sin(time))
valueRight = 0.0

phi = CellVariable(name="solution variable",
                  mesh=mesh,
                  value=valueRight,
                  hasOld=1)

eq = TransientTerm() == DiffusionTerm(coeff=D0 * (1 - phi))

phi.constrain(valueLeft, mesh.facesLeft)
phi.constrain(valueRight, mesh.facesRight)

if __name__ == '__main__':
     viewer = Viewer(vars=phi, datamin=0., datamax=1.)
     viewer.plot()

timeStepDuration = 0.9 * dx**2 / (2 * D0)
while time() < 100:
    time.setValue(time() + timeStepDuration)
    # only move forward in time once per time step
    phi.updateOld()
         
    # but "sweep" many times per time step
    res = 1e+10    
    while res > 1e-6 :
        res = eq.sweep(var=phi,
                       dt=timeStepDuration)
    if __name__ == '__main__':
        viewer.plot()



                 