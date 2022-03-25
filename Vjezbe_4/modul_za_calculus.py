import calculus as calc
import matplotlib.pyplot as plt
import math

a = 0
b = 6

def kubna(x):
    return x**3 - 8*x**2 + math.sin(x)*math.e**x

# lista1 = calc.derivacija_2(kubna, a, b, 0.1, 1)
# lista2 = calc.derivacija_2(kubna, a, b, 0.01, 1)
# listaF = []
# for i in lista1[0]:
#     listaF.append(3*i**2 - 16*i + math.cos(i)*math.e**i + math.sin(i)*math.e**i)



# plt.plot(lista1[0], lista1[1], color = "red")
# plt.plot(lista1[0], listaF, "b+")
# plt.plot(lista2[0], lista2[1], color = "yellow", linestyle = "dashed")
# plt.show()

def integrabilna_funkcija(x):
    return x**2

listaGornjih = []
listaDonjih = []
listaTrapeznih = []
listaKoraka = []
listaAnalitickih = []

analitickoRj = 234
for i in range(1,8):
    n = i * 100
    listaKoraka.append(n)
    listaGornjih.append(calc.integral_pravokutni(integrabilna_funkcija, 3, 9, n)[0])
    listaDonjih.append(calc.integral_pravokutni(integrabilna_funkcija, 3, 9, n)[1])
    listaTrapeznih.append(calc.integral_trapezni(integrabilna_funkcija, 3, 9, n))
    listaAnalitickih.append(analitickoRj)


plt.scatter(listaKoraka, listaGornjih, s = 4)
plt.scatter(listaKoraka, listaDonjih, s = 4)
plt.scatter(listaKoraka, listaTrapeznih, s = 4, color = "red")
plt.plot(listaKoraka, listaAnalitickih, color = "green")
plt.show()