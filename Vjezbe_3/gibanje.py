import particle as prt
import numpy as np
import matplotlib.pyplot as plt
# p1 = prt.Particle()
# p1.set_initial_conditions(5, 0.3, 0, 2)
listaDt = list(np.linspace(0.001,0.1,200))
listaDomet = []
analitickiDomet = 100 * np.sin(2*np.pi/3)/9.81
listaGresaka = []
for i in listaDt:
    p2=prt.Particle()
    p2.set_initial_conditions(10, np.pi/3, 0, 0, i )
    listaDomet.append(p2.range())
    listaGresaka.append(abs(listaDomet[-1] - analitickiDomet)*100/analitickiDomet)

fig, axs = plt.subplots(1, figsize = (6,6))
axs.plot(listaDt, listaGresaka)
plt.setp(axs, xlabel = "dt (s)")
plt.setp(axs, ylabel = "pogreška (%)")
plt.show()
