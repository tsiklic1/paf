import projektil as pro
#stavljeno je da vjetar utječe na projektil tako što mu mijenja brzinu uz koeficjent 0.1
p1 = pro.ProjectileDrop(2000, 200)
p2 = pro.ProjectileDrop(2000, 200)

p1.meta(20000, 10, -100)
p2.meta(20000, 10, 0)

