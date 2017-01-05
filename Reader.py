import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# DOES NOT CLOSE PROPERLY WHEN TRUE, TRY TO FIX THAT
REPEAT = True


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
#plt.ion()
#ax = fig.add_subplot(111, projection='3d')
ax = fig.add_subplot(111, projection='3d')
ax.has_been_closed = False
ax.set_axis_bgcolor('black')
n = 100
figsizeX = 10000
figsizeY = 10000
figsizeZ = 10000
plt.xlim([-figsizeX, figsizeX])
plt.ylim([-figsizeY, figsizeY])
ax.set_zlim(bottom=-figsizeZ, top=figsizeZ, emit=True, auto=False)

particle_num = 0
plt.tick_params(axis='both', color='r', labelcolor='r')

def on_close(event):
    event.canvas.figure.axes[0].has_been_closed = True


ax.xaxis.label.set_color('red')
ax.yaxis.label.set_color('red')
ax.zaxis.label.set_color('red')

fig.canvas.mpl_connect('close_event', on_close)

def updateplot(iteration,xs,ys,zs):
    ax.clear()
    ax.autoscale(enable=False)
    ax.set_xlabel('(pc)')
    ax.set_ylabel('(pc)')
    ax.set_zlabel('(pc)')

    ax.text2D(0.05, 0.95, "Iteration: " + repr(iteration), transform=ax.transAxes, color='red')
    ax.text2D(0.05, 0.90, "Particles: " + repr(particle_num), transform=ax.transAxes, color='red')
    ax.scatter(xs, ys, zs, c='r', marker='o', s=5)
    plt.pause(0.001)


def read_sim():
    with open('sim_data.txt', 'r') as f:
        iter = -1

        xs = []
        ys = []
        zs = []

        for line in f:

            if ax.has_been_closed:
                break

            if line.startswith("HEAD:"):
                particle_num = int(line[15:])
                continue

            data = line.split(',')
            i = data[0]
            if i != iter:
                iter = i
                updateplot(iter, xs, ys, zs)

                xs = []
                ys = []
                zs = []

            x = float(data[1])
            y = float(data[2])
            z = float(data[3])
            xs.append(x)
            ys.append(y)
            zs.append(z)


read_sim()
while REPEAT:
    read_sim()

plt.close()