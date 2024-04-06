#3p orbital plot
# 3p because it has radial and angular nodes and looks cool


import math
import matplotlib.pyplot as plt
import numpy as np
point=','
x=0
res=16
y=10**-7/(res*100)
z=10**-7/(res*100)

colourss=['#9E0142' ,'#D53E4F', '#F46D43', '#FDAE61' ,'#FEE08B' ,'#FFFFBF', '#E6F598', '#ABDDA4', '#66C2A5', '#3288BD' ,'#5E4FA2','#2D004B']

for q in range(12):
    ypoints=[]
    zpoints=[]
    for i in range(-124*res+1,124*res,2):
        for j in range(-150*res+1,150*res,2):
            yy=i*y
            zz=j*z
            phi=0
            a0=52.9*10**-10
            e=math.e
            r=(yy*yy+zz*zz)**0.5
            theta=math.asin(zz/r)
            psi=1/(81*(6*math.pi*a0**5)**0.5)*r/a0*(6-r/a0)*e**(-r/(3*a0))*math.sin(theta)
            if 10**(35+q*0.25-0.25)<psi**2<10**(35+q*0.25+0.25-0.25):
                ypoints.append(yy)
                zpoints.append(zz)

    yp = np.array(ypoints)
    zp = np.array(zpoints)
    plt.plot(zp, yp, point,color=colourss[q])

ypoints=[]
zpoints=[]
for i in range(-124*res+1,124*res,2):
    for j in range(-150*res+1,150*res,2):
        yy=i*y
        zz=j*z
        phi=0
        a0=52.9*10**-10
        e=math.e
        r=(yy*yy+zz*zz)**0.5
        theta=math.asin(zz/r)
        psi=1/(81*(6*math.pi*a0**5)**0.5)*r/a0*(6-r/a0)*e**(-r/(3*a0))*math.sin(theta)
        if 10**(35-0.25)>psi**2:
            ypoints.append(yy)
            zpoints.append(zz)

yp = np.array(ypoints)
zp = np.array(zpoints)

plt.plot(zp, yp, point,color='#000000')

plt.show()


