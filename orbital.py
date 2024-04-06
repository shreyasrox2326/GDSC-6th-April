#3px orbital plot
#3px because it has radial and angular nodes and looks cool


import math
import matplotlib.pyplot as plt
import numpy as np

x=0

choicelist=[[1,'.'],[2,'.'],[4,','],[8,','],[16,',']]

choice=int(input("Enter your resolution choice\ncan be 1,2,3,4 or 5.\nhigher num=higher resolution(double)\n1 and 2 are instant,3 takes a few seconds,4 and 5 are not recommended\nChoice: "))
res=choicelist[choice-1][0] #resolution variable, keep 4 for fast plot, 8 or 16 for higher resolution (16 takes 2 minutes to plot not recommended)
point=choicelist[choice-1][1]
y=10**-7/(res*100)
z=10**-7/(res*100)
#colourss variable contains list of colours for getting a gradient according to probability density
colourss=['#9E0142' ,'#D53E4F', '#F46D43', '#FDAE61' ,'#FEE08B' ,'#FFFFBF', '#E6F598', '#ABDDA4', '#66C2A5', '#3288BD' ,'#5E4FA2','#2D004B']

#to fill in the colours for each pixel according to the probablity density function
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
            r=(yy*yy+zz*zz)**0.5 #converting x and y to r and theta
            theta=math.asin(zz/r)
            #psi**2 is the probabilty density function
            psi=1/(81*(6*math.pi*a0**5)**0.5)*r/a0*(6-r/a0)*e**(-r/(3*a0))*math.sin(theta)
            if 10**(35+q*0.25-0.25)<psi**2<10**(35+q*0.25+0.25-0.25):
                ypoints.append(yy)
                zpoints.append(zz)
    #plot colour according to value of psi**2
    yp = np.array(ypoints)
    zp = np.array(zpoints)
    plt.plot(zp, yp, point,color=colourss[q])

ypoints=[]
zpoints=[]
# to colour the remaining area black
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
#colour the remaining area black
plt.plot(zp, yp, point,color='#000000')

plt.show()


