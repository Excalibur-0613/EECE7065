import Environment
# Agent Object 

class Agent():
    
    def __init__(self, r, c, f, E):
        self._env = E # self.Environment.getCellInfo()
        
        self._currentRow = r
        self._currentCol = c
        self._force = f
        
        #Init can't return anything, but we want to know whether the object got placed properly
        #So we need a flag variable
        
        self._placementSuccess = False
        
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
        
    # def setPose(self, pose):
        # self._pose = pose
        
    def getR(self):
        return self._currentRow
    
    def getC(self):
        return self._currentCol
        
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
            # Pass neighboor cell positions to getCellInfo method
            tempCell = self._env.getCell(neighborCellPosition[0], neighborCellPosition[1])
            self.neighborInfo.append(tempCell)
            
        # self.setCellProb()
        
        return self.neighborInfo
        
        # Check in with environment and create 8 
        # objects of the cell to include within the lists
        # with the correct information
    
    def setValProb(self, agentProb, objectProb, phProb, beaconProb):
        # list containing probabilities for different types of occupancy in neighbor cells
        
        self._probs = [agentProb, objectProb, phProb, beaconProb]
        self.setCellProb()
        
    def getValProb(self, accessProb):
            return self._probs[accessProb]
    
    def setCellProb(self):
        
        self.neighborMin = min(min(self.neighborInfo, key=min))
        
        for cellInfo in self.neighborInfo:
            self.probSum = self.probSum + (sum(cellInfo) + abs(self.neighborMin) + 1)
            self.prob.append(sum(cellInfo) + abs(self.neighborMin) + 1)
            
        self.neighborProb = self.prob/self.probSum
        
        pass
        
    def move(self, newPose):
        
        # Pheremone equation?
        self.setPose(newPose)
        
        self.getNeighboorCellInfo()
        pass
        
        