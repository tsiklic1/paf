import numpy as np
import matplotlib.pyplot as plt

class el_magn:
    def __init__(self,q, m, v, e, b):
        self.listaX = [0]
        self.listaY = [0]
        self.listaZ = [0]
        self.kxyz = np.array((0., 0., 0.))
        self.v = v
        self.E = e
        self.B = b
        self.q = q
        self.m = m
        self.dt = 0.01
        self.duration = 20
        self.t = 0

    # def __a(self):
    #     return self.q/self.m * (self.E + np.cross(self.v, self.B))

    def __move(self):
        #self.v = np.add(self.v, self.__a() * self.dt, out = self.v, casting = "unsafe")
        self.a = self.q/self.m * (self.E + np.cross(self.v, self.B))
        self.v += self.a * self.dt
        self.listaX.append(self.listaX[-1] + self.v[0] * self.dt)
        self.listaY.append(self.listaY[-1] + self.v[1] * self.dt)
        self.listaZ.append(self.listaZ[-1] + self.v[2] * self.dt)
        self.t += self.dt

    def __a(self, v):
        return self.q/self.m * (self.E + np.cross(v, self.B))

    def __move_rk4(self):
        k1v = self.__a(self.v) * self.dt
        k1xyz = self.v * self.dt 

        k2v = self.__a(self.v + k1v/2) * self.dt
        k2xyz = (self.v + k2v/2) * self.dt

        k3v = self.__a(self.v + k2v/2) * self.dt
        k3xyz = (self.v + k2v/2) * self.dt

        k4v = self.__a(self.v + k3v) * self.dt
        k4xyz = (self.v + k3v) * self.dt

        self.v += (k1v + 2*k2v + 2*k3v + k4v)/6
        self.listaX.append(self.listaX[-1] + (k1xyz[0] + 2*k2xyz[0] + 2*k3xyz[0] + k4xyz[0])/6)
        self.listaY.append(self.listaY[-1] + (k1xyz[1] + 2*k2xyz[1] + 2*k3xyz[1] + k4xyz[1])/6)
        self.listaZ.append(self.listaZ[-1] + (k1xyz[2] + 2*k2xyz[2] + 2*k3xyz[2] + k4xyz[2])/6)   
        self.t += self.dt

    def trajectory(self):
        while self.t < self.duration:
            self.__move()

    def trajectory_rk4(self):
        while self.t < self.duration:
            self.__move_rk4()



        # fig = plt.figure()
        # ax = plt.axes(projection = "3d")
        # ax.plot3D(self.listaX, self.listaY, self.listaZ)
        # plt.show()

p1 = el_magn(-1., 1., np.array((0.1,0.1,0.1)), np.array((0.,0.,0.)), np.array((0., 0., 1.)))
p1.trajectory()
# p2 = el_magn(1., 1., np.array((0.1,0.1,0.1)), np.array((0.,0.,0.)), np.array((0., 0., 1.)))
# p2.trajectory()
p3 =  el_magn(-1., 1., np.array((0.1,0.1,0.1)), np.array((0.,0.,0.)), np.array((0., 0., 1.)))
p3.trajectory_rk4()


fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.plot3D(p1.listaX, p1.listaY, p1.listaZ)
ax.plot3D(p3.listaX, p3.listaY, p3.listaZ, linestyle = "dashed")
plt.show()


