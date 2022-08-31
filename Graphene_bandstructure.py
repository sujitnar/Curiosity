#!/usr/bin/env python3

import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import assoc_laguerre
from scipy.special import eval_genlaguerre
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib import cm
import pylab as py
from mpl_toolkits.axes_grid1 import make_axes_locatable
import utils2 as utils2
from numpy.linalg import inv
from numpy.linalg import matrix_power
from mpl_toolkits.mplot3d import axes3d
from matplotlib.ticker import LinearLocator
t1 = 2.7
t2 = 0.54




def energy1(x,y):
    func = 2 * np.cos(np.sqrt(3) * y) + 4 * np.cos(0.5 * np.sqrt(3) * y) * np.cos(1.5 * x)
    gunc = np.sqrt(3 + func)
    e1 = t1*gunc - t2*func
    return e1

def energy2(x,y):
    func = 2 * np.cos(np.sqrt(3) * y) + 4 * np.cos(0.5 * np.sqrt(3) * y) * np.cos(1.5 * x)
    gunc = np.sqrt(3 + func)
    e2 = -t1*gunc - t2*func
    return e2
def energy3(x,y):
    e3= 3*t2 + 1.5*(np.sqrt(x**2 + y**2))
    return e3

def energy4(x,y):
    e4= 3*t2 - 1.5*(np.sqrt(x**2 + y**2))
    return e4




X = np.linspace(-4,4,200)
Y = np.linspace(-4,4,200)
X, Y = np.meshgrid(X,Y)
Z1 = energy1(X,Y)
Z2 = energy2(X,Y)
# Z3 = energy3(X,Y)
# Z4=energy4(X,Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(X,Y,Z2,rstride=1,cstride=1,cmap='viridis_r',edgecolor = 'none')
ax.plot_surface(X,Y,Z1,rstride=1,cstride=1,cmap='viridis',edgecolor = 'none')

ax.set_xlabel('$k_x$')
ax.set_ylabel('$k_y$')
ax.set_title('$\epsilon(\~ k)$')
#plt.axis('off')
plt.show()