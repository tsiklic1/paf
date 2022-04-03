import numpy as np
import matplotlib.pyplot as plt
class gibanje:
    def __init__(self, sila, x0, v0, m, t):
        self.x0 = x0
        self.v0 = v0
        self.t = t
        self.dt = 0.01
        self.m = m
        self.sila = sila
        self.sila0 = sila(x0, v0, self.dt)
        self.a0 = self.sila(x0, v0, v0) / self.m
        self.brojac = 0
        self.listaT = [self.dt]
        self.listaX = [x0]
        self.listaV = [v0]
        self.listaA = [self.a0]
        self.listaF = [self.sila0]


    def __move(self):
        self.brojac += 1
        self.listaT.append(self.brojac * self.dt)
        self.listaF.append(self.sila(self.listaX[-1], self.listaV[-1], self.listaT[-1]))
        self.listaA.append(self.listaF[-1] / self.m)
        self.listaV.append(self.listaV[-1] + self.listaA[-1] * self.dt)
        self.listaX.append(self.listaX[-1] + self.listaV[-1] * self.dt)
        

    def plot_trajectory(self):
        for i in self.listaT:
            if i < self.t:
                self.__move()
            else:
                break
            
        # plt.scatter(self.listaT, self.listaX)
        # plt.show()

        fig, axs = plt.subplots(1, figsize = (6,6))
        axs.scatter(self.listaT, self.listaX, s = 0.4)
        plt.setp(axs, xlabel = "t (s)")
        plt.setp(axs, ylabel = "x (m)")
        plt.show()

        fig, axs = plt.subplots(1, figsize = (6,6))
        axs.scatter(self.listaT, self.listaA, s = 0.4, color = "green")
        plt.setp(axs, xlabel = "t (s)")
        plt.setp(axs, ylabel = "a (m/s**2)")
        plt.show()

        fig, axs = plt.subplots(1, figsize = (6,6))
        axs.scatter(self.listaT, self.listaV, s = 0.4, color = "red")
        plt.setp(axs, xlabel = "t (s)")
        plt.setp(axs, ylabel = "v (m/s)")
        plt.show()





# def sila(x, v, t):
#     return 0

# g1 = gibanje(sila, 0.3, 0, 0.1, 2)
# g1.plot_trajectory()