import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self, name, color, m, r, v):
        self.name = name
        self.color = color
        self.m = m
        self.r = r
        self.v = v
        self.F = 0
        self.listaX = [self.r[0]]
        self.listaY = [self.r[1]]

class Universe:
    def __init__(self):
        self.planets = []
        self.G = 6.67408 * 10**(-11)
        self.dt = 3600 * 24
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
            i.v += i.a * self.dt
            i.r += i.v * self.dt 
            i.listaX.append(i.r[0])
            i.listaY.append(i.r[1])
        self.duration += self.dt
        
        
    def trajectory(self, years):
        while self.duration < 3600 * 24 * 365.242 * years:
            self.__move()

        