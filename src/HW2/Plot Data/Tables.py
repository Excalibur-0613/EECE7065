# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:16:49 2021

@author: Bennett
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import numpy as np
import random
from tabulate import tabulate
epochs=20
agents=1400
rg=range(0,agents*(epochs)-1,agents)
P1P2=np.load('Saved_Sim_ScoresP1P2.npy')
hap12mean=np.mean(P1P2,axis=)
hap12std=np.std(P1P2,axis=0)
std12=np.zeros([len(rg)])
mean12=np.zeros([len(rg)])
epoch=range(0,epochs)
print(epoch)
k=-1
for ii in rg:
    k=k+1
    std12[k]=hap12std[ii]
    mean12[k]=hap12mean[ii]
    

plt.plot(rg,std12)