import Environment
import numpy as np
# Agent Object 

class Agent():
    
    def __init__(self, r, c, f, E):
        
        self._currentRow = r
        self._currentCol = c
        self._force = f
        self._env = E
        
        #Init can't return anything, but we want to know whether the object got placed properly
        #So we need a flag variable
        
        self._placementSuccess = False
        
        # Status of beacon emission, use beacon method passing either 0 or 1
        
        self._beacon = False
        self.beaconRange = 0
        self._beaconPhDelta = 5 # How much beacon should increase ph at each epoch, tune as needed
        self.beaconPhStore = [] # Stored changes to cells from beacon
        
        # Memory of the last object position seen
        # i.e. an object is pushed at the end of the epoch and
        # no longer in immediate neighborhood
        
        self.storeObjPose = [None, None]
        
        #On initial call of move(), neighborInfo may be empty, so let's populate it before trying to index in
        self.getNeighboorCellInfo() # Make sure appropriate attributes are filled
        
        if self._currentRow in range(self._env.getSize()[0]) and self._currentCol in range(self._env.getSize()[1]): #row and col are in bounds
            
            self._CurrentCell = self._env.getCell(self._currentRow, self._currentCol) #pick current cell
        
        else:
            return #False #error - invalid location
        
        #Now we check occupancy before updating the environment
        if self._CurrentCell.getobj() == 0 and self._CurrentCell.getagent() == 0:
            
            self._CurrentCell.updateCellObj(1) #Update the environment
            self._placementSuccess = True
            
            return #True #Object successfully placed in Environment
        
        else:
            return #False #error - cell is occupied by agent or other object
        
    def getR(self):
        return self._currentRow
    
    def getC(self):
        return self._currentCol
    
    def updateAgentForce(self, f):
        return self._force
        
    def getNeighboorCellInfo(self):
        
        self.neighborPose = []
        self.neighborInfo = []
        
        self.neighborPose.append([self.getR() + 1, self.getC()])     # North
        self.neighborPose.append([self.getR() + 1, self.getC() + 1]) # Northeast
        
        self.neighborPose.append([self.getR(), self.getC() + 1])     # East
        self.neighborPose.append([self.getR() - 1, self.getC() + 1]) # Southeast
        
        self.neighborPose.append([self.getR() - 1, self.getC()])     # South
        self.neighborPose.append([self.getR() - 1, self.getC() - 1]) # Southwest
        
        self.neighborPose.append([self.getR(), self.getC() - 1])     # West
        self.neighborPose.append([self.getR() + 1, self.getC() - 1]) # Northwest
    
        # Call into environment object 8 times to create a list of 8 elements with information for each neighboring cell
        for neighborCellPosition in self.neighborPose:

            if neighborCellPosition[0] < self._env.getSize()[0] and neighborCellPosition[1] < self._env.getSize()[1] and neighborCellPosition[0] > 0 and neighborCellPosition[1] > 0:
                
                # Pass neighboor cell positions to getCellInfo method
                tempCell = self._env.getCell(neighborCellPosition[0], neighborCellPosition[1])
                self.neighborInfo.append(tempCell)
            
                # Store first object in array to remember (i.e. northernmost), ignore the others
                if self.neighborInfo[-1].getobj() and self.storeObjPose[0] == None and self.storeObjPose[1] == None:
                    
                    self.storeObjPose = [self.neighborInfo[-1].getr(), self.neighborInfo[-1].getc()]
                    
                elif self.neighborInfo[-1].getobj() and self.storeObjPose[0] != None and self.storeObjPose[1] != None:
                    
                    pass
    
    def setNeighborProb(self):
        
        self.neighborProb = []
        self.phVals = []
        self.prob = []
        self.probSum = 0
        
        for i in range(len(self.neighborInfo)):
            
            self.phVals.append(self.neighborInfo[i].getph())
            
        self.neighborMin = min(self.phVals) # take the minimum value of ph from the list 
        
        for cellInfo in self.neighborInfo:
            self.probSum = self.probSum + (sum(self.phVals) + abs(self.neighborMin) + 1) # Numerator
            self.prob.append(sum(self.phVals) + abs(self.neighborMin) + 1) # Denomonator
         
        self.neighborProb = [x / self.probSum for x in self.prob] # Probability vector for each neighbor cell   
        
        pass
    
    # Call this function to try and move the agent to a new position depending on 
    # current neighbor cell ph values. 
    # will return false if agent was unable to move successfully
    def move(self):
        
        
        
        # If object is directly north of object, i.e. "in the way" 
        # will only have probability to move towards SW or SE
        # Top priority case to avoid errors
        if self.neighborInfo[0].getobj() == 0:
            
            rng = np.random.default_rng()
            indexList = np.array([3,5]) # 2 possible neighbors to move towards
            index = rng.choice(indexList,1) # Choose which neighbor cell to go to
            self.newPose = self.neighborPose[int(index)] # Give new list of decided move location
            r = self.newPose[0]
            c = self.newPose[1]
        
        # If there was an object pushed in a previous time step, set the propability to move south 
        # will not trigger if there is another object directly south
        elif self.storeObjPose[0] != None and self.storeObjPose[1] != None:
            
            if self.recentPush and self.neighborInfo[4].getobj() == 0:
                
                self.getNeighboorCellInfo() # Make sure appropriate attributes are filled
                # self.setNeighborProb() # Make sure appropriate attributes are filled
                self.newPose = self.neighborPose[4] # Move south 
                r = self.newPose[0]
                c = self.newPose[1]
            
        # Regular Random Movement, no prior objects
        else : 
        
            self.getNeighboorCellInfo() # Make sure appropriate attributes are filled
            self.setNeighborProb() # Make sure appropriate attributes are filled
            
            rng = np.random.default_rng()
            indexList = np.array([0,1,2,3,4,5,6,7]) # 8 possible neighbors to move towards
            p = self.neighborProb # Array of probabilities
            index = rng.choice(indexList,1,p) # Choose which neighbor cell to go to
            self.newPose = self.neighborPose[int(index)] # Give new list of decided move location
            r = self.newPose[0]
            c = self.newPose[1]
            
        self._placementSuccess = False
        
        # Check validity and occupancy, then move
        if r in range(self._env.getSize()[0]) and c in range(self._env.getSize()[1]): #row and col are in bounds
        
            TargetCell = self._env.getCell(r,c) #pick target cell
            
        else:
            
            return False #error - invalid location
        
        # Check occupancy before moving
        if TargetCell.getobj() == 0 and TargetCell.getagent() == 0:
            
            self._CurrentCell.updateCellObj(0) #Update the environment
            TargetCell.updateCellObj(1)
            
            self._CurrentCell = TargetCell #record the update
            self._currentRow = r
            self._currentCol = c
            
            self._placementSuccess = True
            self.storeObjPose = [None, None]
            self.recentPush = False
            
            return True #Object successfully moved
            
        else:
            return False #error - target cell is occupied by agent or other object
        
    # Pass the cell location to add force to that cell position   
    def push(self, r, c):
        
        self.recentPush = False
        self.pushCell = self._env.getCell(r,c)
        
        if self.pushCell.getobj() == 1:
        
            currCellForce = self.pushCell.getCellForces() # Get the current force attatched to that cell
            newForce = currCellForce + self._force # Adds force attributed to the current agent to the selected cell
            self.pushCell.updateCellForces(newForce) # Pass new force after applied force is added
            self.recentPush = True
            
        else:
            return False #error - target cell is occupied by agent or other object
    
    def PlacementSuccess(self):
        return self._placementSuccess
    
    # Place beacon if object did not move from last time step
    # pass b = 1 to initially activate beacon
    # continue to pass b = 1 to expand the range of the beacon and update the beacon ph value
    # pass b = 0 to deactivate and remove all previously placed ph
    def beacon(self, b):

        # Stores locations of cells where ph is updated
        if b == 1:
            
            envSize = self._env.getSize()
            self._beacon = 1
            self.beaconPhStore = []
            self.cellPhPoses = []
            self.beaconRange = self.beaconRange + 1 # Every increase is one on top of the neighbor vision
            self.landMark = [self._currentRow + self.beaconRange, self._currentCol + self.beaconRange] # Start at northeast corner
            self.beaconSize = 2 * self.beaconRange + 3 # Square size of beacon matrix
            
            # 3x3 neighbor vision with 5x5 being min beacon area
            # Increases cell Ph by beaconPhDelta at each epoch
            for i in range(self.beaconSize):
                
                for j in range(self.beaconSize):
                    
                    cellUpdate = [self.landMark[0] - i, self.landMark[1] - j]
            
                    if cellUpdate[0] < envSize[0] and cellUpdate[1] < envSize[1] and cellUpdate[0] > 0 and cellUpdate[1] > 0:
                        
                        tempCell = self._env.getCell(cellUpdate[0],cellUpdate[1])
                        currPh = tempCell.getph()
                        newPh = currPh + self._beaconPhDelta
                        self.beaconPhStore.append(newPh)
                        tempCell.updateCellPh(newPh)
                        self.cellPhPoses.append(cellUpdate)
                        
                    else:
                        pass

            return True
        
        # Uses stored cell location and ph vals to remove beacon influence
        else:
            
            if self.beaconPhStore != []:
                storeIndex = 0
                envSize = self._env.getSize()  
                
                for elem in self.cellPhPoses:
                    
                    tempCell = self._env.getCell(elem[0],elem[1])
                    currPh = tempCell.getph()
                    newPh = currPh - self.beaconPhStore[storeIndex]
                    tempCell.updateCellPh(newPh) 
                    storeIndex = storeIndex + 1
                
            else:
                pass
              
            self.beaconRange = 0
            self.beaconPhStore = []
            
            return False
        
    # Call this to reset critical values for agent after the object is pushed to goal area
    def completedObjective(self):
        
        self.beacon(0)
        self.storeObjPose = [None, None]
        self.recentPush = False
            
    
    
    
    
    
        
        