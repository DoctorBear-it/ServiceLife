# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:15:37 2015

@author: Timothy
"""
from fipy import*
import math
import numpy as np
import matplotlib.pyplot as plt
import pprint
from fipy.tools import dump 
import timeit

#Units are in meters and seconds for diffusion, or years for time to corrosion
#Chloride content in in percent by mass of concrete
#Don't forget, numbering starts at [0]!
start = timeit.default_timer()
Lx = 0.3
nx = 300
dx = Lx/nx
rebarDepth = .064/dx
corrosionInitiation = 0.5
mesh = Grid1D(nx = nx, Lx = Lx)

D0 = 3e-12
k = 5.
n = 0.3
porosity = 0.10

time = Variable()
month = Variable()

if month > 11:
    valueLeft = 3.
elif month < 2:
    valueLeft = 3.
else: 
   valueLeft = 0.0 
#valueLeft = 3 * (1 + numerix.sin(time))
valueRight = 0.0
background = 1e-6

phi = CellVariable(name="solution variable", mesh=mesh, value=background, hasOld=1)

eq = TransientTerm() == DiffusionTerm(coeff= D0 / (porosity * (1 + k * n * phi**(n-1))))

phi.constrain(valueLeft, mesh.facesLeft)
#phi.constrain(valueRight, mesh.facesRight)

if __name__ == '__main__':
     viewer = Viewer(vars=phi, datamin=0., datamax=1.)
     viewer.plot()
#     viewer2 = Viewer(vars=phi[50])
#     viwer2.plot()

step = 0
t = []
a = []
timeStepDuration = 0.9 * dx**2 / (2 * D0)  #max stable timestep
#timeStepDuration = 12*60*60 #half day timestep
while phi[rebarDepth+dx] < corrosionInitiation:
#while time() < 10:    
    time.setValue(time() + timeStepDuration)
    month = time()/60/60/24/365*12
    # only move forward in time once per time step
    phi.updateOld()
   
    # but "sweep" many times per time step
    res = 1e+10    
    while res > 1e-6 :
        res = eq.sweep(var=phi,
                       dt=timeStepDuration)

    if __name__ == '__main__':
        viewer.plot()
    
#    (f, filename) = dump.write({'concentration' : phi.value, 'time' : time.value}, extension = '.gz')
    step += 1
    t.append(step*timeStepDuration)
    a.append(float(phi[rebarDepth+dx]))

c = [float(j) for j in phi]
[float(i) for i in t]          
t = np.array(t)
t = t/60/60/24/365
a = np.array(a)
c = np.array(c)
stop = timeit.default_timer()
print stop-start
#data = dump.read(filename, f)
#concentration = data['concentration']
#time = data['time']
print(c[rebarDepth+dx])
print(time)
print(t)
print(a)
x = mesh.cellCenters
x = np.transpose(x)
x = x[:,0]*1000


#delimiter = ","
np.savetxt('x.txt', x, delimiter = ",")
np.savetxt('c.txt', c, delimiter = ",")
np.savetxt('t.txt', t, delimiter = ",")
np.savetxt('CAR.txt', a, delimiter = ",")

#xVar = CellVariable(mesh = mesh, name = 'x', value = x)
#yVar = CellVariable(mesh = mesh, name = 'Concentration', value = concentration)


#pprint.pprint(a)

#plt.plot(x[:], concentration[:], 'x--', linewidth = 2)
#plt.show()

#viewer2 = MatplotlibViewer(vars =[x,concentration])
#viewer2.plot()

#if __name__ == '__main__':
#         raw_input("Solution Complete. \
# Press <return> to proceed...")



#    concentration = np.array(print(phi[rebarDepth+1]))    
#    m += 1     
#    elapsedTime = np.array(time.value)
#
#plt.plot(time, concentration)
#plt.show()

#while time() < 100:
#    time.setValue(time() + timeStepDuration)
#    # only move forward in time once per time step
#    phi.updateOld()
#         
#    # but "sweep" many times per time step
#    res = 1e+10    
#    while res > 1e-6 :
#        res = eq.sweep(var=phi,
#                       dt=timeStepDuration)
#    if __name__ == '__main__':
#        viewer.plot()
#    if phi[49] == 0.5:
#        end
                 