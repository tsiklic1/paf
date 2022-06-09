import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import universe as universe
from matplotlib.animation import PillowWriter
import math

au = 1.496 * 10**(11)
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", "yellow", 1.989 * 10**30, np.array((0.,0.)), np.array((0.,0.)))
mercury = universe.Planet("Merkur", "brown", 3.3 * 10**24, np.array((0., 0.466*au)), np.array((-47362., 0.)))
venus = universe.Planet("Venus", "black", 4.8685*10**24, np.array((0.723*au, 0.)), np.array((0., 35020.)))
earth = universe.Planet("Earth", "blue", 5.9742 * 10**24, np.array((float(-1. * au), 0.)), np.array((0., float(-29783))))
mars = universe.Planet("Mars","red", 6.417*10**23, np.array((0., -1.666*au)), np.array((24007., 0.)))


svemir = universe.Universe()
svemir.add_planet(earth)
svemir.add_planet(sun)
svemir.add_planet(mercury)
svemir.add_planet(venus)
svemir.add_planet(mars)

svemir.trajectory(1)

fig = plt.figure()

metadata = dict(title="Movie", artist = "Toma")
writer = PillowWriter(fps=15, metadata=metadata)

with writer.saving(fig, "universe.gif", 100):
    for i in range(len(mercury.listaX)):
        if i%5 == 0:
            plt.clf()
            for j in svemir.planets:
                
                plt.plot(j.listaX[:i], j.listaY[:i], color =j.color)
                plt.scatter(j.listaX[i], j.listaY[i], color=j.color)

            plt.xlim(-2*au, 2*au)
            plt.ylim(-2*au, 2*au)

            writer.grab_frame()


