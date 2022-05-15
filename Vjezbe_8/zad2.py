import kh_sa_otporom as otp
import numpy as np
import matplotlib.pyplot as plt

p1 = otp.Projectile()
p1.set_initial_conditions(20, 0.5, 0, 0, 1.2, 0.47, 0.25, 5)
p1.plot()

p2 = otp.Projectile()
p2.set_initial_conditions(20, 0.5, 0, 0, 1.2, 0.47, 0.25, 5)
p2.plot_rk4()

plt.plot(p1.listaX, p1.listaY)
plt.plot(p2.listaX, p2.listaY)
plt.show()

#Što je manja masa Eulerova metoda je sve nepreciznija u odnosu na rk4