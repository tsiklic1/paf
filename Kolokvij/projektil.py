import matplotlib.pyplot as plt

class ProjectileDrop:
    def __init__(self, h, vx):
        self.h = h
        self.vx = vx
        self.dt = 0.01
        self.listaY = [h]
        self.listaVy = [0]
        self.listaX = [0]
        self.listaT = [self.dt]
        self.listaVx = [vx]
        self.brojac = 0
        self.a = -9.81
        print("Objekt je uspješno stvoren, vx = ", vx, "h = ", h)

    def promjena_visine(self, novaVisina):
        self.h = novaVisina
        print("Nova visina je ", self.h)

    def reset(self):
        self.listaY = [self.h]
        self.listaVy = [0]
        self.listaX = [0]
        self.listaVx = [self.vx]
        self.listaT = [self.dt]

    def promjena_brzine(self, promjena):
        self.vx += promjena
        print("Nova brzina je", self.vx)

    def __move(self):
        # self.brojac = self.brojac + 1
        self.listaT.append(self.listaT[-1] + self.dt)
        self.listaVy.append(self.listaVy[-1] + self.a* self.dt)
        self.listaY.append(self.listaY[-1] + self.listaVy[-1] * self.dt)
        self.listaX.append(self.listaX[-1] + self.vx*self.dt)
        # print(self.listaY[-1])
    def gibanje(self):
        while self.listaY[-1] >= 0:
            self.__move()
            

        # plt.plot(self.listaT, self.listaY)
        # plt.show()



        return self.listaT, self.listaX, self.listaY, self.listaVy
    
    def trajanje(self, dt):
        self.reset()
        self.dt = dt
        #print(self.dt)
        while self.listaY[-1] >= 0:
            self.__move()

        #print("Vreijeme trajanja: ", self.listaT[-1])
        return self.listaT[-1]
    
    def __move_sa_vjetrom(self):
        self.listaT.append(self.listaT[-1] + self.dt)
        self.listaVy.append(self.listaVy[-1] + self.a* self.dt)
        self.listaVx.append(self.listaVx[-1] + self.vVjetra*self.dt*self.k)
        self.listaY.append(self.listaY[-1] + self.listaVy[-1] * self.dt)
        self.listaX.append(self.listaX[-1] + self.listaVx[-1]*self.dt)


    def meta(self, x, sirina, vVjetra):
        self.x = x
        self.sirina = sirina
        self.vVjetra = vVjetra
        self.k = 0.1
        while self.listaY[-1] >= 0:
            self.__move_sa_vjetrom()

        self.domet = self.listaX[-1] - self.listaX[0]
        #print(self.domet)

        self.pocetniX = self.x - self.domet
        #self.krajnjiX = self.x + self.sirina - self.domet

        self.reset()
        self.listaX = [self.pocetniX]
        # print(self.listaX)
        # print(self.listaY)
        while self.listaY[-1] >= 0:
            self.__move_sa_vjetrom()
        
        plt.plot(self.listaX, self.listaY)
        plt.show()

        self.reset()
        while self.listaX[-1] < self.pocetniX:
            self.__move()
        print("Mora ispustiti u trenutku t = ", self.listaT[-1])


       

a = ProjectileDrop(2000, 200)
# a.promjena_visine(3)
# a.promjena_brzine(-1)
#a.gibanje()
#a.trajanje()
# a.meta(20000, 10, -100)