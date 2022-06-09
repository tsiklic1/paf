from matplotlib import artist
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
import random

# fig, ax = plt.subplots()

# ax.set(xlim =(-0.1, 2*np.pi + 0.1), ylim=(-1.1, 1.1))

# line, = ax.plot([], [])

# x = np.linspace(0, 2*np.pi, num = 50)
# y = np.sin(x)

# def animate(i):
#     line.set_data(x[:i], y[:i])
#     return line,

# anim = FuncAnimation(fig, animate, frames = len(x) + 1, interval = 30, blit = True)
# plt.show()

fig = plt.figure()
l, = plt.plot([], [], "k-")

plt.xlim(-5, 5)
plt.ylim(-5, 5)

def func(x):
    return np.sin(x) * 3

metadata = dict(title="Movie", artist = "artist")
writer = PillowWriter(fps=15, metadata=metadata)

xlist = []
ylist = []

with writer.saving(fig, "sinwave.gif", 100):
    for xval in np.linspace(-5,5,200):
        xlist.append(xval)
        ylist.append(func(xval))

        l.set_data(xlist, ylist)

        writer.grab_frame()

# plt.scatter(sun.listaX[i], sun.listaY[i], color=sun.color)

            # plt.plot(mercury.listaX[:i], mercury.listaY[:i], color=mercury.color)
            # plt.scatter(mercury.listaX[i], mercury.listaY[i], color=mercury.color)

            # plt.plot(venus.listaX[:i], venus.listaY[:i], color=venus.color)
            # plt.scatter(venus.listaX[i], venus.listaY[i], color=venus.color)

            # plt.plot(earth.listaX[:i], earth.listaY[:i], color=earth.color)
            # plt.scatter(earth.listaX[i], earth.listaY[i], color=earth.color)

            # plt.plot(mars.listaX[:i], mars.listaY[:i], color=mars.color)
            # plt.scatter(mars.listaX[i], mars.listaY[i], color=mars.color)

