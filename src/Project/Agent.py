import Environment
# Agent Object 

class Agent():
    
    def __init__(self, pose, E):
        self.Environment = E
        self.Environment.getCellInfo()
        self._pose = pose
        self.getNeighboorCellInfo()
        
    def setPose(self, pose):
        self._pose = pose
        
    def getR(self):
        return self._pose(0)
    
    def getC(self):
        return self._pose(1)
        
    def getNeighboorCellInfo(self):
        
        self.neighborPose.clear()
        self.neighborInfo.clear()
        self.neighborPose.append([self.getR() + 1, self.getC()])     # North
        self.neighborPose.append([self.getR() + 1, self.getC() + 1]) # Northeast
        
        self.neighborPose.append([self.getR(), self.getC() + 1])     # East
        self.neighborPose.append([self.getR() - 1, self.getC() + 1]) # Southeast
        
        self.neighborPose.append([self.getR() - 1, self.getC()])     # South
        self.neighborPose.append([self.getR() - 1, self.getC() - 1]) # Southwest
        
        self.neighborPose.append([self.getR(), self.getC() - 1])     # West
        self.neighborPose.append([self.getR() + 1, self.getC() - 1]) # Northwest
    
        # Call into environment object 8 times to create a list of 8 elements with information for each neighboring cell
        for element in self.neighborPose:
            # Pass neighboor cell positions to getCellInfor method
            self.neighborInfo.append(self.getEnvCellInfo(element))
            Environment.getCell()
        self.setValProb()
        # Check in with environment and create 8 
        # objects of the cell to include within the lists
        # with the correct information
    
    def setValProb(self, agentProb, objectProb, phProb, beaconProb):
        # llst containing probabilities for different types of occupancy in neighbor cells
        
        self.probs = [agentProb, objectProb, phProb, beaconProb]
        self.setCellProb()
        
    def getValProb(self,accessProb):
            return self.probs[accessProb]
    
    def setCellProb(self):
        for cellInfo in self.neightborInfo:
            for data in cellInfo:
                for i in range(0, len(data)):
                    data[i] = self.probs[i]
        pass
        
    def move(self):
        
        
        
        self.getNeighboorCellInfo()
        pass
        
        