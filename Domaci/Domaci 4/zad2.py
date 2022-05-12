import kh_sa_otporom as otp
import numpy as np
import matplotlib.pyplot as plt

p1 = otp.Projectile()
p1.angle_to_hit_target(3, 3, 0.5, 10, 0, 0, 1.226, 0.5, 5, 0.25)

p2 = otp.Projectile()
p2.angle_to_hit_target(3, 8, 0.5, 14, 0, 0, 1.226, 0.5, 5, 0.25)
plt.show()

meta1 = plt.Circle((p1.p, p1.q), p1.r, color = "red")
meta2 = plt.Circle((p2.p, p2.q), p2.r, color = "magenta")
fig, axs = plt.subplots()
axs.set_aspect("equal")
axs.add_patch(meta1)
axs.add_patch(meta2)
axs.plot(p1.listaX, p1.listaY)
axs.plot(p2.listaX, p2.listaY)
plt.setp(axs, xlabel = "x (m)")
plt.setp(axs, ylabel = "y (m)")
plt.show()