# Set up the imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
import math
from numpy import cos, sin, pi, exp 

# Step function for use in animation
def graddescstep(f, derivf, xstart, lr):
    bestx = xstart
    xtemp = bestx - derivf(bestx) * lr 
    bestx = xtemp
    y = f(bestx)
    return bestx
    
def testfunc(x):
    return cos(x)**4 - sin(x)**3 - 4*sin(x)**2 + cos(x) + 1

def derivtestfunc(x):
    return -4*sin(x)*(cos(x))**3 - 3*cos(x)*(sin(x)**2) - 8*sin(x)*cos(x) - sin(x)


# Create the axis and function
xbase = np.linspace(-pi, pi, 100)
ybase = testfunc(xbase)

fig, ax = plt.subplots()
ax.plot(xbase, ybase)
xall, yall = [], []
lnall,  = ax.plot([], [], 'ro', markersize=4)
lngood, = ax.plot([], [], 'go', markersize=8)

xstart = 0.1
ystart = testfunc(xstart)

def plotbest(frame):
    global xstart, ystart
    lngood.set_data(xstart, ystart)
    xall.append(xstart)
    yall.append(ystart)
    lnall.set_data(xall, yall)
    x = graddescstep(testfunc, derivtestfunc, xstart, 0.05)
    xstart = x
    ystart = testfunc(xstart)

ani= FuncAnimation(fig, plotbest, frames=range(200), interval=50, repeat=False)
ani.save('EE21B005_2dplot2_right.gif')
plt.show()