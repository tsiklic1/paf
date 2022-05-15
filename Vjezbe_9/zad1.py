import bungee_jumping as bun
import numpy as np
import matplotlib.pyplot as plt

skakac1 = bun.bungee_jump(80, 100, 0.7 , 1, 1.22, 30, 100)
skakac1.plot_trajectory()
skakac2 = bun.bungee_jump(80, 100, 0 , 1, 1.22, 30, 100)
skakac2.plot_trajectory()