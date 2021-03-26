import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import numpy as np
import random

def score(R,C,color):
    neighbors = np.array([[R-1,C-1], [R-1,C], [R-1,C+1], \
                          [R,C-1],            [R,C+1], \
                          [R+1,C-1], [R+1,C], [R+1,C+1]])%S
    score=0
    for neighbor in neighbors:
        if a[int(neighbor[0]),int(neighbor[1])]==color:
            score=score+1

    return score

def Policy1(R,C):
    if current_score<k:
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
        Q=100
        q=0
        
        for rr in qr:
            for cc in qc:
                if q <= Q:
                    if a[rr,cc]==0:
                        q=q+1
                        empty_score=score(rr,cc,color)
                        
                        if empty_score>=k:
                            a[R,C]=0
                            a[rr,cc]=color
                            agent[ID,0]=rr
                            agent[ID,1]=cc
                            agent[ID,3]=empty_score
                            return
                        elif best_score>current_score:
                            best_R=rr
                            best_C=cc
                            best_score=empty_score
        a[R,C]=0
        a[best_R,best_C]=color
        agent[ID,0]=best_R
        agent[ID,1]=best_C
        agent[ID,3]=best_score
    return

def Define_Friends():
    n_friends = 10
    #define each agents friends
    agent_friends=np.zeros([N,n_friends])
    for n in range(N):
        agent_friends[n,:]=random.sample(range(N),n_friends)
    
    return agent_friends

def Policy2(R,C):

    counter=0
    friends=agent_friends[ID,:]
    relocation_positions='none'
    for friend in friends:
        relocation_position=Phone(friend)

        if relocation_position != 'none':
            if counter==0:
                relocation_positions=np.array(relocation_position)
                counter=1
            else:
                relocation_positions=np.vstack((relocation_positions, \
                                       relocation_position))
                
    #randomly select a move location
    if relocation_positions=='none':
        return
    else:
        if np.ndim(relocation_positions)==1:
            relocation_positions=np.array([relocation_positions])
        sel=random.sample(range(0,len(relocation_positions)),1)
        sel_R=relocation_positions[sel,0]
        sel_C=relocation_positions[sel,1]
        sel_score=relocation_positions[sel,2]
        a[R,C]=0
        a[sel_R,sel_C]=color
        agent[ID,0]=sel_R
        agent[ID,1]=sel_C
        agent[ID,3]=sel_score
    return

def Define_Friends_Same_Color():
    n_friends = 10
    #define each agents friends, friends must be same color
    agent_friends=np.zeros([N,n_friends])
    Friend_Ord=np.arange(N)
        
    for n in range(N):
        np.random.shuffle(Friend_Ord)
        current_friend=0
        nn=0
        while current_friend < n_friends:
            
            if agent[n,2] == agent[Friend_Ord[nn],2]: # if colors match
                agent_friends[n,current_friend]=Friend_Ord[nn]
                current_friend=current_friend+1
            nn=nn+1
    
    return agent_friends


def Phone(FRIEND):
    F=int(FRIEND)
    R=agent[F,0]
    C=agent[F,1]
    p_neighborhood = 3 #must be odd number, pxp matrix around friend
    ind=(p_neighborhood-1)/2
    #neighborhood = np.zeros(p_neighborhood**2-1,3) #friend x row,col,score
    ct=0
    neighborhood='none'
    for rr in range(int(R-ind),int(R+ind)):
        for cc in range(int(C-ind),int(C+ind)):
            # if r!=R and c!=C:
            # print(r)
            # print(c)
            r=rr%S
            c=cc%S
            if a[r,c]==0: #if friends neighborhood has vacancy, then score the vacany position
                empty_score = score(r,c,color)
                if empty_score>=k: # if empty score is greater than min, add it to the possible locations
                    if ct==0:
                        neighborhood=np.array([r,c,score(r,c,color)])
                        ct=1
                    else:
                        # asdf=np.array([r,c,score(r,c,color)])
                        
                        # if np.size(asdf)!=np.size(neighborhood[:,0]):
                        #         print('stop')
                                
                        neighborhood=np.vstack((neighborhood,np.array([r,c,score(r,c,color)])))
                
    
    return neighborhood


    
                           
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


#create agent matrix
ID=0
agent=np.zeros([N,4])
for er in np.arange(S):
    for ec in np.arange(S):
        if a[er,ec] != 0:
            agent[ID, 0]=er 
            agent[ID, 1]=ec
            agent[ID, 2]=a[er,ec] # color
            agent[ID, 3]=score(er,ec,a[er,ec]) #score
            ID=ID+1



t_epochs=N
total_epochs=20
tf= total_epochs*t_epochs
t=0
AgentOrder=np.arange(N)
np.random.shuffle(AgentOrder)
# plt.matshow(a,cmap=cmap) #plot matrix
# plt.title(t)
POLICY='BB'
epoch=0
scoreVepoch=np.zeros(total_epochs)
while t<=tf:
    if t>epoch*t_epochs:
        np.random.shuffle(AgentOrder)
        scoreVepoch[epoch]=agent[:,3].mean()
        
        plt.pause(0.01)

        
        plt.subplot(1,2,1)
        plt.plot(scoreVepoch)
        plt.grid()
        plt.xlabel('epoch')
        plt.ylabel('1e3/score')
        plt.subplot(1,2,2)
        plt.imshow(a,cmap=cmap) 
        plt.show()
        epoch=epoch+1
        
    for n in range(N):
        ID=AgentOrder[n]
        r=agent[ID,0]
        c=agent[ID,1]
        color=agent[ID,2]
        current_score=score(r,c,color)
        if POLICY==1:
            Policy1(r,c)
        elif POLICY==2:
            if t==0:
                agent_friends=Define_Friends()
            Policy2(int(r),int(c))
        elif POLICY=='BB':
            if t==0:
                agent_friends=Define_Friends_Same_Color()
                print(agent_friends)
            Policy2(int(r),int(c))
            
        # plt.matshow(a,cmap=cmap) #plot matrix
        # plt.title(t)
        # plt.show()
        t=t+1


# plt.matshow(a,cmap=cmap) 
# plt.title(epoch)

                    
# plt.plot(scoreVepoch)

        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    







