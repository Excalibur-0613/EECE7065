#Environment Class is composed of Cell objects.
# Has a constructor for environments of R by C cells
# Has setters and getters for each attribute of a cell at a specified position
# Has a global pheromone update function

import Cell

class environment:
    
    def __init__(self, R=5, C=5):       #This sets up an 'array' of cell objects of arbitrary size
        self._row_size = R
        self._column_size = C
        self._cell_array = []
        
        for row in range(R):
            self._cell_array.append([])
            for location in range(C):
                self._cell_array[row].append(Cell.cell(row,location, 0,0,0))        #This creates one new empty cell object in each possible location
        
    def getSize(self):
        Size = [self._row_size, self._column_size]
        return Size
    
    def getCell(self, row, col):        #This should expose a particular cell object so the attributes can be changed via the cell class's methods
        return self._cell_array[row][col]
    
    def GlobalPhDelta(self, PhChange):  #This should be helpful for pheromone decay.  Negative PhChange will decrease pheromone levels.  Will not decrease pheromone below 0.
        for row in range(self._row_size):
            for location in range(self._column_size):
                oldPh = self._cell_array[row][location].getph()
                if (oldPh + PhChange) > 0:
                    self._cell_array[row][location].updateCellPh(oldPh + PhChange)
                    



