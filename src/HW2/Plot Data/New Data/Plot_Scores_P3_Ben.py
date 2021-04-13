import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import numpy as np
import random
# from tabulate import tabulate
# import plotly.graph_objects as go
epochs=20
agents=1400
rg=range(0,agents*epochs,agents)

hap3 = np.load('P3_Ben_mean.npy')
hap2 = np.load('P1_Ben_mean.npy')
SD3=np.load('P3_Ben_sd.npy')
std3=np.zeros([len(rg),5])
#sort SD's by epoch
epoch=np.array(range(1,epochs+1))
for CS in range(0,5):
    k=-1
    for ii in rg:
        k=k+1
        std3[k,CS]=SD3[CS,ii]
std3=np.round(std3,decimals=4) 

#Create Table
headers=['Epoch P3 - BR','o = 0.05','o = 0.25', \
         'o = 0.5', 'o = 0.75', 'o = 0.95']
val = np.zeros([epochs,len(headers)])
val[:,0]=epoch
val[:,1:len(headers)]=std3
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
maxVals = np.zeros(5)
diffs = np.zeros(4)
for i in range(0,5):
    maxVals[i] = max(hap3[i,:])
    if i != 0:
        diffs[i-1] = abs(max(hap3[i,:]) - max(hap3[i-1,:]))
print(maxVals)
print(diffs)

P3=hap3[0,:]
# P2=hap12[-1,:]
# P3=hap3[-1,:]
t=range(len(P3))

plt.figure(dpi=600)
plt.plot(t,hap2[0,:],label='Policy 1 (q = 100)')
plt.plot(t,hap3[0,:],label='Policy 3 (o = 0.05)')
plt.plot(t,hap3[1,:],label='Policy 3 (o = 0.25)')
plt.plot(t,hap3[2,:],label='Policy 3 (o = 0.5)')
plt.plot(t,hap3[3,:],label='Policy 3 (o = 0.75)')
plt.plot(t,hap3[4,:],label='Policy 3 (o = 0.95)')

plt.grid()
plt.ylabel('Mean Happiness')
plt.xlabel('time step')
plt.legend()
plt.title('Mean Happiness vs. Time')
plt.savefig('P1P2.png', dpi=600)

'''
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

'''