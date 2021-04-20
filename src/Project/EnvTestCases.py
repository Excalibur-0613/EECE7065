# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 10:57:28 2021

@author: ethan

Some Object test code - Looking at the variable explorer line-by-line and everything checks out so far.
"""

from Environment import Environment

from Object import Object

Env = Environment() #Create a default size 10 by 10 environment

TestObject = Object(Env, 1, 1, 2)  #Create an object at location 1,1

print(TestObject.PlacementSuccess())  #Placement works

print(TestObject.Move(2,2))  #Move to 2,2 - success returns true

print(TestObject.Move(100,100)) #Move to 100,100 - out of bounds, returns false, no changes made to Object or Environment

Obstacle = Object(Env, 3, 3, 2)  #Here is another object blocking cell 3,3

print(TestObject.Move(3,3))  #Test object will not move to 3,3 - refurns false

TestCell = Env.getCell(2,2)  #Pick out the Test Object's current cell

TestCell.updateCellForces([0,1])  #Some force, but not enough to move the test object

print(TestObject.ApplyPhysics())  #Test object should not move

TestCell.updateCellForces([0,7])  #That should be enough force to move the test object

print(TestObject.GetLocation())

print(TestObject.ApplyPhysics())  #Object moves

print(TestObject.GetLocation())   #New location is one cell South of old location

Env.GlobalForcesClear()  #Clear all forces

print(TestCell.getforces())  #Forces are cleared!



