#Environment Class is composed of Cell objects.
# Has a constructor for environments of R by C cells
# Has setters and getters for each attribute of a cell at a specified position
# Has a global pheromone update function and a global forces clear function

import numpy as np
import math
from Cell import Cell
#import Agent
#import Object

class Environment(Cell):
    
    def __init__(self, R=10, C=10):       #This sets up an 'array' of cell objects of arbitrary size, should be larger than 10x10
        self._row_size = R
        self._column_size = C
        self._cell_array = []
        
        for row in range(R):
            self._cell_array.append([])
            for location in range(C):
                self._cell_array[row].append(Cell(row,location, 0,0,0))        #This creates one new empty cell object in each possible location
    
       
        #This code probably belongs in main - The environment should not need to create agents and objects
        # self._agentDensity = math.floor((self._row_size * self._column_size)/7) # Number of agents depending on the size of the environment   
        # self._objectDensity = math.floor((self._row_size * self._column_size)/20) # Number objects depending on size of environment
        
        # # Generate random list of non duplicate numbers of the same size of number of agents and objects
        # plcR = np.random.randint(R, size = self._agentDensity + self._objectDensity, repeat = False) 
        # plcC = np.random.randint(C, size = self._agentDensity + self._objectDensity, repeat = False)
        
        # for i in range(len(plcR)):

        #     if i < self._agentDensity:
        #         self.agent[i] = Agent.Agent([plcR[i],plcC[i]])
        #         updateCellAgent()
                
        #     else:
        #         self.object[i - self._agentDensity] - Object.Object(plcR,plcC) 
        
    
    def getSize(self):
        Size = [self._row_size, self._column_size]
        return Size
    
    # This should expose a particular cell object so the attributes can be changed via the cell class's methods
    def getCell(self, row, col):        
        return self._cell_array[row][col]
    
    # This should be helpful for pheromone decay.  Negative PhChange will decrease pheromone levels.  Will not decrease pheromone below 0.
    # Will need rework if ph is set to be a list
    def GlobalPhDelta(self, PhChange):  
        for row in range(self._row_size):
            for location in range(self._column_size):
                oldPh = self._cell_array[row][location].getph()
                if (oldPh + PhChange) > 0:
                    self._cell_array[row][location].updateCellPh(oldPh + PhChange)
                    
    #This will return the force values in each cell back to 0,0. Force is supposed to be momentary, so should be cleared at the end of each timestep
    def GlobalForcesClear(self):  
        for row in range(self._row_size):
            for location in range(self._column_size):
                self._cell_array[row][location].updateCellForces([0,0])
                    

    

