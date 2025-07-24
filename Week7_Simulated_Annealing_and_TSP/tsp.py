# Set up imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys

def tsp(file, itnum, t, lr):
    x_cities = []
    y_cities = []
    num = int(file.readline().strip())
    finalorder = [i for i in range(num)]
    data = file.readlines()
    for line in data:
        line = line.split()
        x_cities.append(line[0])
        y_cities.append(line[1])
    x_cities = np.array(x_cities, dtype='float64')
    y_cities = np.array(y_cities, dtype='float64')
    finalorder = np.array(finalorder)
    x_bestorder = x_cities
    y_bestorder = y_cities
    bestdist = sys.float_info.max
    for j in range(itnum):
        ind1 = np.random.randint(0, num)
        ind2 = np.random.randint(0, num)
        x_cities[min(ind1,ind2):max(ind1,ind2)] = x_cities[min(ind1,ind2):max(ind1,ind2)][::-1]
        y_cities[min(ind1,ind2):max(ind1,ind2)] = y_cities[min(ind1,ind2):max(ind1,ind2)][::-1]
        finalorder[min(ind1,ind2):max(ind1,ind2)] = finalorder[min(ind1,ind2):max(ind1,ind2)][::-1]
        dist = 0
        for i in range(num):
            dist += (((x_cities[i] - x_cities[(i + 1) % num])**2) + ((y_cities[i] - y_cities[(i + 1) % num])**2))**0.5
        if dist < bestdist:
            bestdist = dist
            x_bestorder = np.copy(x_cities)
            y_bestorder = np.copy(y_cities)
        else:
            toss = np.random.random_sample()
            if toss < np.exp(-(dist-bestdist)/t):
                bestdist = dist
                x_bestorder = np.copy(x_cities)
                y_bestorder = np.copy(y_cities)
            else:
                x_cities[min(ind1,ind2):max(ind1,ind2)] = x_cities[min(ind1,ind2):max(ind1,ind2)][::-1]
                y_cities[min(ind1,ind2):max(ind1,ind2)] = y_cities[min(ind1,ind2):max(ind1,ind2)][::-1]
                finalorder[min(ind1,ind2):max(ind1,ind2)] = finalorder[min(ind1,ind2):max(ind1,ind2)][::-1]
                pass
        t = t * lr
    
    x_bestorder = np.append(x_bestorder, x_bestorder[0])
    y_bestorder = np.append(y_bestorder, y_bestorder[0])
    return finalorder, bestdist, x_bestorder, y_bestorder
    
minn = [0,sys.float_info.max,0,0]
for i in range(10):
    with open(f'EE21B005 Assignment 7/Salesman/tsp_100.txt') as f:
        newmin = tsp(f, 10000, 10000, 0.99)
        if (newmin[1] < minn[1]):
            minn = newmin
print(minn[0], minn[1])
plt.figure()
plt.plot(minn[2], minn[3], 'o-')
plt.show()
    
    