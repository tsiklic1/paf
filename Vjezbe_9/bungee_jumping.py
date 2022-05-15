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
        self.listaEk = [0]
        self.listaEp = [h0 * m * 9.81]
        self.listaEel = [0]
        self.listaEuk = []
        
    def __a_sa_Fel(self, v, y):
        return self.g - np.sign(v)*(self.rho * self.Cd * self.A) / (2*self.m) * v**2 + self.k/self.m * (self.h0 - self.listaY[-1] - self.l0)

    def __a_bez_Fel(self, v, y):
        return self.g - np.sign(v)*(self.rho * self.Cd * self.A) / (2*self.m) * v**2

    def __move(self, a):
        self.listaA.append(a(self.listaV[-1], self.listaY[-1]))
        self.listaV.append(self.listaV[-1] + self.listaA[-1] * self.dt)
        self.listaY.append(self.listaY[-1] + self.listaV[-1] * self.dt)
        self.listaT.append(self.listaT[-1] + self.dt)
        self.listaEk.append(self.__kin(self.m, self.listaV[-1]))
        self.listaEp.append(self.__pot(self.m, self.listaY[-1]))

    def __kin(self, m, v):
        return m*v**2/2

    def __pot(self, m, h):
        return m*h*9.81

    def __elas(self, k, x):
        return k*x**2/2

    def plot_trajectory(self):
        while self.listaT[-1] < 50:
            if self.listaY[-1] > self.h0 - self.l0:
                self.__move(self.__a_bez_Fel)
                self.listaEel.append(0)
                #print("bez")
            else:
                self.__move(self.__a_sa_Fel)
                self.listaEel.append(self.__elas(self.k, self.h0 - self.listaY[-1] - self.l0))
                #print("sa")
        #print(self.listaY)
        plt.plot(self.listaT, self.listaY)
        plt.show()

        for i in range(len(self.listaEel)):
            self.listaEuk.append(self.listaEk[i] + self.listaEel[i] + self.listaEp[i])

        plt.plot(self.listaT, self.listaEk, linewidth = 0.6)
        plt.plot(self.listaT, self.listaEp, linewidth = 0.6)
        plt.plot(self.listaT, self.listaEel, linewidth = 0.6)
        plt.plot(self.listaT, self.listaEuk, linewidth = 0.6)
        plt.show()


