#kosi hitac

#javlja neki memory error kod maks brzine

import numpy as np
import matplotlib.pyplot as plt

def putanja(v0, kut, y0):
    dt = 0.01
    a = -9.81
    x = 0
    y = y0

    vx = np.cos(kut) * v0
    vy = np.sin(kut) * v0

    listaY = []
    listaX = []

    while y >= 0:
        listaY.append(y)
        listaX.append(x)
        vy = vy + a*dt

        y = y + vy*dt
        x = x + vx*dt

    fig, axs = plt.subplots(1, figsize = (6,6))
    axs.plot(listaX, listaY)
    plt.setp(axs, xlabel = "x (m)")
    plt.setp(axs, ylabel = "y (m)")
    axs.set_aspect("equal")
    plt.show()
    
        

def maks_visina(v0, kut, y0):
    dt = 0.01
    a = -9.81
    x = 0
    y = y0

    vx = np.cos(kut) * v0
    vy = np.sin(kut) * v0

    listaY = []
    listaX = []

    while y >= 0:
        listaY.append(y)
        listaX.append(x)
        vy = vy + a*dt

        y = y + vy*dt
        x = x + vx*dt
    return max(listaY)

def domet(v0, kut, y0):
    dt = 0.01
    a = -9.81
    x = 0
    y = y0

    vx = np.cos(kut) * v0
    vy = np.sin(kut) * v0

    listaY = []
    listaX = []

    while y >= 0:
        listaY.append(y)
        listaX.append(x)
        vy = vy + a*dt

        y = y + vy*dt
        x = x + vx*dt

    return(listaX[-1])

    

def maks_brzina(v0, kut, y0):
    dt = 0.01
    a = -9.81
    x = 0
    y = y0

    vx = np.cos(kut) * v0
    vy = np.sin(kut) * v0

    listaY = []
    maksV = 0
    while y >= 0:
        listaY.append(y)
        
        tempV = (vx**2 + vy**2)**0.5
        if tempV > maksV:
            maksV = tempV
        vy = vy + a*dt
        
        y = y + vy*dt
    return(maksV)

def meta(p, q, r, v0, kut, y0):
    dt = 0.01
    a = -9.81
    x = 0
    y = y0

    vx = np.cos(kut) * v0
    vy = np.sin(kut) * v0

    listaY = []
    listaX = []

    while y >= 0:
        listaY.append(y)
        listaX.append(x)
        vy = vy + a*dt

        y = y + vy*dt
        x = x + vx*dt
    pogodilo = False
    for i in listaX:
        for j in listaY:
            if (i-p)**2 + (j-q)**2 <= r**2:
                pogodilo = True
                break
    if pogodilo:
        print("Projektil je pogodio metu.")
    else:
        print("Projektil nije pogodio metu")

    meta = plt.Circle((p, q), r, color = "red")
    fig, axs = plt.subplots()
    axs.set_aspect("equal")
    axs.add_patch(meta)
    axs.plot(listaX, listaY)
    plt.show()

