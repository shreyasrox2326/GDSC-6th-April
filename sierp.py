import matplotlib.pyplot as plt
import numpy as np
import random
xx=[1, 11, 6]
yy=[1, 1, 1+5*3**0.5]

p=[[1,1],[11,1],[6,1+5*3**0.5]]
z=[2,2]
for i in range(10000):
    x=random.randint(0,2)
    y=p[x]
    z[0]=(z[0]+y[0])/2
    z[1]=(z[1]+y[1])/2
    xx.append(z[0])
    yy.append(z[1])

xpoints = np.array(xx)
ypoints = np.array(yy)
plt.plot(xpoints, ypoints, ',')
plt.show()
