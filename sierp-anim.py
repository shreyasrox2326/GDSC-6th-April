import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.animation as animation

xx=[1, 11, 6]
yy=[1, 1, 1+5*3**0.5]

p=[[1,1],[11,1],[6,1+5*3**0.5]]
z=[2,2]

fig, ax = plt.subplots()
line, = ax.plot(xx, yy, ',')

xx_anim = []
yy_anim = []

def update(frame, num_points):
    global xx_anim, yy_anim

    if frame == 0:
        xx_anim = xx.copy()
        yy_anim = yy.copy()

    for i in range(num_points):
        x = random.randint(0, 2)
        y = p[x]
        z[0] = (z[0] + y[0]) / 2
        z[1] = (z[1] + y[1]) / 2
        xx_anim.append(z[0])
        yy_anim.append(z[1])

    line.set_data(xx_anim, yy_anim)
    ax.set_xlim([min(xx_anim), max(xx_anim)])
    ax.set_ylim([min(yy_anim), max(yy_anim)])

ani = animation.FuncAnimation(fig, update, frames=500, interval=30, fargs=(1000,))

plt.show()