import numpy as np
import matplotlib.pyplot as plt

class planet:
    def __init__(self, m, r, v, a):
        self.m = m
        self.r = r
        self.v = v
        self.a = 0
        self.F = 0
        self.listaX = [self.r[0]]
        self.listaY = [self.r[1]]

class svemir:
    def __init__(self):
        self.planets = []
        self.G = 6.67408 * 10**(-11)
        self.dt = 3600 * 24 * 0.1
        self.duration = 0

    def add_planet(self, planet):
        self.planets.append(planet)

    def __move(self):
        for i in self.planets:
            i.F = 0
            for j in self.planets:
                if i != j:
                    i.F += -self.G * i.m * j.m * (i.r - j.r) / (np.linalg.norm(i.r - j.r))**3

            i.a = i.F/i.m
            i.v += i.a * self.dt # *0.99
            i.r += i.v * self.dt 
            i.listaX.append(i.r[0])
            i.listaY.append(i.r[1])
        self.duration += self.dt
        
        
    def trajectory(self):
        #self.duration = 0
        while self.duration < 3600 * 24 * 365.242:
            #print(self.duration)
            self.__move()

        
        

        

zemlja = planet(5.9742 * 10**24, np.array((float(-1.496 * 10**11), 0.)), np.array((0., float(29783))), np.array((0.,0.)))
sunce = planet(1.989 * 10**30, np.array((0.,0.)), np.array((0.,0.)), np.array((0.,0.)))


svemir = svemir()
svemir.add_planet(zemlja)
svemir.add_planet(sunce)

svemir.trajectory()

# print(zemlja.listaX)
# print(zemlja.listaY)

fig, axs = plt.subplots()
axs.set_aspect("equal")
axs.plot(zemlja.listaX, zemlja.listaY)
axs.plot(sunce.listaX, sunce.listaY, color = "yellow")
plt.show()