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

    #define each agents friends
    agent_friends=np.zeros([N,n_friend])
    for nn in range(N):
        agent_friends[nn,:]=random.sample(range(N),n_friend)
    
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
    #define each agents friends, friends must be same color
    agent_friends=np.zeros([N,n_friend])
    Friend_Ord=np.arange(N)
        
    for n in range(N):
        np.random.shuffle(Friend_Ord)
        current_friend=0
        nn=0
        while current_friend < n_friend:
            
            if agent[n,2] == agent[Friend_Ord[nn],2]: # if colors match
                agent_friends[n,current_friend]=Friend_Ord[nn]
                current_friend=current_friend+1
            nn=nn+1
    
    return agent_friends


def Phone(FRIEND):
    F=int(FRIEND)
    R=agent[F,0]
    C=agent[F,1]
    ind=(p_neighbor-1)/2
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

t_epochs=N
total_epochs=1#20
tf= total_epochs*t_epochs

POLICIES=[1,3]
# n_friends=[5,10,20]
# p_neighborhood = [3,5] #must be odd number, pxp matrix around friend

scores=np.zeros([7,tf])
scores_SD=np.zeros([7,tf])
Current_Case=-1
simulations=1#30
for POLICY in POLICIES:
    if POLICY==1:
        n_friends=[1]
        p_neighborhood = [1]
    else:
        n_friends=[5,10,20]
        p_neighborhood = [3,5]
    for n_friend in n_friends:
        for p_neighbor in p_neighborhood:
            Current_Case=Current_Case+1
            sim_scores=np.zeros([simulations,tf])
            for sim in range(simulations):
                
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
                
                
                
                AgentOrder=np.arange(N)
                np.random.shuffle(AgentOrder)
                
                t=0
                epoch=0
                while t<tf:
                   
                    for n in range(N):
                        if t>epoch*t_epochs:
                            np.random.shuffle(AgentOrder)
                            epoch=epoch+1
                        sim_scores[sim,t]=agent[:,3].mean()
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
                        elif POLICY==3:
                            if t==0:
                                agent_friends=Define_Friends_Same_Color()
                                # print(agent_friends)
                            Policy2(int(r),int(c))
                            
                        t=t+1
            scores[Current_Case,:]=np.mean(sim_scores,axis=0)
            scores_SD[Current_Case,:]=np.std(sim_scores,axis=0)
            if POLICY==1:
                lbl='Policy %1i (q=%1i)' % (POLICY,q)
            elif POLICY==2:
                lbl='Policy %1i (n=%1i, p=%1i)' \
                    % (POLICY,n_friend,p_neighbor)
            elif POLICY==3:
                lbl='Policy %1i (n=%1i, p=%1i)' \
                    % (POLICY,n_friend,p_neighbor)
            plt.plot(scores[Current_Case,:],label=lbl)
            plt.plot(scores_SD[Current_Case,:],label=lbl)
# for CSS in range(1,7)
# plt.subplot(6,1,CSS)
# plt.plot(np.transpose(scores))
plt.grid()
plt.ylabel('Mean Happiness')
plt.xlabel('time step')
plt.legend()
plt.title('Mean Happiness vs. Time')

# plt.show()

        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    







