#The Object Class - an object has location and weight. It acts on an Environment
#The move and apply physics functions respect environment bounds and cell occupancy
#Most methods return a boolean (True for success and False for fail)
#If the force in its cell meets or exceeds the object's weight, the object will try to move in the direction of the force


import numpy as np
import math
from Environment import Environment

class Object(Environment):
    
    def __init__(self, E, r, c, w=1):  #The environment, initial location, and weight must be specified to make an Object
        self._env = E
        self._currentRow = r
        self._currentCol = c
        self._weight = w
        self._hiding = False
        
        #Init can't return anything, but we want to know whether the object got placed properly
        #So we need a flag variable
        
        self._placementSuccess = False
        
        #We must check for valid location before updating the environment
        
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
            
   
    def Move(self, r, c):
        
        self._placementSuccess = False
        #Check validity and occupancy, then move
        if r in range(self._env.getSize()[0]) and c in range(self._env.getSize()[1]): #row and col are in bounds
            TargetCell = self._env.getCell(r,c) #pick target cell
        else:
            return False #error - invalid location
        
        #Check occupancy before moving
        if TargetCell.getobj() == 0 and TargetCell.getagent() == 0 and not self._hiding:
            
            self._CurrentCell.updateCellObj(0) #Update the environment
            TargetCell.updateCellObj(1)
            
            self._CurrentCell = TargetCell #record the update
            self._currentRow = r
            self._currentCol = c
            
            self._placementSuccess = True
            return True #Object successfully moved
        else:
            return False #error - target cell is occupied by agent or other object
        
   
    def ApplyPhysics(self):
        targetRow = self._currentRow
        targetCol = self._currentCol
        Forces = self._CurrentCell.getforces()
        
        if Forces[0] >= self._weight:  #if row force exceeds weight, object will displace by one row
            targetRow += 1
        elif Forces[0] <= -self._weight:
            targetRow -= 1
            
        if Forces[1] >= self._weight:  #if col force exceeds weight, object will displace by one column
            targetCol += 1
        elif Forces[1] <= -self._weight:
            targetCol -= 1
        
        return self.Move(targetRow,targetCol)  #will return true if Move succeeds or if no move is required
        
    def GetLocation(self):
        return [self._currentRow, self._currentCol]
    
    def GetWeight(self):
        return self._weight
    
    def PlacementSuccess(self):
        return self._placementSuccess 
    
    def hide(self, visible):
        self._hiding = visible
        if self._hiding == True:
           self._CurrentCell.updateCellObj(0)
        else:
            self._CurrentCell.updateCellObj(1)
    