# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:52:20 2021

@author: Bennett
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import numpy as np
import random
epochs=20
agents=1400
rg=range(0,agents*epochs,agents)

hap12=np.load('P1P2mean.npy')
SD12=np.load('P1P2sd.npy')
std12=np.zeros([7,len(rg)])

hap13=np.load('P1P3mean.npy')
SD13=np.load('P1P3sd.npy')
std13=np.zeros([7,len(rg)])

for CS in range(6):
    k=-1
    for ii in rg:
        k=k+1
        std12[CS,k]=SD12[CS,ii]
        std13[CS,k]=SD13[CS,ii]
    




P1=hap12[0,:]
P2=hap12[-1,:]
P3=hap13[-1,:]
t=range(len(P1))

plt.figure(dpi=600)
plt.plot(t,P1,label='Policy 1 (q=100)')
plt.plot(t,P2,label='Policy 2 (n=20, p=3)')
plt.plot(t,P3,label='Policy 3 (n=20, p=3)')
plt.grid()
plt.ylabel('Mean Happiness')
plt.xlabel('time step')
plt.legend()
plt.title('Policy Comparison')
plt.savefig('P1P2P3.png', dpi=600)

plt.figure(dpi=600)
plt.plot(t,hap12[0,:],label='Policy 1 (q=100)')
plt.plot(t,hap12[1,:],label='Policy 2 (n=5, p=3)')
plt.plot(t,hap12[2,:],label='Policy 2 (n=5, p=5)')
plt.plot(t,hap12[3,:],label='Policy 2 (n=10, p=3)')
plt.plot(t,hap12[4,:],label='Policy 2 (n=10, p=5)')
plt.plot(t,hap12[5,:],label='Policy 2 (n=20, p=3)')
plt.plot(t,hap12[6,:],label='Policy 2 (n=20, p=5)')
plt.grid()
plt.ylabel('Mean Happiness')
plt.xlabel('time step')
plt.legend()
plt.title('Mean Happiness vs. Time')
plt.savefig('P1P2.png', dpi=600)

plt.figure(dpi=600)
plt.plot(t,hap13[0,:],label='Policy 1 (q=100)')
plt.plot(t,hap13[1,:],label='Policy 3 (n=5, p=3)')
plt.plot(t,hap13[2,:],label='Policy 3 (n=5, p=5)')
plt.plot(t,hap13[3,:],label='Policy 3 (n=10, p=3)')
plt.plot(t,hap13[4,:],label='Policy 3 (n=10, p=5)')
plt.plot(t,hap13[5,:],label='Policy 3 (n=20, p=3)')
plt.plot(t,hap13[6,:],label='Policy 3 (n=20, p=5)')
plt.grid()
plt.ylabel('Mean Happiness')
plt.xlabel('time step')
plt.legend()
plt.title('Mean Happiness vs. Time')
plt.savefig('P1P3.png', dpi=600)