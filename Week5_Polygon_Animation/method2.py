
# Some basic imports that are useful
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def morph(x1, y1, x2, y2, alpha):
    xm = (1-alpha) * x1 + (alpha) * x2
    ym = (1-alpha) * y1 + (alpha) * y2
    return xm, ym

def linpoly(n, r, npoints, offset_angle=0):
    x = []
    y = []
    pps = int(npoints/n)
    for i in range(n):
        x.extend(np.linspace(np.cos(offset_angle + (2*i*np.pi/n)),np.cos(offset_angle + (2*(i+1)*np.pi/n)),pps))
        y.extend(np.linspace(np.sin(offset_angle + (2*i*np.pi/n)),np.sin(offset_angle + (2*(i+1)*np.pi/n)),pps))
    x = np.array(x)
    y = np.array(y)
    return x,y 

# Initializing figures

npoints = 840
radius = 1
x1,y1 = linpoly(3, radius, npoints)
x2,y2 = linpoly(4, radius, npoints)
x3,y3 = linpoly(5, radius, npoints)
x4,y4 = linpoly(6, radius, npoints)
x5,y5 = linpoly(7, radius, npoints)
x6,y6 = linpoly(8, radius, npoints)


fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'r')

framenum = 1000

def init(): 
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    return ln,
def update(frame):
    # xdata.append(frame)
    # ydata.append(np.sin(frame))
    frame /= framenum/10000
    if (frame < 9):
        xdata, ydata = morph(x1, y1, x2, y2, frame/9)
        ln.set_data(xdata, ydata)
    elif (frame < 18):
        xdata, ydata = morph(x2, y2, x3, y3, (frame-9)/9)
        ln.set_data(xdata, ydata)        
    elif (frame < 27):
        xdata, ydata = morph(x3, y3, x4, y4, (frame-18)/9)
        ln.set_data(xdata, ydata)        
    elif (frame < 36):
        xdata, ydata = morph(x4, y4, x5, y5, (frame-27)/9)
        ln.set_data(xdata, ydata)        
    elif (frame < 45):
        xdata, ydata = morph(x5, y5, x6, y6, (frame-36)/9)
        ln.set_data(xdata, ydata)
    elif (frame < 55):
        pass
    elif (frame < 64):
        xdata, ydata = morph(x6, y6, x5, y5, (frame-55)/9)
        ln.set_data(xdata, ydata)        
    elif (frame < 73):
        xdata, ydata = morph(x5, y5, x4, y4, (frame-64)/9)
        ln.set_data(xdata, ydata)        
    elif (frame < 82):
        xdata, ydata = morph(x4, y4, x3, y3, (frame-73)/9)
        ln.set_data(xdata, ydata)        
    elif (frame < 91):
        xdata, ydata = morph(x3, y3, x2, y2, (frame-82)/9)
        ln.set_data(xdata, ydata)
    elif (frame <= 100):
        xdata, ydata = morph(x2, y2, x1, y1, (frame-91)/9)
        ln.set_data(xdata, ydata)


fig.suptitle('Polygon Morphing - Method 2, EE21B005 Aditya Mallick', fontsize=14)
ani = FuncAnimation(fig, update, frames=np.linspace(0, framenum/100, framenum + 1), init_func=init, blit=False, interval=(10000/framenum), repeat=False)
plt.show()
