import kh_sa_otporom as otp
import numpy as np
import matplotlib.pyplot as plt

p1 = otp.Projectile()
p1.set_initial_conditions(10, 0.5, 0, 0, 1, 0.4, 0.5, 0.3)
p1.plot()
plt.plot(p1.listaX, p1.listaY)

p2 = otp.Projectile()
p2.set_initial_conditions(10, 0.5, 0, 0, 1, 0.4, 0.5, 0.3, 0.03)
p2.plot()
plt.plot(p2.listaX, p2.listaY)
plt.show()

print("Eulerova metoda ne daje naznake nefizikalnog gibanja za dt <= 0.03")