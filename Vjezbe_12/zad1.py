import numpy as np
import matplotlib.pyplot as plt
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

svemir.trajectory(2.4)

fig, axs = plt.subplots()
axs.set_aspect("equal")
axs.plot(earth.listaX, earth.listaY)
axs.scatter(sun.listaX, sun.listaY, color = "yellow")
axs.plot(mercury.listaX, mercury.listaY)
axs.plot(venus.listaX, venus.listaY)
axs.plot(mars.listaX, mars.listaY)

axs.scatter(earth.listaX[-1], earth.listaY[-1])
axs.scatter(sun.listaX[-1], sun.listaY[-1], color = "yellow")
axs.scatter(mercury.listaX[-1], mercury.listaY[-1])
axs.scatter(venus.listaX[-1], venus.listaY[-1])
axs.scatter(mars.listaX[-1], mars.listaY[-1])
plt.show()