import matplotlib.pyplot as plt
import numpy as np

def jeLiBroj(unos):
    try: 
        broj = int(unos)
        return "int"
    except ValueError:
        try: 
            broj = float(unos)
            return "float"
        except ValueError:
            return "greska"

def petljaZaUnos(unos):
    while jeLiBroj(unos) == "greska":
        unos = input("Unijeli ste nešto što nije broj. Pokušajte ponovo. ")
    tip = jeLiBroj(unos)
    if tip == "int":
        broj = int(unos)
    elif tip == "float":
        broj = float(unos)
    return broj


def jednadbaPravca(x1, y1, x2, y2):
    k = (y2-y1)/(x2-x1)
    l = k*(-1*x1) + y1
    print("y = ", k, "x + ", l)
    lista = [k,l]
    return lista

def ekranIliPdf(lista):
    unos = input("Za ekran upišite 1, za PDF 2: ")
    x = np.linspace(x1-5,x2+5,100)
    y = lista[0]*x + lista[1]
    plt.plot(x, y)
    plt.plot([x1,x2], [y1,y2], "ro")
    
    if unos == "1":
        plt.show()
    else:
        ime = input("Unesite ime pod kojim želite spremiti file.")
        plt.savefig(ime + ".pdf")



x1 = input("x1 ")
x1 = petljaZaUnos(x1)
y1 = input("y1 ")
y1 = petljaZaUnos(y1)
x2 = input("x2 ")
x2 = petljaZaUnos(x2)
while x2 == x1:
    x2 = input("Unijeli ste 2 iste x koordinate za različite točke i jednadžba neće raditi. Pokušajte ponovo.")
    x2 = petljaZaUnos(x2)
y2 = input("y2 ")
y2 = petljaZaUnos(y2)


ekranIliPdf(jednadbaPravca(x1, y1, x2, y2))