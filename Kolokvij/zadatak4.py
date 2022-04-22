import projektil as pro
import matplotlib.pyplot as plt
import numpy as np

raspon = list(np.linspace(0.001, 0.1, 100))
listaTrajanja = []

p = pro.ProjectileDrop(2000, 200)

for i in raspon:

    listaTrajanja.append(p.trajanje(i))

plt.scatter(raspon, listaTrajanja, s = 0.5)
plt.show()

#print(listaTrajanja)