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
    plot.set_data(a)
    return [plot]

nFrames=1000
fDelay = 20 
n = 10
a = np.zeros((n,n))
a[0,0] = 1

rng = np.random.default_rng()

# fig = plt.figure()
fig,ax = plt.subplots()
plot = ax.matshow(a)
#ax = plt.axes(xlim=(0,n),ylim=(0,n))
# plot = plt.matshow(a, fignum=0)

ani = FuncAnimation(fig, update, frames=nFrames,
                    init_func=init, interval=fDelay,repeat=False, blit=True)
plt.show(block=False)

print('saving')
# ani.save('robot.gif', fps = 60)
ani.save('robot.gif', writer='pillow', fps=120)
print('Done')




