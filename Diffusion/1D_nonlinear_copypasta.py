# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 00:29:38 2015

@author: Timothy
"""

from fipy import*

nx = 50
dx = 1.
L = nx * dx
mesh = Grid1D(nx = nx, dx = dx)


valueLeft = 1.
valueRight = 0.
#phi = CellVariable(name="solution variable",
#                  mesh=mesh,
#                  value=valueRight,
#                  hasOld=1)
phi = [
     CellVariable(name="solution variable",
                  mesh=mesh,
                  value=valueRight,
                  hasOld=1),
     CellVariable(name="1 sweep",
                  mesh=mesh),
     CellVariable(name="2 sweeps",
                  mesh=mesh),
     CellVariable(name="3 sweeps",
                  mesh=mesh),
     CellVariable(name="4 sweeps",
                  mesh=mesh)
 ]
phiAnalytical = CellVariable(name="analytical value",
                              mesh=mesh) 
 
D0 = 1.
eq = TransientTerm() == DiffusionTerm(coeff=D0 * (1 - phi[0]))

phi[0].constrain(valueRight, mesh.facesRight)
phi[0].constrain(valueLeft, mesh.facesLeft)

x = mesh.cellCenters[0]
phiAnalytical.setValue(1. - numerix.sqrt(x/L))

timeStepDuration = 0.9 * dx**2 / (2 * D0)
steps = 100

if __name__ == '__main__':
     viewer = Viewer(vars=phi + [phiAnalytical],
                     datamin=0., datamax=1.)
     viewer.plot()
     
for sweeps in range(1,5):
     phi[0].setValue(valueRight)
     for step in range(steps):
         # only move forward in time once per time step
         phi[0].updateOld()
         
         # but "sweep" many times per time step
         for sweep in range(sweeps):
             res = eq.sweep(var=phi[0],
                            dt=timeStepDuration)
         if __name__ == '__main__':
             viewer.plot()
             
     # copy the final result into the appropriate display variable
     phi[sweeps].setValue(phi[0])
     if __name__ == '__main__':
         viewer.plot()
         raw_input("Implicit variable diffusity. %d sweep(s). \
 Residual = %f. Press <return> to proceed..." % (sweeps, (abs(res))))
 
eq = DiffusionTerm(coeff=D0 * (1 - phi[0]))

phi[0].setValue(valueRight)
res = 1e+10
while res > 1e-6:
     res = eq.sweep(var=phi[0],
                    dt=timeStepDuration)


print phi[0].allclose(phiAnalytical, atol = 1e-1)
1

if __name__ == '__main__':
     viewer.plot()
#     raw_input("Implicit variable diffusity - steady-state. \
# Press <return> to proceed...")

#image:: mesh1Dvariable.*
#   :width: 90%
#   :align: center
#   :alt: solution to a diffusion problem a non-linear diffusivity
   


