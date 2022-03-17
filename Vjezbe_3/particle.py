import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.listaX = []
        self.listaY = []
        self.listaT = [0]
        self.listaVx = []
        self.listaVy = []


    def set_initial_conditions(self, v0, kut, x0, y0):
        self.listaX.append(x0)
        self.listaY.append(y0)
        self.listaVx.append(v0 * np.cos(kut))
        self.listaVy.append(v0 * np.sin(kut))
        self.kut = kut

    def reset(self):
        self.listaX = []
        self.listaY = []


    def __move(self):
        a = -9.81
        dt = 0.01
        self.listaVy.append(self.listaVy[-1] + a*dt)
        self.listaY.append(self.listaY[-1] + self.listaVy[-1] * dt)
        self.listaX.append(self.listaX[-1] + self.listaVx[0]*dt)
        self.listaT.append(self.listaT[-1] + dt)


    def range(self):
        while self.listaY[-1] > 0:
            self.__move()

        if self.listaY[-1] < 0:
            self.listaY.pop()
            self.listaX.pop()

        print("Domet je", self.listaX[-1] - self.listaX[0])

            
    def plot_trajectory(self):
        while self.listaY[-1] > 0:
            self.__move()

        if self.listaY[-1] < 0:
            self.listaY.pop()
            self.listaX.pop()
        
        plt.plot(self.listaX, self.listaY)
        plt.show()

    def total_time(self):
        while self.listaY[-1] > 0:
            self.__move()

        if self.listaY[-1] < 0:
            self.listaT.pop()

        print("Ukupno vrijeme: ", self.listaT[-1])

    def max_speed(self):
        while self.listaY[-1] > 0:
            self.__move()

        if self.listaY[-1] < 0:
            self.listaVy.pop()

        maksVy = self.listaVy[0]
        for i in self.listaVy:
            if abs(i) > maksVy:
                maksVy = abs(i)
          
        print("Najveća ostvarena brzina:", (maksVy**2 + self.listaVx[0]**2)**0.5)

    def velocity_to_hit_target(self, potrebnaV, p, q, r):

    def angle_to_hit_target(self, potrebniKut, p, q, r):
        


p1 = Particle()
p1.set_initial_conditions(5, 0.6, 0, 2)
p1.range()
#p1.plot_trajectory()
p1.total_time()
p1.max_speed()