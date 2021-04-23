# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 16:14:58 2021

@author: ethan

Let's put the pieces together to run the simulation
"""

#import libraries

import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import numpy as np
import random

#import simulation components

from Cell import Cell
from Environment import Environment
from Object import Object
from Agent import Agent

#Set simulation parameters

PlottingEnabled = True

R = 70
C = 70

agentDens = 0.01 # Percent of agents on board 
objDens = 0.005 # Percent of objects on board
agentForce = 1 #How hard an agent pushes objects toward the South
objMaxWeight = 3 #Upper weight limit for objects

agentAmount = round(R * C * agentDens) # Number of agents depending on the size of the environment   
objectAmount = round(R * C * objDens) # Number objects depending on size of environment
goalZoneDepth = round(R * 0.1)  #The southernmost rows are the 'goal zone'

phDecay = -0.2  #pheromone decay rate

epochLimit = 100 #Simulation will stop after this many full rounds

#Create Environment

Env = Environment(R, C)


#Generate lists of initial locations - repeats will be handled when constructors are called

objectStartRows = np.random.randint(0, R-goalZoneDepth, size = (1, objectAmount))
objectStartCols = np.random.randint(0, C, size = (1, objectAmount))

#objectStartLocations = np.vstack((objectStartRows, objectStartCols))

agentStartRows = np.random.randint(0, R, size = (1, agentAmount))
agentStartCols = np.random.randint(0, C, size = (1, agentAmount))

#agentStartLocations = np.vstack((agentStartRows, agentStartCols))

#Create list of Ojects on the Env

objList = []

for i in range(objectAmount):
    objList.append(Object(Env, objectStartRows[0,i], objectStartCols[0,i], np.random.randint(2, objMaxWeight+1)))
    attempt = 0
    while (not objList[-1].PlacementSuccess()) and attempt < 5: #relocate conflicting placements
        objList[-1].Move(np.random.randint(0, R-goalZoneDepth), np.random.randint(0, C))
        attempt += 1
        

#Create list of Agents on the Env

agentList = []

for i in range(agentAmount):
    agentList.append(Agent(agentStartRows[0,i], agentStartCols[0,i], agentForce, Env, R-goalZoneDepth))
    attempt = 0
    while (not objList[-1].PlacementSuccess()) and attempt < 5: #agents move out of conflicting placements
        agentList[-1].move()
        attempt += 1
    


#Initialize Simulation Loop

done = False

epoch = 0

t = 0

retrievedObjects = 0
listOfRetrieved = []

agentTurnOrder = np.arange(agentAmount)
np.random.shuffle(agentTurnOrder)

plt.grid()

while not done:
    

    #Increment Epoch counter    
    epoch += 1
    if epoch >= epochLimit:
        done = True
        
    #Agents move and push in random order
    np.random.shuffle(agentTurnOrder)
    for a in range(agentAmount):
        agentList[agentTurnOrder[a]].takeTurn()
        t += 1
   
    #Objects try to move
    for o in range(objectAmount):
        objList[o].ApplyPhysics()
    
        
    #Cleanup - clear forces, decay pheromones, count and hide retrieved objects
    Env.GlobalForcesClear()
    Env.GlobalPhDelta(phDecay)
    for o in range(objectAmount):
        pos = objList[o].GetLocation()
        if pos[0] >= R - goalZoneDepth and o not in listOfRetrieved:
            retrievedObjects += 1
            listOfRetrieved.append(o)
            objList[o].hide(True)  #This hides retrieved objects from the agents by turning them invisible
    
    if retrievedObjects == objectAmount:
        done = True
    
    
    if PlottingEnabled:
        #Plot ph, agents, and objects
        Pmon_Map=Env.getPhMap()   
            
    
        fig,ax = plt.subplots()
        
        cmap=plt.cm.PiYG
        norm=colors.TwoSlopeNorm(vmin=Pmon_Map.min()-0.1,vcenter=0,vmax=Pmon_Map.max()+0.1)
        rgba=cmap(norm(Pmon_Map))
        
        obj_r = np.zeros([objectAmount,1])
        obj_c = np.zeros([objectAmount,1])
        
        for o in range(objectAmount):
            pos = objList[o].GetLocation()
            obj_r[o] = pos[0]
            obj_c[o] = pos[1]
        
        agent_r = np.zeros([agentAmount,1])
        agent_c = np.zeros([agentAmount,1])
        
        for a in range(agentAmount):
            agent_r[a] = agentList[a].getR()
            agent_c[a] = agentList[a].getC()
        
        obj_r = np.int_(obj_r) #row locations of objects
        obj_c = np.int_(obj_c)  #column locations of objects 
        agent_r = np.int_(agent_r) #row locations of agents
        agent_c = np.int_(agent_c) #column locations of agents
        
        rgba[obj_r, obj_c, :3] = 0, 0, 0 #make objects black
        rgba[agent_r, agent_c, :3] = 1, 0, 0 #make agents white
        
        im = ax.imshow(rgba, interpolation='nearest')
        im2 = ax.imshow(Pmon_Map, cmap=cmap, norm=norm)
        cbar = plt.colorbar(im2, ax=ax)
        im2.set_alpha(0.0)
        plt.show()
    
#Output results summary

print(epoch)
print(retrievedObjects)
print(objectAmount)


#THE END
