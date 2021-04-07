# Agent Object 



class agent:
    
    
    
    def __init__(self, pose):
        self._pose = pose
        
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
        for element in neighborPose:
            self.neighborInfo.append(getCellInfo(element))
        
        # Check in with environment and create 8 
        # objects of the cell to include within the lists
        # with the correct information
    
    def getCellInfo(pose):
        
        pass
        # call environment methods to get specific cell information
    
    def setValProb(self, agentProb, objectProb, phProb, beaconProb):
        self._agentProb = 1
        self._objectProb = 1
        self._phProb = 1
        self._beaconProb = 1
        
    def getValProb():
        return [_agentProb, _objectProb, _phProb, _beaconProb]
    
    def setCellProb():
        for element in neightborInfo:
            for info in cellInfo:
                if info[0] == 'Object':
                    
                    
                else if info[0] == 'Ph':
                
                
                else if info[0] == 'Agent':
                
        pass
        
    def move():
        
        
        