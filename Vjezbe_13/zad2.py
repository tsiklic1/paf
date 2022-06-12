import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import universe as universe
from matplotlib.animation import PillowWriter
import math

au = 1.496 * 10**(11)
day = 60*60*24
year = 365.242*day

sun = universe.Planet("Sun", "yellow", 1.989 * 10**30, np.array((0.,0.)), np.array((0.,0.)), 696340000)
mercury = universe.Planet("Merkur", "brown", 3.3 * 10**24, np.array((0., 0.466*au)), np.array((-47362., 0.)))
venus = universe.Planet("Venus", "black", 4.8685*10**24, np.array((0.723*au, 0.)), np.array((0., 35020.)))
earth = universe.Planet("Earth", "blue", 5.9742 * 10**24, np.array((float(-1. * au), 0.)), np.array((0., float(-29783))), 6371000)
mars = universe.Planet("Mars","red", 6.417*10**23, np.array((0., -1.666*au)), np.array((24007., 0.)))

comet = universe.Planet("comet","grey", 10**14, np.array((-4.*au, 1.7*au)), np.array((20000., 0.)), 30000)


svemir = universe.Universe()

# svemir.add_planet(sun)
# svemir.add_planet(mercury)
# svemir.add_planet(venus)
# svemir.add_planet(earth)
# svemir.add_planet(mars)
# svemir.add_planet(comet)

# svemir.trajectory(1)


lista = list(np.linspace(1.7*au, 1.9*au, 1000))

print(len(lista))

for i in lista:
    comet = universe.Planet("comet","grey", 10**14, np.array((-4.*au, i)), np.array((20000., 0.)), 0.1*au)
    svemir.add_planet(sun)
    svemir.add_planet(mercury)
    svemir.add_planet(venus)
    svemir.add_planet(earth)
    svemir.add_planet(mars)
    svemir.add_planet(comet)

    svemir.trajectory(1)
    svemir.planets.clear()