import numpy as np
import matplotlib.pyplot as plt
import el_magn as em

def const(t):
    return np.array((0., 0., 1.))

def promj(t):
    bx = 0
    by = 0
    bz = 0.1*t
    return np.array((bx, by, bz))


elektron1 = em.el_magn(const, -1., 1., np.array((0.1, 0.1, 0.1)), np.array((0.,0.,0.)), np.array((0., 0., 1.)))
elektron2 = em.el_magn(promj, -1., 1., np.array((0.1, 0.1, 0.1)), np.array((0.,0.,0.)), np.array((0., 0., 1.)))
elektron1.trajectory_f()
elektron2.trajectory_f()

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.plot3D(elektron1.listaX, elektron1.listaY, elektron1.listaZ)
#ax.plot3D(elektron2.listaX, elektron2.listaY, elektron2.listaZ)

plt.show()