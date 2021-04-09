#Environment Class is composed of Cell objects.
# Has a constructor for environments of R by C cells
# Has setters and getters for each attribute of a cell at a specified position
# Has a global pheromone update function

import numpy as np
import math
import Cell
import Agent
import Object

class Environment(Cell):
    
    def __init__(self, R=10, C=10):       #This sets up an 'array' of cell objects of arbitrary size, should be larger than 10x10
        self._row_size = R
        self._column_size = C
        self._cell_array = []
        
        for row in range(R):
            self._cell_array.append([])
            for location in range(C):
                self._cell_array[row].append(Cell(row,location, 0,0,0))        #This creates one new empty cell object in each possible location
    
        self._agentDensity = math.floor((self._row_size * self._column_size)/7) # Number of agents depending on the size of the environment   
        self._objectDensity = math.floor((self._row_size * self._column_size)/20) # Number objects depending on size of environment
        
        # Generate random list of non duplicate numbers of the same size of number of agents and objects
        plcR = np.random.randint(R, size = self._agentDensity + self._objectDensity, repeat = False) 
        plcC = np.random.randint(C, size = self._agentDensity + self._objectDensity, repeat = False)
        
        for i in range(len(plcR)):

            if i < self._agentDensity:
                self.agent[i] = Agent.Agent([plcR[i],plcC[i]])
                updateCellAgent()
                
            else:
                self.object[i - self._agentDensity] - Object.Object(plcR,plcC) 
        
    
    def getSize(self):
        Size = [self._row_size, self._column_size]
        return Size
    
    # This should expose a particular cell object so the attributes can be changed via the cell class's methods
    def getCell(self, row, col):        
        return self._cell_array[row][col]
    
    # This should be helpful for pheromone decay.  Negative PhChange will decrease pheromone levels.  Will not decrease pheromone below 0.
    def GlobalPhDelta(self, PhChange):  
        for row in range(self._row_size):
            for location in range(self._column_size):
                oldPh = self._cell_array[row][location].getph()
                if (oldPh + PhChange) > 0:
                    self._cell_array[row][location].updateCellPh(oldPh + PhChange)
                    

    

