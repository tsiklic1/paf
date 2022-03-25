import math
import numpy as np

def derivacija(f, x, h, metoda = 0):
    if metoda == 0:
        d = (f(x + h) - f(x - h))/(2*h)
    
    else:
        d = (f(x + h) - f(x))/h
    return d

def derivacija_2(f, a, b, h, metoda = 0):
    listaX = list(np.arange(a,b, h))
    listaD = []
    for i in listaX:
        listaD.append(derivacija(f, i, h, metoda))
    return [listaX, listaD]

def integral_pravokutni(f, a, b, n):
    listaX = list(np.linspace(a, b, n +1))
    dx = (b - a)/n
    
    gornjaMeda = 0
    donjaMeda = 0
    
    #print(listaX)
    for i in range(len(listaX) - 1):
        
        donjaMeda += f(listaX[i]) * dx
        gornjaMeda += f(listaX[i+1]) * dx
        #print(listaX[i], f(listaX[i]),f(listaX[i]) * dx)

    donjaMeda += f(listaX[-1] * dx)
    
    return [gornjaMeda, donjaMeda]

def integral_trapezni(f, a, b, n):
    listaX = list(np.linspace(a, b, n + 1))
    dx = (b - a)/n
    integral = 0
    for i in range(len(listaX) - 1):
        integral += f(listaX[i])*dx + (f(listaX[i+1]) - f(listaX[i])) * dx/2

    return integral




def funkcija(x):
    return x**2

#derivacija_2(funkcija, 0, 4, 0.001)
#derivacija(funkcija, 1)
# print(integral_pravokutni(funkcija, 3, 10, 100))
# print(integral_trapezni(funkcija, 3, 10, 100))