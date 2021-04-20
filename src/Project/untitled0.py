# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 09:11:43 2021

@author: Bennett
"""

import Cell

Cell1=Cell.Cell(123,1,1,1,1)
#Cell1.updateCellRow(123)
#val=Cell1.getr()
print(Cell1.getr())


#some environment test code

import Environment 

E = Environment.Environment(4,4)  #make a 4x4 environment
print(E.getSize())    #confirm size
print(E.getCell(3,0).getr())  #confirm cell 3,0 records its row as 3

E.getCell(3,0).updateCellRow(42)  #change cell 3,0's recorded location to row 42

print(E.getCell(3,0).getr())  #cell 3,0 now thinks that it is located in row 42

print(E.getCell(3,0).getph())

E.getCell(3,0).updateCellPh(666)

print(E.getCell(3,0).getph())  #now we can read and alter a cell's pheromone level

#Now that ph is a list, the global ph delta function needs reworked
#E.GlobalPhDelta(-7)  #pheromone can decay across the board

#print(E.getCell(3,0).getph()) #It seems to work

#print(E.getCell(3,1).getph()) #But negatave pheromone levels are impossible so the method will not bring ph level below 0
