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
from datetime import *
from dateutil.rrule import *
import calendar

#Units are in meters and seconds for diffusion, or years for time to corrosion
#Chloride content in in percent by mass of concrete
#Don't forget, numbering starts at [0]!



#Model geometry and discretization parameters
Lx = 0.3                            #Length
nx = 300                            #Number of discretizations
dx = Lx/nx                          #Length of discretizations
rebarDepth = .064/dx                #Depth of rebar, located by node
corrosionInitiation = 0.5           #Corrosion initiation threshold, cl%
mesh = Grid1D(nx = nx, Lx = Lx)     


#D0 = 1e-13
k = 5.
n = 0.3
porosity = 0.10


#Datetime construction to drive the simulation
castDate = date.today()             #Assumed cast date is current date 
time = Variable()
#time.setValue(28*24*60*60)                   
#simDate = Variable()
simDate = castDate                  #Initialize the simulation date
deicerMonth = [1,2,3,11,12]
exposureConcentration = Variable()

def salting(simDate):
    if simDate.month in deicerMonth:
        return 1.
    else:
        return 0.5

#Diffusion Parameters
#D0 = -4.829e-14 + 1.329e-10/(time/60/60/24)

aa = 6.26e-26
bb = 1.74e-20
D0 = np.sqrt(aa + bb/(time/60/60/24)**2)
#valueLeft = Variable()
#valueLeft = 0.
valueLeft = exposureConcentration
#valueLeft = 3 * (1 + numerix.sin(time))
valueRight = 0.0
background = 1e-6


#Creation of the variable to be solved for, phi, equal to the cl% 
phi = CellVariable(name="solution variable", mesh=mesh, value=background, hasOld=1)

#Write the diffusion equation 
eq = TransientTerm() == DiffusionTerm(coeff= D0 / (porosity * (1 + k * n * phi**(n-1))))

#Impose boundary conditions
phi.constrain(valueLeft, mesh.facesLeft)
#phi.constrain(valueRight, mesh.facesRight)

#Initialize a plot to view the results as calculations are made
if __name__ == '__main__':
     viewer = Viewer(vars=phi, datamin=0., datamax=1.)
     viewer.plot()
#     viewer2 = Viewer(vars=phi[50])
#     viwer2.plot()

#Initialize some loop tools
step = 0.
t = []
a = []


#Set the timestep interval
#timeStepDuration = 0.9 * dx**2 / (2 * D0)  #max stable timestep
timeStepDuration = 7*24*60*60 #one day timestep

#Timer to time solution process
start = timeit.default_timer()

#Solve the diffusion equation for the corrosion initiation at the depth of rebar
while phi[rebarDepth+dx] < corrosionInitiation:
#while time() < 10:    
    time.setValue(time() + timeStepDuration)
    simDate += timedelta(seconds = timeStepDuration) #will only work when timestep is greater than 1 day
    exposureConcentration.setValue(salting(simDate))

    # only move forward in time once per time step
    phi.updateOld()
   
    # but "sweep" many times per time step
    res = 1e+10    
    while res > 1e-6 :
        res = eq.sweep(var=phi,
                       dt=timeStepDuration)

    # and plot the converged solution for each timestep
    if __name__ == '__main__':
        viewer.plot()
#        plt.ion()
#        plt.plot(simDate, valueLeft, 'o-')
#        plt.draw()
        
    # then save the results of interest     
    step += 1
    t.append(step*timeStepDuration)
    a.append(float(phi[rebarDepth+dx]))

#Stop the timer
stop = timeit.default_timer()
print stop-start

#Manipulate results of interest
c = [float(j) for j in phi]
[float(i) for i in t]          
t = np.array(t)
t = t/60/60/24/365
a = np.array(a)
c = np.array(c)
x = mesh.cellCenters
x = np.transpose(x)
x = x[:,0]*1000

#Print the answer
print(c[rebarDepth+dx])
print(time)
print(t)
print(a)

#Save the results of each variable in single column text file for import into 
#post processing script
np.savetxt('x.txt', x, delimiter = ",")
np.savetxt('c.txt', c, delimiter = ",")
np.savetxt('t.txt', t, delimiter = ",")
np.savetxt('CAR.txt', a, delimiter = ",")



#______________________________________________________________________________

#Scheme to 'pickle' data for use in further calculations within this script
#    (f, filename) = dump.write({'concentration' : phi.value, 'time' : time.value}, extension = '.gz')
#data = dump.read(filename, f)
#concentration = data['concentration']
#time = data['time']


#Scheme to associate variables with mesh centers such that they can be operated
#xVar = CellVariable(mesh = mesh, name = 'x', value = x)
#yVar = CellVariable(mesh = mesh, name = 'Concentration', value = concentration)


#Scheme to stop simulation from ending upon completion
#if __name__ == '__main__':
#         raw_input("Solution Complete. \
# Press <return> to proceed...")

#Original loop with end command in loop
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
                 