import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def init():
    plot.set_data(a)
    return [plot]

def update(frames):
    plcn = rng.integers(low=0, high=n, size=1)
    plcm = rng.integers(low=0, high=n, size=1)
    #bit = rng.integers(low=0, high=2, size=1)
    a[plcn,plcm] = not(a[plcn,plcm])
    # print(np.array([plcn,plcm,bit]))
    # print(a)
    
    
    cmap=plt.cm.RdYlGn
    norm = plt.Normalize(a.min(), a.max())
    rgba=cmap(norm(a))
    obj_r=range(2) #row locations of objects
    obj_c=range(2) #column locations of objects 
    agent_r=5 #row locations of agents
    agent_c=5 #column locations of agents
    rgba[obj_r, obj_c, :3] = 0, 0, 0 #make objects black
    rgba[agent_r, agent_c, :3] = 1, 1, 1 #make agents white
    plot.set_data(rgba)
    return [plot]

nFrames=10
fDelay = 20 
n = 10
a = np.zeros((n,n))
a[0,0] = 1

rng = np.random.default_rng()


# fig = plt.figure()
fig,ax = plt.subplots()



plot = ax.imshow(a)#, interpolation='nearest')


#plot = ax.imshow(a)
#ax = plt.axes(xlim=(0,n),ylim=(0,n))
# plot = plt.matshow(a, fignum=0)

ani = FuncAnimation(fig, update, frames=nFrames,
                    init_func=init, interval=fDelay,repeat=False, blit=True)
plt.show(block=False)

print('saving')
# ani.save('robot.gif', fps = 60)
ani.save('robot.gif', writer='pillow', fps=120)
print('Done')




