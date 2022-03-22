from ctypes.wintypes import PSIZEL
import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.listaX = []
        self.listaY = []
        self.listaT = [0]
        self.listaVx = []
        self.listaVy = []
        self.a = -9.81
        # self.dt = 0.01
        self.listaKoraka = list(np.linspace(0.001, 0.1, 10))
        self.listaGresaka = []

    def set_initial_conditions(self, v0, kut, x0, y0, dt = 0.1):
        self.listaX.append(x0)
        self.listaY.append(y0)
        self.listaVx.append(v0 * np.cos(kut))
        self.listaVy.append(v0 * np.sin(kut))
        self.kut = kut
        self.dt = dt

    def reset(self):
        self.listaX = []
        self.listaY = []


    def __move(self):
        self.listaVy.append(self.listaVy[-1] + self.a*self.dt)
        self.listaY.append(self.listaY[-1] + self.listaVy[-1] * self.dt)
        self.listaX.append(self.listaX[-1] + self.listaVx[0]*self.dt)
        self.listaT.append(self.listaT[-1] + self.dt)


    def range(self):
        while self.listaY[-1] >= 0:
            self.__move()

        if self.listaY[-1] < 0:
            self.listaY.pop()
            self.listaX.pop()

        #print("Domet je", self.listaX[-1] - self.listaX[0])
        return self.listaX[-1] - self.listaX[0]

            
    def plot_trajectory(self):
        while self.listaY[-1] >= 0:
            self.__move()

        if self.listaY[-1] < 0:
            self.listaY.pop()
            self.listaX.pop()
        
        plt.plot(self.listaX, self.listaY)
        plt.show()

    def total_time(self):
        while self.listaY[-1] >= 0:
            self.__move()

        if self.listaY[-1] < 0:
            self.listaT.pop()

        print("Ukupno vrijeme: ", self.listaT[-1])

    def max_speed(self):
        while self.listaY[-1] >= 0:
            self.__move()

        if self.listaY[-1] < 0:
            self.listaVy.pop()

        maksVy = self.listaVy[0]
        for i in self.listaVy:
            if abs(i) > maksVy:
                maksVy = abs(i)
          
        print("Najveća ostvarena brzina:", (maksVy**2 + self.listaVx[0]**2)**0.5)


    def velocity_to_hit_target(self, kut, p, q, r, x0, y0):

        self.pogodilo = False
        self.pocetnaV = 0.1
        self.brojac = 0

        while self.pogodilo == False:
            self.brojac += 1
            self.set_initial_conditions(self.pocetnaV*self.brojac, kut, x0, y0)
            print(self.brojac * self.pocetnaV)
            while self.listaY[-1] >= 0:
                self.__move()
            
            
            
            for i in self.listaX:
                for j in self.listaY:
                    if (i - p)**2 + (j - q)**2 <= r**2:
                        self.pogodilo = True
                        print("Pogodilo")
                        # break



        
        




    def angle_to_hit_target(self, v0, p, q, r):
        pass


p1 = Particle()
p1.set_initial_conditions(10, np.pi/3, 5, 7)
# print(p1.range())
# #p1.plot_trajectory()
# #p1.total_time()
# #p1.max_speed()
# p1.relativna_pogreska()
p1.velocity_to_hit_target(0.7, 4, 2, 1, 0, 0)