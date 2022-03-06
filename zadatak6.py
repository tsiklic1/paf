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

    print("Udaljenost točke od kružnice je: ", udaljenost)

    x = np.linspace(kruznica[0]-1*kruznica[2], kruznica[0]+kruznica[2], 100)
    y1 = (kruznica[2]**2 - (x-kruznica[0])**2)**(1/2) + kruznica[1]
    y2 = -(kruznica[2]**2 - (x-kruznica[0])**2)**(1/2) + kruznica[1]

    plt.plot(x, y1, "c")
    plt.plot(x, y2, "c")
    plt.plot([kruznica[0]],[kruznica[1]], "bo")
    plt.plot([tocka[0]],[tocka[1]], "ro")
    plt.show()

polozaj(tocka, kruznica)
    