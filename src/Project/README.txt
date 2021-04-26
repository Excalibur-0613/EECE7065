Self-Organizing Search and Retrieve Cellular Automata
Authors: Bennet Breese, Ethan Fitz, Benjamin Russ
Submitted 4/25/2021
This project is a Cellular Atoumata based simulation of a swarm of agents performing a search and retrieval task.
The simulation is started by running 'mainTest.py'.  The code runs the simulation, creates a series of epoch plots and prints the numbers of epochs, objects recoverd, total objects, and total agents.
Critical files: 'mainTest.py'  'Cell.py'  'Environment.py'  'Object.py'  'Agent.py'
These files should be located in the same folder for the code to run properly.
Tunable parameters:
In 'mainTest.py', the environment size, agent and object placement density, object maximum weight, pheromone decay rate, and agent push strength can be changed.
In 'Agent.py', the initial strength of the repulsive pheromone trail, and the growth rate of attractive pheromone (beacon) propagation can be changed.