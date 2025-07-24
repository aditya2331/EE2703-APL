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

def multivargraddescstep(f, grad, start, lr):
    bestinputs = start
    direction = grad(bestinputs)
    tempinputs = bestinputs - direction * lr 
    bestinputs = tempinputs
    return bestinputs

def testfunc(inputs):
    # x^2 + y^2
    return inputs[0]**2 + inputs[1]**2

def vecgradientfunc(inputs):
    # (2x)î + (2y)ĵ
    return np.array([2*inputs[0],2*inputs[1]])

# Create the basic x and y arrays for choosing limits of plot
xbase = np.linspace(-10, 10, 20)
ybase = np.linspace(-10, 10, 20)

# Initialize matrices for surface plotting
xbase, ybase = np.meshgrid(xbase, ybase)
zbase = testfunc([xbase,ybase])
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plot the surface
ax.plot_surface(xbase, ybase, zbase, color='gainsboro',alpha = 0.5)

# Initialize matrices for points along the taken path
xall, yall, zall = [], [], []
lnall,  = ax.plot3D([], [], [], 'ro')
lngood, = ax.plot3D([], [], [], 'go', markersize=10)

# Initialize starting point
inputs = np.array([-10,0])
zstart = testfunc(inputs)

# Update path
def multidimplotbest(frame):
    global inputs, zstart
    xall.append(inputs[0])
    yall.append(inputs[1])
    zall.append(zstart)
    temp = multivargraddescstep(testfunc, vecgradientfunc, inputs, 0.05)
    inputs = temp
    zstart = testfunc(inputs)
    ax.plot(xall, yall, zall, color='red')
    

ani= FuncAnimation(fig, multidimplotbest, frames=range(150), interval=1, repeat=False)
ani.save('EE21B005_3dplot1.gif')
plt.show()