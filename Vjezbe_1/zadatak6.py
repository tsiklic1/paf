import numpy as np
import matplotlib.pyplot as plt



x = float(input("X koordinata točke"))
y = float(input("Y koordinata točke"))
xk = float(input("X koordinata središta kružnice"))
yk = float(input("Y koordinata središta kružnice"))
r = float(input("Radijus kružnice"))

tocka = [x,y]
kruznica = [xk,yk,r]

def polozaj(tocka, kruznica):
    if (tocka[0] - kruznica[0])**2 + (tocka[1] - kruznica[1])**2 > kruznica[2]**2:
        print("Točka je izvan kružnice")
    elif (tocka[0] - kruznica[0])**2 + (tocka[1] - kruznica[1])**2 == kruznica[2]**2:
        print("Točka je na kružnici")
    else:
        print("Točka je unutar kružnice")
    
    udaljenost = abs(((tocka[0] - kruznica[0])**2 + (tocka[1] - kruznica[1])**2)**(1/2)-kruznica[2])

    print("Udaljenost točke od kružnice je: ", udaljenost, ", a točka se nalazi na koordinatama (" + str(tocka[0]) + "," + str(tocka[1]) + ").")

    x = np.linspace(kruznica[0]-1*kruznica[2], kruznica[0]+kruznica[2], 100)
    y1 = (kruznica[2]**2 - (x-kruznica[0])**2)**(1/2) + kruznica[1]
    y2 = -(kruznica[2]**2 - (x-kruznica[0])**2)**(1/2) + kruznica[1]

    fig = plt.figure(figsize=(4,4), dpi = 200)
    axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])
    axes.set_aspect("equal")
    axes.plot(x, y1, "c")
    axes.plot(x, y2, "c")
    axes.plot([kruznica[0]],[kruznica[1]], "bo")
    axes.plot([tocka[0]],[tocka[1]], "ro")
    unos = input("Za ekran upišite 1, za PDF 2: ")
    
    if unos == "1":
        plt.show()
    else:
        ime = input("Unesite ime pod kojim želite spremiti file.")
        plt.savefig(ime + ".pdf")


polozaj(tocka, kruznica)
    