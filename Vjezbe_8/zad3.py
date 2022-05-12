import kh_sa_otporom as otp
import numpy as np
import matplotlib.pyplot as plt

listaCd = list(np.linspace(0, 1, 10))
listaM = list(np.linspace(1, 5, 100))
listaDometa1 = []
listaDometa2 = []
for i in listaCd:
    prt = otp.Projectile()
    prt.set_initial_conditions(20, 0.5, 0, 0, 1.2, i, 0.25, 5)
    listaDometa1.append(prt.domet())
    #prt.plot_rk4()
plt.scatter(listaCd, listaDometa1, s = 0.5)
plt.show()

for i in listaM:
    prt = otp.Projectile()
    prt.set_initial_conditions(20, 0.5, 0, 0, 1.2, 0.47, 0.25, i)
    listaDometa2.append(prt.domet())
plt.scatter(listaM, listaDometa2, s = 0.5)
plt.show()