import jednodimenzionalno as jd

def konstantna_sila(x, v, t):
    return 10

def elasticna_sila(x, v, t):
    return -10*x

def cudna_sila(x, v, t):
    return 3*v + 8 - x**3

g1 = jd.gibanje(konstantna_sila, 0, 0, 1, 2)
g2 = jd.gibanje(elasticna_sila, 0.3, 0, 0.1, 2)
g3 = jd.gibanje(cudna_sila, 0, -2, 3, 4)

g1.plot_trajectory()
g2.plot_trajectory()
g3.plot_trajectory()