# Set up the imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
import math

# Step function for use in animation
def graddescstep(f, derivf, xstart, lr):
    bestx = xstart
    xtemp = bestx - derivf(bestx) * lr 
    bestx = xtemp
    y = f(bestx)
    return bestx
    
def testfunc(x):
    return x ** 2 + 3 * x + 8

def derivtestfunc(x):
    return 2*(x) + 3


# Create the axis and function
xbase = np.linspace(-5, 5, 100)
ybase = testfunc(xbase)

fig, ax = plt.subplots()
ax.plot(xbase, ybase)
xall, yall = [], []
lnall,  = ax.plot([], [], 'ro', markersize=4)
lngood, = ax.plot([], [], 'go', markersize=8)

xstart = 5
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
ani.save('EE21B005_2dplot1.gif')
plt.show()