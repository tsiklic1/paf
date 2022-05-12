import numpy as np
import matplotlib.pyplot as plt

class bungee_jump:
    def __init__(self, m, k, Cd, A, rho, l0, h0):
        self.m = m
        self.k = k
        self.Cd = Cd
        self.A = A
        self.rho = rho
        self.l0 = l0
        self.h0 = h0
        self.listaV = [0]
        self.listaY = [h0]
        self.listaA = [-9.81]
        self.listaT = [0]
        self.dt = 0.01
        self.g = -9.81
        
    def __a_sa_Fel(self, v, y):
        return self.g - np.sign(v)*(self.rho * self.Cd * self.A) / (2*self.m) * v**2 - self.k/self.m * y

    def __a_bez_Fel(self, v, y):
        return self.g - np.sign(v)*(self.rho * self.Cd * self.A) / (2*self.m) * v**2

    def __move(self, a):
        self.listaA.append(a(self.listaV[-1], self.listaY[-1]))
        self.listaV.append(self.listaV[-1] + self.listaA[-1] * self.dt)
        self.listaY.append(self.listaY[-1] + self.listaV[-1] * self.dt)
        self.listaT.append(self.listaT[-1] + self.dt)

    def plot_trajectory(self):
        while self.listaT[-1] < 20:
            if self.listaY[-1] > self.h0 - self.l0:
                self.__move(self.__a_bez_Fel)
            else:
                self.__move(self.__a_sa_Fel)
        
        plt.plot(self.listaT, self.listaY)
        plt.show()
            
skakac1 = bungee_jump(80, 50, 10, 0.075, 1, 10, 40)
skakac1.plot_trajectory()