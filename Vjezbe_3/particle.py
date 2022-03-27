import numpy as np
import matplotlib.pyplot as plt

#možda stavit da se plota i kad se promaši meta

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

    def set_initial_conditions(self, v0, kut, x0, y0, dt = 0.001):
        self.listaX.append(x0)
        self.listaY.append(y0)
        self.listaVx.append(v0 * np.cos(kut))
        self.listaVy.append(v0 * np.sin(kut))
        self.kut = kut
        self.dt = dt

    def reset(self):
        self.listaX = []
        self.listaY = []
        self.listaVx = []
        self.listaVy = []
        self.listaT = [0]

    def __move(self):
        self.listaVy.append(self.listaVy[-1] + self.a*self.dt)
        self.listaY.append(self.listaY[-1] + self.listaVy[-1] * self.dt)
        self.listaX.append(self.listaX[-1] + self.listaVx[0]*self.dt)
        self.listaT.append(self.listaT[-1] + self.dt)

    def range(self):
        while self.listaY[-1] >= 0:
            self.__move()

        #print("Domet je", self.listaX[-1] - self.listaX[0])
        return self.listaX[-1] - self.listaX[0]
          
    def plot_trajectory(self):
        while self.listaY[-1] >= 0:
            self.__move()


        fig, axs = plt.subplots(1, figsize = (6,6))
        axs.plot(self.listaX, self.listaY)
        plt.setp(axs, xlabel = "x (m)")
        plt.setp(axs, ylabel = "y (m)")
        plt.show()

    def total_time(self):
        while self.listaY[-1] >= 0:
            self.__move()

        #print("Ukupno vrijeme: ", self.listaT[-1])
        return(self.listaT[-1])

    def max_speed(self):
        while self.listaY[-1] >= 0:
            self.__move()

        maksVy = self.listaVy[0]
        for i in self.listaVy:
            if abs(i) > maksVy:
                maksVy = abs(i)
          
        print("Najveća ostvarena brzina:", (maksVy**2 + self.listaVx[0]**2)**0.5)

    def velocity_to_hit_target(self, kut, p, q, r, x0 = 0, y0 = 0):

        self.pogodilo = False
        self.pocetnaV = 0.1
        self.brojac = 0

        while self.pogodilo == False:
            if self.pocetnaV*self.brojac < 100:
                self.reset()
                self.brojac += 1
                self.set_initial_conditions(self.pocetnaV*self.brojac, kut, x0, y0, 0.1)
                while self.listaY[-1] >= 0:
                    self.__move()
                
                    for i in range(len(self.listaX)):
                        if self.pogodilo == False:
                            if (self.listaX[i] - p)**2 + (self.listaY[i] - q)**2 < r**2:
                                self.pogodilo = True
                                print("Brzina potrebna da bi se pogodila meta za kut", kut, "rad je: ", self.pocetnaV*self.brojac, "m/s")
                                break
                
                

                # if self.pogodilo:
                #     meta = plt.Circle((p, q), r, color = "red")
                #     fig, axs = plt.subplots()
                #     axs.set_aspect("equal")
                #     axs.add_patch(meta)
                #     axs.plot(self.listaX, self.listaY)
                #     plt.setp(axs, xlabel = "x (m)")
                #     plt.setp(axs, ylabel = "y (m)")
                #     plt.show()
                    
                #print(self.pocetnaV*self.brojac)

            else:
                print("Program je zaustavljen jer je potrebna prevelika brzina (>100m/s) \n ili je zadan nemoguć slučaj (meta iza ili iznad projektila).")
                break

        meta = plt.Circle((p, q), r, color = "red")
        fig, axs = plt.subplots()
        axs.set_aspect("equal")
        axs.add_patch(meta)
        axs.plot(self.listaX, self.listaY)
        plt.setp(axs, xlabel = "x (m)")
        plt.setp(axs, ylabel = "y (m)")
        plt.show()
                
    def angle_to_hit_target(self, v0, p, q, r, x0 = 0, y0 = 0):
        self.pogodilo = False
        self.pocetniKut = 0.01
        self.brojac = 0
        
        while self.pogodilo == False:
            if self.pocetniKut * self.brojac < np.pi / 2:
                self.reset()
                self.brojac += 1
                self.set_initial_conditions(v0, self.pocetniKut*self.brojac, x0, y0, 0.01)

                while self.listaY[-1] >= 0:
                    self.__move()

                    for i in range(len(self.listaX)):
                            if self.pogodilo == False:
                                if (self.listaX[i] - p)**2 + (self.listaY[i] - q)**2 < r**2:
                                    self.pogodilo = True
                                    print("Potreban kut je", self.pocetniKut * self.brojac, "rad")
                                    break

                # if self.pogodilo:
                #     meta = plt.Circle((p, q), r, color = "red")
                #     fig, axs = plt.subplots()
                #     axs.set_aspect("equal")
                #     axs.add_patch(meta)
                #     axs.plot(self.listaX, self.listaY)
                #     plt.setp(axs, xlabel = "x (m)")
                #     plt.setp(axs, ylabel = "y (m)")
                #     plt.show()
            else:
                print("Zadana je premala brzina i nikad neće pogodit ili je meta krivo postavljena (iza projektila)")
                break

        meta = plt.Circle((p, q), r, color = "red")
        fig, axs = plt.subplots()
        axs.set_aspect("equal")
        axs.add_patch(meta)
        axs.plot(self.listaX, self.listaY)
        plt.setp(axs, xlabel = "x (m)")
        plt.setp(axs, ylabel = "y (m)")
        plt.show()

    def ovisnostDometa(self, v0):
        self.listaKutova = list(np.arange(0, np.pi/2, 0.01))
        self.listaDometa = []
        
        for i in self.listaKutova:
            self.reset()
            self.set_initial_conditions(v0, i, 0, 0)
            self.listaDometa.append(self.range())

        fig, axs = plt.subplots()
        axs.plot(self.listaKutova, self.listaDometa)
        plt.setp(axs, xlabel = "kut (rad)")
        plt.setp(axs, ylabel = "domet (m)")
        plt.show()

    def ovisnostVremena(self, v0):
        self.listaKutova = list(np.arange(0, np.pi/2, 0.01))
        self.listaVremena = []
        for i in self.listaKutova:
            self.reset()
            self.set_initial_conditions(v0, i, 0, 0)
            self.listaVremena.append(self.total_time())

        fig, axs = plt.subplots()
        axs.plot(self.listaKutova, self.listaVremena)
        plt.setp(axs, xlabel = "kut (rad)")
        plt.setp(axs, ylabel = "t (s)")
        plt.show()



p1 = Particle()
p1.set_initial_conditions(5, 0.1, 0, 0)
#print(p1.range())
#p1.plot_trajectory()
#print(p1.total_time())
#p1.max_speed()
#p1.velocity_to_hit_target(0.7, 10, 2, 1, 0, 0)
#p1.angle_to_hit_target(14, 4, 2, 1)
#p1.ovisnostDometa(5)
#p1.ovisnostVremena(5)
