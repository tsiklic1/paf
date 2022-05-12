import kh_sa_otporom as otp
import numpy as np
import matplotlib.pyplot as plt

p1 = otp.Projectile()
p1.set_initial_conditions(20, 0.5, 0, 0, 1.2, 0.47, 5)
p1.oblik("kocka", 0.2, 0.2)
p1.plot_rk4()

p2 = otp.Projectile()
p2.set_initial_conditions(20, 0.5, 0, 0, 1.2, 0.47, 5)
p2.oblik("kugla", 0.2, 0.2)
p2.plot_rk4()

plt.plot(p1.listaX, p1.listaY)
plt.plot(p2.listaX, p2.listaY)
plt.show()