# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:09:32 2021

@author: Ben Russ
"""

import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation


n_frames = 3 #Numero de ficheros que hemos generado
data = np.empty(n_frames, dtype=object) #Almacena los datos

#Leer todos los datos
for k in range(n_frames):
    data[k] = np.loadtxt("frame"+str(k))


fig = plt.figure()
plot =plt.matshow(data[0], fignum=0)

def init():
    plot.set_data(data[0])
    return plot

def update(j):
    plot.set_data(data[j])
    return [plot]


anim = FuncAnimation(fig, update, init_func = init, frames=n_frames, interval = 30, blit=True)

plt.show()