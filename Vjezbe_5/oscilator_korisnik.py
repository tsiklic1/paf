import harmonic_oscillator as osc
import matplotlib.pyplot as plt
import math

h1 = osc.harmonic_oscillator(2, 10, 0.1, 0.3)
h1.plot_trajectory()

#Ovaj dio je za preciznost ovisno o dt

h2 = osc.harmonic_oscillator(2, 10, 0.1, 0.3, 0, 0.05)
h3 = osc.harmonic_oscillator(2, 10, 0.1, 0.3, 0, 0.1)

# lista1 = h1.polozaj()
# lista2 = h2.polozaj()
# lista3 = h3.polozaj()

# plt.scatter(lista1[0], lista1[1], s = 0.1, color = "red")
# plt.scatter(lista2[0], lista2[1], s = 0.5, color = "green")
# plt.scatter(lista3[0], lista3[1], s = 1.2, color = "black")

# listaAnaliticko = h1.analiticko()
# plt.plot(listaAnaliticko[0], listaAnaliticko[1], color = "yellow")
# plt.show()

# print(h1.analiticko())


listaPerioda = []
listaPerioda.append(h1.period())
listaPerioda.append(h2.period())
listaPerioda.append(h3.period())

print("Analitički period je: ", h1.analitickiPeriod(), "\nnumerički period za dt = ", listaPerioda[0][1],
    "je ", listaPerioda[0][0] ,"\nnumerički period za dt = ", listaPerioda[1][1],
    "je ", listaPerioda[1][0], "\nnumerički period za dt = ", listaPerioda[2][1],
    "je ", listaPerioda[2][0])