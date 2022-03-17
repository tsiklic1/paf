import numpy as np  
import matplotlib.pyplot as plt

# f = int(input("Iznos sile  (u N): "))
# m = int(input("Masa (u kg): "))

f = 10
m = 1

korak = 0.01
a = f/m
listaA = []
t = []
for i in range(1000):
    t.append(korak*i)

for i in range(1000):
    listaA.append(a)

v = 0
listaV = [] 
for j in range(1000):
    v = v + a*korak
    listaV.append(v)

x = 0
listaX = []
for k in listaV:
    x = x + k*0.01
    listaX.append(x)


fig, axs = plt.subplots(3, figsize = (6,6))
axs[0].plot(t, listaA)
axs[1].plot(t, listaV)
axs[2].plot(t, listaX)

plt.setp(axs[0], xlabel = "t (s)")
plt.setp(axs[0], ylabel = "a (m/s**2)")
plt.setp(axs[1], xlabel = "t (s)")
plt.setp(axs[1], ylabel = "v (m/s)")
plt.setp(axs[2], xlabel = "t (s)")
plt.setp(axs[2], ylabel = "x (m)")
fig.tight_layout(pad=2.5)
plt.show()
