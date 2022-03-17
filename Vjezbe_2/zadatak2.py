import numpy as np
import matplotlib.pyplot as plt
v0 = 20
stupnjevi = 40
kut = stupnjevi*np.pi/180

v0x = np.cos(kut) * v0
v0y = np.sin(kut) * v0

a = -9.81
dt = 0.01
n = 1000

listaVx = []
vy = v0y
listaVy = []
t = []
for i in range(n):
    listaVx.append(v0x)
    vy = vy + a*dt
    listaVy.append(vy)
    t.append(i * dt)

    

x = 0
y = 0

def polozaj(smjer, listaV):
    listaSmjer = []
    for i in range(n):
        if smjer>=0:
            smjer = smjer + listaV[i]*dt
            listaSmjer.append(smjer)
        else:
            listaSmjer.append(smjer)
    return listaSmjer


listaX = polozaj(x, listaVx)
listaY = polozaj(y, listaVy)

fig, axs = plt.subplots(3, figsize = (6,6))
axs[0].plot(t, listaX)
axs[1].plot(t, listaY)
axs[2].plot(listaX, listaY)

plt.setp(axs[0], xlabel = "t (s)")
plt.setp(axs[0], ylabel = "x (m)")
plt.setp(axs[1], xlabel = "t (s)")
plt.setp(axs[1], ylabel = "y (m)")
plt.setp(axs[2], xlabel = "x (m)")
plt.setp(axs[2], ylabel = "y (m)")
fig.tight_layout(pad=2.5)

plt.show()