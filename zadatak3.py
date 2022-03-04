import matplotlib.pyplot as plt

def jeLiBroj(unos):
    br = 0
    for i in unos:
        if not(i.isdigit()):
            br += 1
            break
    if br == 0 and len(unos) != 0:
        return True
    
    else:
        return False

def jednadbaPravca(x1, y1, x2, y2):
    k = (y2-y1)/(x2-x1)
    l = k*(-1*x1) + y1
    print("y = ", k, "x + ", l)

def ekranIliPdf(x1, y1, x2, y2):
    unos = input("Za ekran upišite 1, za PDF 2: ")
    plt.plot([x1,y1,x2,y2])
    if unos == "1":
        plt.show()
    else:
        plt.savefig("plot.pdf")

x1 = input("x1 ")
while jeLiBroj(x1) == False:
    x1 = input("Unijeli ste nešto što nije broj. Pokušajte ponovo. ")
x1 = int(x1)
y1 = input("y1 ")
while jeLiBroj(y1) == False:
    y1 = input("Unijeli ste nešto što nije broj. Pokušajte ponovo. ")
y1 = int(y1)
x2 = input("x2 ")
while jeLiBroj(x2) == False:
    x2 = input("Unijeli ste nešto što nije broj. Pokušajte ponovo. ")
x2 = int(x2)
y2 = input("y2 ")
while jeLiBroj(y2) == False:
    y2 = input("Unijeli ste nešto što nije broj. Pokušajte ponovo. ")
y2 = int(y2)


ekranIliPdf(x1,y1,x2,y2)