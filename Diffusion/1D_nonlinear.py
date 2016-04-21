# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:15:37 2015

@author: Timothy
"""
from fipy import*

nx = 50
dx = 1.
L = nx * dx
mesh = Grid1D(nx = nx, dx = dx)

D0 = 1.

#time = Variable()
#valueLeft = 0.5 * (1 + numerix.sin(time))
#phi.constrain(valueLeft, mesh.facesLeft)
#phi.constrain(0., mesh.facesRight)

valueLeft = 1.0
valueRight = 0.0



phi = CellVariable(name="solution variable",
                  mesh=mesh,
                  value=valueRight,
                  hasOld=1)


#eq = DiffusionTerm(coeff=D0 * (1 - phi[0]))
eq = TransientTerm() == DiffusionTerm(coeff=D0 * (1 - phi))

phi.constrain(valueRight, mesh.facesRight)
phi.constrain(valueLeft, mesh.facesLeft)

#dt = .1
#while time() < 15:
#     time.setValue(time() + dt)
#     eq.solve(var=phi, dt=dt)
#     if __name__ == '__main__':
#         viewer.plot()

#timeStepDuration = 10 * dx**2 / (2 * D0)
timeStepDuration = 0.9 * dx**2 / (2 * D0)
steps = 100

if __name__ == '__main__':
     viewer = Viewer(vars=phi, datamin=0., datamax=1.)
     viewer.plot()

#phi.setValue(valueRight)
for step in range(steps):
    # only move forward in time once per time step
    phi.updateOld()
     
    # but "sweep" many times per time step
    res = 1e+10    
    while res > 1e-6 :
        res = eq.sweep(var=phi,
                       dt=timeStepDuration)
    if __name__ == '__main__':
        viewer.plot()


#x = mesh.cellCenters[0]
#t = timeStepDuration*steps

                 