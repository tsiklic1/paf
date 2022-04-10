import jednodimenzionalno as jd

def konstantna_sila(x, v, t):
    return 10

def elasticna_sila(x, v, t):
    return -10*x

g1 = jd.gibanje(konstantna_sila, 0, 0, 1, 2)
g2 = jd.gibanje(elasticna_sila, 0.3, 0, 0.1, 2)

g1.plot_trajectory()
g2.plot_trajectory()
