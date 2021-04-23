import Environment
import numpy as np
# Agent Object 

class Agent():
    
    def __init__(self, r, c, f, E):
        self._env = E
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
            if neighborCellPosition[0] < self._env.getSize()[0] and neighborCellPosition[1] < self._env.getSize()[0]:
                # Pass neighboor cell positions to getCellInfo method
                tempCell = self._env.getCell(neighborCellPosition[0], neighborCellPosition[1])
                self.neighborInfo.append(tempCell)
            
        # self.setCellProb()
        pass
        # return self.neighborInfo
    
    def setNeighborProb(self):
        
        self.neighborProb = []
        self.phVals = []
        self.prob = []
        self.probSum = 0
        
        for i in range(len(self.neighborInfo)):
            
            self.phVals.append(self.neighborInfo[i].getph())
            
        # print(self.phVals)
        self.neighborMin = min(self.phVals)
        
        for cellInfo in self.neighborInfo:
            self.probSum = self.probSum + (sum(self.phVals) + abs(self.neighborMin) + 1)
            self.prob.append(sum(self.phVals) + abs(self.neighborMin) + 1)
         
        self.neighborProb = [x / self.probSum for x in self.prob]   
        
        pass
    
    def move(self):
        
        self.getNeighboorCellInfo()
        self.setNeighborProb()
        
        rng = np.random.default_rng()
        testList = np.array([0,1,2,3,4,5,6,7])
        p = self.neighborProb
        index = rng.choice(testList,1,p)
        self.newPose = self.neighborPose[int(index)]
        r = self.newPose[0]
        c = self.newPose[1]
        
        self._placementSuccess = False
        #Check validity and occupancy, then move
        if r in range(self._env.getSize()[0]) and c in range(self._env.getSize()[1]): #row and col are in bounds
            TargetCell = self._env.getCell(r,c) #pick target cell
        else:
            return False #error - invalid location
        
        #Check occupancy before moving
        if TargetCell.getobj() == 0 and TargetCell.getagent() == 0:
            
            self._CurrentCell.updateCellObj(0) #Update the environment
            TargetCell.updateCellObj(1)
            
            self._CurrentCell = TargetCell #record the update
            self._currentRow = r
            self._currentCol = c
            
            self._placementSuccess = True
            return True #Object successfully moved
        else:
            return False #error - target cell is occupied by agent or other object
    
    
    def PlacementSuccess(self):
        return self._placementSuccess  
    
    
    
    
    
    
        
        