import Agent
import Environment
import Object
import Cell
import numpy as np
import math

R = 40
C = 40
agentDens = 0.1 # Percent of objects on board 
objDens = 0.05 # Percent of agent on board
agentForce = 2
objWeight = 1


agentDensity = round(R * C * agentDens) # Number of agents depending on the size of the environment   
objectDensity = round(R * C * objDens) # Number objects depending on size of environment
# Cell1=Cell.Cell(123,1,1,1,1) # Initiate cell object

# print(Cell1.getr()) # Check cell

Env = Environment.Environment(R,C) # Initiate Environment

print(Env.getSize()) # Check environment

# Generate random list of non duplicate numbers of the same size of number of agents and objects
plcRand = np.random.randint(0, R, size = (2,agentDensity + objectDensity)) 
# plcC = np.random.randint(0, C, size = agentDensity + objectDensity)

agent = []
obj = []
indexRand = []
skip = []
dupFlag = True
print(len(plcRand[0]))

while dupFlag:
    count = 0
    for j in range(len(plcRand[0])):
        
        tempPlc = plcRand[:,j] 
          
        for k in range(len(plcRand[0])):
            if k != j:
                if plcRand[0, k] == tempPlc[0] and plcRand[1,k] == tempPlc[1]:
                    # print(k)
                    # print(j)
                    # print(tempPlc)
                    # print(plcRand[:,k])
                    plcRand[0,k] = int(np.random.randint(0, R, 1))
                    plcRand[1,k] = int(np.random.randint(0, R, 1))
                    count = count + 1
                    # print(count)
                    
    if count == 0:
        # print(count)
        dupFlag = False
    
    '''
    count = 0
    if j not in skip:

        
        xR = np.where(plcR == plcR[j])
        xC = np.where(plcC == plcC[j])
        
        for k in range(len(xC)):
            
            print(k)
            print(xC[k])
            
            if xC[k] in xR:
                print(xC[k])
                count = count + 1
            
            if count > 1:
                print(count)

'''

# print(agentDensity)
# print(np.size(plcC))

plcR = plcRand[0,:]
plcC = plcRand[0,:]

for i in range(len(plcR)):

    if i < agentDensity:
        
        agent.append(Agent.Agent(plcR[i], plcC[i], agentForce, Env))
        
    else:
        
        obj.append(Object.Object(Env,plcR[i],plcC[i],objWeight))
        
# print(plcR[50])
print(agent[10].getR())
print(agent[10].getC())

# print(agent[10].getNeighboorCellInfo()[0].getr())
# print(agent[10].getNeighboorCellInfo()[0].getc())
agent[10].move()

tempR = agent[10].getR()
tempC = agent[10].getC()

print(agent[10].getR())
print(agent[10].getC())

tempCell = Env.getCell(tempR + 1, tempC)
currPh = tempCell.getph()
print(currPh)

for i in range(len(agent)):
    for j in range(30):
        agent[10].beacon(1)
        tempCell = Env.getCell(tempR + 1, tempC)
        currPh = tempCell.getph()
        print(currPh)
        # print(j)
    # print(i)

for i in range(len(agent)):
    agent[10].beacon(0)
    print(i)

print("done")
'''
currPh = tempCell.getph()
print(currPh)

agent[10].beacon(0)
currPh = tempCell.getph()
print(currPh)
agent[10].beacon(0)
# print(obj[10].GetLocation())
'''



