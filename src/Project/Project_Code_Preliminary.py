# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:36:42 2021

@author: Bennett
"""

import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import numpy as np
import random

def Update_Locs():
    a=np.zeros([S,S])
    for er in range(len(agents)):
        rr=int(agents[er,0])
        cc=int(agents[er,1])
        a[rr,cc]=int(agents[er,2]) #red
    for er in range(len(objects)):
        rr=int(objects[er,0])
        cc=int(objects[er,1])
        a[rr,cc]=int(objects[er,2]) #black
    return a


def Check_Agent_Neighborhood(R,C,rng):
    P=0
    num_nabes=rng*rng-1
    neighbors=np.zeros([num_nabes, 3])
    kk=0
    Bnd=int((rng-1)/2)
    for rrr in range(-Bnd,Bnd+1): 
        
        for ccc in range(-Bnd,Bnd+1):

            if rrr!=0 or ccc!=0:
                
                neighbors[kk][0]=R+rrr
                neighbors[kk][1]=C+ccc
                kk=kk+1

    # neighbors = np.array([[R-1,C-1,P], [R-1,C,P], [R-1,C+1,P], \
    #                       [R,C-1,P],              [R,C+1,P], \
    #                       [R+1,C-1,P], [R+1,C,P], [R+1,C+1,P]])
    ZZ=np.ones([num_nabes,3])
    ind=0
    
    ObjFound=False
    for neighbor in neighbors:
        

        RRR=int(neighbor[0])
        CCC=int(neighbor[1])

        # make sure cells aren't on edge
        if RRR<0 or RRR>=S or CCC<0 or CCC>=S:
            ZZ[ind,2]=0
        #Check if the cell is occupied
        elif Phys_Map[RRR,CCC]!=0:
            ZZ[ind,2]=0
            if Phys_Map[RRR,CCC]==2:
                idxx=np.where((objects[:,0]==RRR) & (objects[:,1]==CCC))
                AdjObj_ID=idxx[0][0]
                ObjFound=AdjObj_ID
                return neighbors, ObjFound
        else: 
            PROB=Pmon_Map[RRR, CCC]
            neighbor[2]=PROB
    
        ind=ind+1

    neighbors[:,2]=(neighbors[:,2]+abs(min(neighbors[:,2]))+1)
    neighbors=neighbors*ZZ
    neighbors[:,2]=neighbors[:,2]/sum(neighbors[:,2])

    return neighbors, ObjFound    
def MOVE(agent):
    R=agent[0]
    C=agent[1]
    rng=3
    neighborhood=Check_Agent_Neighborhood(R,C,rng)
    neighbors=neighborhood[0]
    ObjFound=neighborhood[1]
    if ObjFound!=False: #Dont Move
        AdjObj_ID=ObjFound
        agent[0]=R 
        agent[1]=C
        agent[3]=1 # change agent to retrieval mode
        agent[4]=AdjObj_ID
    else: #Move
        move_loc=np.random.choice(len(neighbors),p=neighbors[:,2])
        agent[0]=neighbors[move_loc,0]
        agent[1]=neighbors[move_loc,1]
        agent[5]=1
    return agent

# def BeaconProp(agent,strength):
#     wt=agent[6]


#SxS grid envirorment
S = 70
#Number of agents
N=20
#Number of objects
O=20

#create agent matrix
agents=np.ones([N,8]) #ID x [row_location, col_location, color_of_agent, mode, ID of attached object, 0 for hasn't moved 1 for moved, wt, Beacon Range]
start_rows=range(S-15,S)
start_cols=range(S)
agents[:,0]=np.random.randint(S-15,S,size=(N,))
agents[:,1]=np.random.choice(start_cols,size=(N,),replace=False)
agents[:,3]=0 #mode
agents[:,4]=None #Attached object ID
agents[:,5]=0 #Move indicator
agents[:,6]=0 #wait time
agents[:,7]=1 #beacon range 
#create object matrix
objects=np.ones([O,5])*2 #ID x [row_location, col_location, color_of_agent, weight, Number of agents or Force]
start_rows=range(0,S-16)
start_cols=range(S)
objects[:,0]=np.random.randint(0,S-16,size=O)
objects[:,1]=np.random.choice(start_cols,size=O,replace=False)#,replace=False)
objects[:,3]=np.random.choice(range(0,9),size=(O,))*-1
objects[:,4]=0
#create Pheromone Map
Pmon_Map=np.zeros([S,S])

tf=1000

Phys_Map=Update_Locs()

for ID in range(len(agents)):
    R=agents[ID,0]
    C=agents[ID,1]
    color=agents[ID,2]
    mode=agents[ID,3]

rng = np.random.default_rng()
plt.grid()



#cmap = ListedColormap(['w', 'r', 'k']) 
RepulsiveStrength=-50
BeaconStrength=20
DecayRate=-1
WaitTime=5
for t in range(tf):
    agents[:,5]=0 
    for agent in agents:
        ar=int(agent[0])
        ac=int(agent[1])
        #aclr=agent[2]
        mode=agent[3] #0=search. 1=retrieval, 2=homing
        AdjObjID=agent[4] 
        MoveCheck=agent[5] 
        wt=agent[6]
        PropRng=agent[7]
        if MoveCheck==0:
            if mode==0:
                Pmon_Map[ar,ac]=RepulsiveStrength #agent drops repulive pheromone in Pmon_Map
                Phys_Map[ar,ac]=0 #vacate cell in Physical map
                agent=MOVE(agent) # move agent
                nr=int(agent[0])
                nc=int(agent[1])
                Pmon_Map[nr,ac]=RepulsiveStrength/2
                Pmon_Map[ar,nc]=RepulsiveStrength/2
                Phys_Map[nr,nc]=1 #place agent in new cell of Physical map
            # elif mode==1:
            #     #check and see if object can be moved.
            #     F=np.count_nonzero(agents[:,4]==AdjObjID)
            #     ObjWeight=objects[AdjObjID,3]
            #     if F>=ObjWeight: #move the object
            #         rty='ty'
            #     else: #drop beacon
            #         #BeaconProp(agent,BeaconStrength)
            #         wt=wt+1
            #         if wt>=WaitTime:
            #             agent[6]=0
            #             agent[7]=PropRng+1
            #         for cel in Pmon_Map([ar-PropRng:ar+PropRng+1],[ac-PropRng:ac+PropRng+1]):
                        
                
        
        
    Pmon_Map=Pmon_Map+DecayRate*np.sign(Pmon_Map)    
        
        
        

    fig,ax = plt.subplots()
    
    cmap=plt.cm.PiYG
    norm=colors.TwoSlopeNorm(vmin=Pmon_Map.min()-0.1,vcenter=0,vmax=Pmon_Map.max()+0.1)
    rgba=cmap(norm(Pmon_Map))
    
    obj_r=np.int_(objects[:,0]) #row locations of objects
    obj_c=np.int_(objects[:,1])  #column locations of objects 
    agent_r=np.int_(agents[:,0]) #row locations of agents
    agent_c=np.int_(agents[:,1]) #column locations of agents
    rgba[obj_r, obj_c, :3] = 0, 0, 0 #make objects black
    rgba[agent_r, agent_c, :3] = 1, 0, 0 #make agents white
    
    im = ax.imshow(rgba, interpolation='nearest')
    im2 = ax.imshow(Pmon_Map, cmap=cmap, norm=norm)
    cbar = plt.colorbar(im2, ax=ax)
    im2.set_alpha(0.0)
    plt.show()
         
    

    
    
    
    
        

    