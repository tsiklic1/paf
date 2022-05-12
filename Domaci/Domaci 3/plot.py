import matplotlib.pyplot as plt

listaX = []
listaV = []
listaA = []
listaT = []
def prepisivanje(file, lista):
    with open(file, "r") as f:
        lista = f.readlines()
    return lista

listaStrX = prepisivanje("xt.txt", listaX)
listaStrV = prepisivanje("vt.txt", listaV)
listaStrA = prepisivanje("at.txt", listaA)
listaStrT = prepisivanje("t.txt", listaT)

for i in range(len(listaStrX)):
    listaX.append(float(listaStrX[i]))
    listaV.append(float(listaStrV[i]))
    listaA.append(float(listaStrA[i]))
    listaT.append(float(listaStrT[i]))

# plt.plot(listaT, listaX)

fig, axs = plt.subplots(1, figsize = (6,6))
axs.scatter(listaT, listaX, s = 0.4)
plt.setp(axs, xlabel = "t (s)")
plt.setp(axs, ylabel = "x (m)")
plt.show()


#plt.plot(listaT, listaA)

fig, axs = plt.subplots(1, figsize = (6,6))
axs.scatter(listaT, listaA, s = 0.4, color = "green")
plt.setp(axs, xlabel = "t (s)")
plt.setp(axs, ylabel = "a (m/s**2)")
plt.show()

#plt.plot(listaT,listaV)

fig, axs = plt.subplots(1, figsize = (6,6))
axs.scatter(listaT, listaV, s = 0.4, color = "red")
plt.setp(axs, xlabel = "t (s)")
plt.setp(axs, ylabel = "v (m/s)")
plt.show()
