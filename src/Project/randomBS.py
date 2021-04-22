import numpy as np

plcR = np.random.randint(5, size = (2,5)) 
# plcC = np.random.randint(0, 5, 20)

skip = []

# xR = np.where(plcR == 4)
# xC = np.where(plcC == 2)
rng = np.random.default_rng()

test = int(np.random.randint(0,40, 1))

# print(plcR)
# print(plcR[:,0])
# print(xC)
testList = np.array([0,1,2,3,4,5,6,7])
p = [0.3,0.3,0.06667,0.06667,0.06667,0.06667,0.06667,0.06667]
print(testList)
index = rng.choice(testList,1,p)

print(index)