import numpy as np
import matplotlib.pyplot as plt
import math
class harmonic_oscillator:
    def __init__(self, t, k, m, x0, v0 = 0, dt = 0.01):
        self.k = k
        self.m = m
        self.t = t
        self.x0 = x0
        self.v0 = v0
        self.dt = dt

        self.listaX = [x0]
        self.listaT = list(np.arange(0, t + self.dt, self.dt))
        
        self.listaA = [-k/m * x0]
        self.listaV = [v0]

    #def set_initital_conditions(self, t, k, m, a):

    def __move(self):
        self.listaA.append(-self.k / self.m * self.listaX[-1])
        self.listaV.append(self.listaV[-1] + self.listaA[-1] * self.dt)
        self.listaX.append(self.listaX[-1] + self.listaV[-1] * self.dt)
    
    def reset(self):
        self.listaA = [-self.k/self.m * self.x0]
        self.listaV = [self.v0]
        self.listaX = [self.x0]
        

    def plot_trajectory(self):
        for i in self.listaT:
            self.__move()

        self.listaX.pop()
        self.listaA.pop()
        self.listaV.pop()

        fig, axs = plt.subplots(1, figsize = (6,6))
        axs.scatter(self.listaT, self.listaX, s = 0.2)
        plt.setp(axs, xlabel = "t (s)")
        plt.setp(axs, ylabel = "x (m)")
        plt.show()

        fig, axs = plt.subplots(1, figsize = (6,6))
        axs.scatter(self.listaT, self.listaA, s = 0.2)
        plt.setp(axs, xlabel = "t (s)")
        plt.setp(axs, ylabel = "a (m/s**2)")
        plt.show()

        fig, axs = plt.subplots(1, figsize = (6,6))
        axs.scatter(self.listaT, self.listaV, s = 0.2)
        plt.setp(axs, xlabel = "t (s)")
        plt.setp(axs, ylabel = "v (m/s)")
        plt.show()


    def polozaj(self):

        for i in self.listaT:
            self.__move()

        self.listaX.pop()
        self.listaA.pop()
        self.listaV.pop()

        return [self.listaT, self.listaX]

    def analiticko(self):
        self.dt = 0.001
        self.listaT = list(np.arange(0, self.t + self.dt, self.dt))
        self.listaAnalitickih = []
        for i in self.listaT:
            self.listaAnalitickih.append(self.x0 * math.sin(math.sqrt(self.k / self.m)*i + math.pi/2))

        return [self.listaT, self.listaAnalitickih]
    

    def period(self):
        self.listaZaPeriod = []

        self.polozaj()
        print(self.listaX)
        if self.listaX[0] > 0:

            for i in range(len(self.listaX)):
                if self.listaX[i] < 0:
                    self.listaZaPeriod.append(self.listaT[i])
                    self.brojac = i
                    break
            
            for i in range(self.brojac, len(self.listaX)):
                if self.listaX[i] > 0:
                    self.listaZaPeriod.append(self.listaT[i])
                    break
        
        elif self.listaX[0] < 0:
            
            for i in range(len(self.listaX)):
                #print(self.listaX[i])
                if self.listaX[i] > 0:
                    self.listaZaPeriod.append(self.listaT[i])
                    self.brojac = i
                    break
        
            for i in range(self.brojac, len(self.listaX)):
                    if self.listaX[i] < 0:
                        self.listaZaPeriod.append(self.listaT[i])
                        break
   
        #print("Period titranja je: ", (self.listaZaPeriod[1] - self.listaZaPeriod[0])*2)

        return [((self.listaZaPeriod[1] - self.listaZaPeriod[0])*2), self.dt]
    
    def analitickiPeriod(self):
        return 2*math.pi*math.sqrt(self.m/self.k)


#h1 = harmonic_oscillator(2, 10, 0.1, 0.3)
#h1.plot_trajectory()
#h1.period()