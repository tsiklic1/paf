import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import universe as universe

au = 1.496 * 10**(11)
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", 1.989 * 10**30, np.array((0.,0.)), np.array((0.,0.)))
mercury = universe.Planet("Merkur", 3.3 * 10**24, np.array((0., 0.466*au)), np.array((-47362., 0.)))
venus = universe.Planet("Venus", 4.8685*10**24, np.array((0.723*au, 0.)), np.array((0., 35020.)))
earth = universe.Planet("Earth", 5.9742 * 10**24, np.array((float(-1. * au), 0.)), np.array((0., float(-29783))))
mars = universe.Planet("Mars", 6.417*10**23, np.array((0., -1.666*au)), np.array((24007., 0.)))


svemir = universe.Universe()
svemir.add_planet(earth)
svemir.add_planet(sun)
svemir.add_planet(mercury)
svemir.add_planet(venus)
svemir.add_planet(mars)

svemir.trajectory(1)

fig = plt.figure()

lines = plt.plot([])
line = lines[0]
plt.xlim(-1.1*au, 1-1*au)
plt.ylim(-1.1*au, 1.1*au)

def animate(frame):
    x = earth.listaX[frame]
    y = earth.listaY[frame]
    line.set_data((x, y))
    return line,

anim = animation.FuncAnimation(fig, animate, 100, )
plt.show()

# fig, axs = plt.subplots()
# axs.set_aspect("equal")
# axs.plot(earth.listaX, earth.listaY)
# axs.scatter(sun.listaX, sun.listaY, color = "yellow")
# axs.plot(mercury.listaX, mercury.listaY)
# axs.plot(venus.listaX, venus.listaY)
# axs.plot(mars.listaX, mars.listaY)
# plt.show()