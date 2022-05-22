import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self):
        self.listaX = []
        self.listaY = []
        self.listaT = [0]
        self.listaVx = []
        self.listaVy = []
        self.listaAy = []
        self.listaAx = []
        self.g = -9.81



    def set_initial_conditions(self, v0, kut, x0, y0, gustoca, koefTr, m, povrsina = 0.25, dt = 0.01):
        self.v0 = v0
        self.kut = kut
        self.x0 = x0
        self.y0 = y0
        self.listaX.append(x0)
        self.listaY.append(y0)
        self.listaVx.append(v0 * np.cos(kut))
        self.listaVy.append(v0 * np.sin(kut))
        self.kut = kut
        self.gustoca = gustoca
        self.koefTr = koefTr
        self.povrsina = povrsina
        self.dt = dt
        self.m = m

    def oblik(self, oblik, r, a):
        if oblik == "kocka":
            self.povrsina = a**2
        else:
            self.povrsina = r**2 * np.pi


    def reset(self):
        self.listaX = []
        self.listaY = []
        self.listaVx = []
        self.listaVy = []
        self.listaT = [0]

    def __move(self):
        self.listaAy.append(self.g - np.sign(self.listaVy[-1])*(self.gustoca * self.koefTr * self.povrsina) / (2*self.m) * self.listaVy[-1]**2)
        self.listaAx.append(- np.sign(self.listaVx[-1])*(self.gustoca * self.koefTr * self.povrsina) / (2*self.m) * self.listaVx[-1]**2)
        self.listaVy.append(self.listaVy[-1] + self.listaAy[-1]*self.dt)
        self.listaVx.append(self.listaVx[-1] + self.listaAx[-1]*self.dt)
        self.listaY.append(self.listaY[-1] + self.listaVy[-1] * self.dt)
        self.listaX.append(self.listaX[-1] + self.listaVx[-1]*self.dt)
        self.listaT.append(self.listaT[-1] + self.dt)
    
    def akceleracijaY_rk4(self, v = 0, x = 0, t = 0):
        return self.g - np.sign(v)*(self.gustoca * self.koefTr * self.povrsina) / (2*self.m) * v**2

    def akceleracijaX_rk4(self, v= 0, x = 0, t = 0):
        return - np.sign(v)*(self.gustoca * self.koefTr * self.povrsina) / (2*self.m) * v**2

    def __move_rk4(self):
        k1vx = self.akceleracijaX_rk4(self.listaVx[-1]) * self.dt
        k1x = self.listaVx[-1] * self.dt
        k2vx = self.akceleracijaX_rk4(self.listaVx[-1] + k1vx/2) * self.dt
        k2x = (self.listaVx[-1] + (k1vx/2)) * self.dt
        k3vx = self.akceleracijaX_rk4(self.listaVx[-1] + k2vx/2) * self.dt
        k3x = (self.listaVx[-1] + (k2vx/2)) * self.dt
        k4vx = self.akceleracijaX_rk4(self.listaVx[-1] + k3vx) * self.dt
        k4x = (self.listaVx[-1] + k3vx) * self.dt

        k1vy = self.akceleracijaY_rk4(self.listaVy[-1]) * self.dt
        k1y = self.listaVy[-1] * self.dt
        k2vy = self.akceleracijaY_rk4(self.listaVy[-1] + k1vy/2) * self.dt
        k2y = (self.listaVy[-1] + (k1vy/2)) * self.dt
        k3vy = self.akceleracijaY_rk4(self.listaVy[-1] + k2vy/2) * self.dt
        k3y = (self.listaVy[-1] + (k2vy/2)) * self.dt
        k4vy = self.akceleracijaY_rk4(self.listaVy[-1] + k3vy) * self.dt
        k4y = (self.listaVy[-1] + k3vy) * self.dt

        self.listaVy.append(self.listaVy[-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)
        self.listaVx.append(self.listaVx[-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
        self.listaY.append(self.listaY[-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)
        self.listaX.append(self.listaX[-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)


    def plot_rk4(self):
        while self.listaY[-1] >= 0:
            self.__move_rk4()
        #plt.plot(self.listaX, self.listaY)
        #plt.show()

    def plot(self):
        while self.listaY[-1] >= 0:
            self.__move()
        #plt.plot(self.listaX, self.listaY)
        #plt.show()

    def domet(self):
        while self.listaY[-1] >= 0:
            self.__move_rk4()
        return self.listaX[-1] - self.listaX[0]

    def angle_to_hit_target(self, p, q, r, v0, x0, y0, gustoca, koefTr, m, povrsina):
        self.pogodilo = False
        self.theta = 0.01
        self.brojac = 0
        self.pocetniKut = 0.01
        self.p = p
        self.q = q
        self.r = r
        while self.pogodilo == False:
            if self.pocetniKut * self.brojac < np.pi / 2:
                self.reset()
                self.brojac += 1
                self.set_initial_conditions(v0, self.pocetniKut * self.brojac, x0, y0, gustoca, koefTr, m, povrsina) 

                while self.listaY[-1] >= 0:
                    self.__move_rk4()

                    for i in range(len(self.listaX)):
                        
                        if self.pogodilo == False:
                            if (self.listaX[i] - p) ** 2 + (self.listaY[i] - q) ** 2 < r**2:
                                self.pogodilo = True
                                print("Potreban kut je", self.pocetniKut * self.brojac, "rad")
                                break
            else:
                print("Premala brzina da bi se pogodilo")
                self.pogodilo = True
