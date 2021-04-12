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
from tabulate import tabulate
import plotly.graph_objects as go
epochs=20
agents=1400
rg=range(0,agents*epochs,agents)

hap12=np.load('P1P2mean.npy')
SD12=np.load('P1P2sd.npy')
std12=np.zeros([len(rg),7])

hap13=np.load('P1P3mean.npy')
SD13=np.load('P1P3sd.npy')
std13=np.zeros([len(rg),7])

#sort SD's by epoch
epoch=np.array(range(1,epochs+1))
for CS in range(0,7):
    k=-1
    for ii in rg:
        k=k+1
        std12[k,CS]=SD12[CS,ii]
        std13[k,CS]=SD13[CS,ii]
std12=np.round(std12,decimals=4) 
std13=np.round(std13,decimals=4) 

#Create Table
headers=['Epoch',' P1 q=100','n=5,p=3', \
         'n=5,p=5', 'n=10,p=3', \
         'n=10,p=5','n=20,p=3',  \
         'n=20,p=5']
val = np.zeros([epochs,len(headers)])
val[:,0]=epoch
val[:,1:len(headers)]=std13
fig, ax = plt.subplots() 
ax.set_axis_off() 

table = ax.table( 
    cellText = val,  
    #rowLabels = epoch,  
    colLabels = headers, 
    #rowColours =["palegreen"] * 10,  
    colColours =["palegreen"] * 9, 
    cellLoc ='center',  
    loc ='upper left')         
table.auto_set_font_size(False)
table.set_fontsize(7)
table.figure.dpi=300




P1=hap12[0,:]
P2=hap12[-1,:]
P3=hap13[-1,:]
t=range(len(P1))

plt.figure(dpi=600)
plt.plot(t,P1,label='Policy 1 (q=100)')
plt.plot(t,P2,label='Policy 2 (n=20, p=5)')
plt.plot(t,P3,label='Policy 3 (n=20, p=5)')
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