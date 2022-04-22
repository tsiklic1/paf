import projektil as pro
import matplotlib.pyplot as plt
p = pro.ProjectileDrop(2000, 200)
listaT, listaX, listaY, listaVy = p.gibanje()

plt.plot(listaX, listaY)
plt.show()
plt.plot(listaT, listaVy)
plt.show()