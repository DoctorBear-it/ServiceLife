# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:35:31 2016

@author: Timothy
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.optimize import curve_fit

#def saturationFunction(wc,V_paste,n=3.28,phi=0.13,gel_cond=0.20):
    
S = np.linspace(0,1,101)


n = 3.28
phi = 0.15
gel_cond = 0.22
F_S = ((1/(1+(S/(1-phi))**(-4*n)))+gel_cond)*(1-gel_cond)*(1+(1/(1-phi))**(-4*n))

def newSaturationFunction(S,n,phi,gel_cond):
    return ((1/(1+(S/(1-phi))**(-4*n)))+gel_cond)*(1-gel_cond)*(1+(1/(1-phi))**(-4*n))
xdata1 = S
ydata1 = F_S
popt1,pcov1 = curve_fit(newSaturationFunction,xdata1,ydata1) #,maxfev=100000

#snick_est = F_S/(1-phi)-gel_cond
#snick_est_ratechange = np.diff(snick_est)
#S_snick_est = S[1:]

fig1 = plt.figure(figsize=(8,8))
ax1 = plt.subplot(111)
ax1.plot(S, F_S,linewidth=2)
ax1.set_xlim(0,1)
ax1.set_ylim(0,1)
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'
ax1.tick_params(which='major',labelsize=22,length=10,width=2,direction='out', pad=10) #direction='inout'
ax1.tick_params(which='minor',labelsize=22,length=5,width=1,direction='out',pad=10)
[i.set_linewidth(2) for i in ax1.spines.itervalues()]    
ax1.set_xlabel(r'Degree of Saturation [$S$]',fontsize=22)
ax1.set_ylabel(r'Saturation Function [$f(S)$]',fontsize=22)


#doh = np.linspace(0,1,101)
doh = 0.8    
densityWater = 1000.
densityCement = 3150.
wc = 0.40
V_air = np.linspace(0,0.10,11)
V_paste = 0.25

P_i = wc/(wc+densityWater/densityCement)

S_nick = []
S_sealed = []
S_gel = []
V_voids = []

for j in V_air:
    nick = (P_i - 0.5*(1-P_i)*doh)/(P_i-0.5*(1-P_i)*doh + (j/V_paste))  
    sealed = (P_i - 0.7*(1-P_i)*doh)/(P_i-0.7*(1-P_i)*doh + (j/V_paste)) 
    gel = (0.8*(1-P_i)*doh)/(P_i-0.5*(1-P_i)*doh + (j/V_paste)) 
    voids = P_i-0.5*(1-P_i)*doh + (j/V_paste)  
    
    S_nick.append(nick)
    S_sealed.append(sealed)
    S_gel.append(gel)      
    V_voids.append(voids)
       
#    fig2 = plt.figure(figsize=(8,8))
#    ax2 = plt.subplot(111)
#    ax2.plot(doh,S_nick,'r',doh,S_sealed,'g',doh,S_gel,'b')
#    ax2.set_xlim(0,1)
#    ax2.set_ylim(0,1)
#    
S_nick = np.array(S_nick)
S_sealed = np.array(S_sealed)
S_gel = np.array(S_gel)
V_voids = np.array(V_voids)

air_matrix_norm_cond = np.logspace(0,3,50) #Equal to cond_air/cond_matrix

phi_a = (V_air/V_paste)/V_voids
normalized_cond = []
for air in phi_a:
    ans = (1+2*air*(((air_matrix_norm_cond)-1)/((air_matrix_norm_cond)+2)))\
                    /(1-air*(((air_matrix_norm_cond)-1)/((air_matrix_norm_cond)+2)))
    normalized_cond.append(ans)

cond_mult = np.amax(normalized_cond,axis=1)
norm_cond_mult = 1/cond_mult
 

fig3 = plt.figure(figsize=(8,8))
ax3 = plt.subplot(111)
for j,jj in enumerate(normalized_cond):
    ax3.plot(jj,air_matrix_norm_cond,linewidth=2,label='Air Content = %s' %'{}%'.format(100*V_air[j]))
ax3.set_xscale('linear')
ax3.set_yscale('log')
ax3.set_xlim(1,5)
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'
ax3.tick_params(which='major',labelsize=22,length=10,width=2,direction='out', pad=10) #direction='inout'
ax3.tick_params(which='minor',labelsize=22,length=5,width=1,direction='out',pad=10)
ax3.grid(True)
[i.set_linewidth(2) for i in ax3.spines.itervalues()]
#ax3.set_title('Conductive Air Void Estimations')
ax3.set_xlabel(r'Normalized Effective Composite Conductivity [$\mathbf{\frac{\sigma_e}{\sigma_m}}$]',fontsize=22)
ax3.set_ylabel(r'Normalized Conductivity [$\mathbf{\frac{\sigma_a}{\sigma_m}}$]',fontsize=22)
plt.legend(loc="lower right",fontsize=22,fancybox=True,bbox_to_anchor=(1.65,0))
#for t1 in ax3.get_yticklabels():
#    t1.set_color('b')
#    
#ax4 = ax3.twinx()
#ax4.plot('','','r')
#ax4.set_ylabel('')
#for t1 in ax4.get_yticklabels():
#    t1.set_color('r')

#plt.tight_layout()

def func(Sat,nn):
    return Sat**nn
xdata = S_nick
ydata = norm_cond_mult
popt,pcov = curve_fit(func,xdata,ydata)

fig4 = plt.figure(figsize=(8,8))
ax4 = plt.subplot(111)
ax4.plot(S_nick,norm_cond_mult,'-x',S,func(S,popt[0]),linewidth=2)
ax4.set_xlim(0,1)
ax4.set_ylim(0,1)
rcParams['mathtext.fontset'] = 'stix'
rcParams['font.family'] = 'STIXGeneral'
ax4.tick_params(which='major',labelsize=22,length=10,width=2,direction='out', pad=10) #direction='inout'
ax4.tick_params(which='minor',labelsize=22,length=5,width=1,direction='out',pad=10)
[i.set_linewidth(2) for i in ax4.spines.itervalues()]    
ax4.set_xlabel(r'Degree of Saturation at the "Nick" Point [$S_n$]',fontsize=22)
ax4.set_ylabel(r'Normalized Effective Conductivity [$\mathbf{\frac{\sigma^*_s}{\sigma_s}}$]',fontsize=22)

plt.show()
    
    #return 