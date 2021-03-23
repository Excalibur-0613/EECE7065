import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import numpy as np

def score(R,C,color):
    neighbors = np.array([[R-1,C-1], [R-1,C], [R-1,C+1], \
                          [R,C-1],            [R,C+1], \
                          [R+1,C-1], [R+1,C], [R+1,C+1]])%S
    score=0
    for neighbor in neighbors:
        if a[int(neighbor[0]),int(neighbor[1])]==color:
            score=score+1

    return score

def Rand_Empties(R,C,Q,Current_Score):
    R=int(R)
    C=int(C)
    color=agent[ID,2]
    qr=np.arange(S)
    qc=np.arange(S)
    np.random.shuffle(qr)
    np.random.shuffle(qc)
    best_R=R
    best_C=C
    best_score= current_score
    q=0
    
    for rr in qr:
        for cc in qc:
            if a[rr,cc]==0:
                q=q+1
                empty_score=score(rr,cc,color)
                
                if empty_score>=k:
                    a[R,C]=0
                    a[rr,cc]=color
                    agent[ID,0]=rr
                    agent[ID,1]=cc
                    return
                elif best_score>current_score:
                    best_R=rr
                    best_C=cc
                    best_score=empty_score
    a[R,C]=0
    a[best_R,best_C]=color
    agent[ID,0]=best_R
    agent[ID,1]=best_C
    return
    
                           
k=3
nFrames=10
fDelay = 20 
#SxS grid envirorment
S = 40
#Number of agents
N=1400
q=100

#intialize population and envirorment
a = np.zeros((S,S))
a[0,1:4] = [0,1,2] 
reds=np.ones(int(N/2)) #number of reds (agent)
blues=2*np.ones(int(N/2)) #number of blues (agent)
whites=np.zeros(S*S-N) #number of whites (empty)
a=np.hstack((reds,blues,whites)) # concatinate reds whites and blues
np.random.shuffle(a) # random shuffle
a=np.reshape(a,(S,S)) # reshape to matrix

cmap = ListedColormap(['w', 'b', 'r']) #define [0 1 2] as [white blue red]
# a[0:3,0:3]=1
# a[1,1]=2
plt.matshow(a,cmap=cmap) #plot matrix

#create agent matrix
ID=0
agent=np.zeros([N,3])
for er in np.arange(S):
    for ec in np.arange(S):
        if a[er,ec] != 0:
            agent[ID, 0]=er
            agent[ID, 1]=ec
            agent[ID, 2]=a[er,ec]
            ID=ID+1



epochs=N
tf= epochs*70
t=0
# ID=

while t<=tf:
    epoch=0
    print(epoch)
    while epoch<epochs:
        
        AgentOrder=np.arange(N)
        np.random.shuffle(AgentOrder)
        
        for n in range(N):
            ID=AgentOrder[n]
            r=agent[ID,0]
            c=agent[ID,1]
            color=agent[ID,2]
            current_score=score(r,c,color)
            
            if current_score<k:
                Rand_Empties(r,c,q,current_score)
                
                    
                plt.pause(0.01)
                plt.matshow(a,cmap=cmap) 
                plt.title(t)
                plt.show() 
            epoch=epoch+1
            t=t+1
        # print(t)
            
    


                    

       
        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    







