#kinematika

#??ne radi kad odavde obrises numpy i matplotlib??
import numpy as np
import matplotlib.pyplot as plt

def polozaj(smjer, listaV, vrijeme):
    n = 10 * vrijeme
    dt = 0.01
    listaSmjer = []
    for i in range(n):
        if smjer>=0:
            smjer = smjer + listaV[i]*dt
            listaSmjer.append(smjer)
        else:
            listaSmjer.append(smjer)
    return listaSmjer

def jednoliko_gibanje(f, m):
    korak = 0.01
    a = f/m
    listaA = []
    t = []
    for i in range(10):
        t.append(korak*i)

    for i in range(10):
        listaA.append(a)

    v = 0
    listaV = [] 
    for j in range(10):
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


def kosi_hitac(v0, kut, vrijeme):
    v0x = np.cos(kut) * v0
    v0y = np.sin(kut) * v0

    a = -9.81
    dt = 0.01
    n = vrijeme * 10

    listaVx = []
    vy = v0y
    listaVy = []
    t = []
    for i in range(n):
        listaVx.append(v0x)
        vy = vy + a*dt
        listaVy.append(vy)
        t.append(i * 0.1)

    x = 0
    y = 0

    listaX = polozaj(x, listaVx, vrijeme)
    listaY = polozaj(y, listaVy, vrijeme)

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

#kosi_hitac(5, 0.3, 25)
#jednoliko_gibanje(5, 1)