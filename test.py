from Vect3D import *
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import fmin
import math

v0 = Vect3D(0,0,0)
v1 = Vect3D(1,0,0)
v2 = Vect3D(2,1,1)
v3 = Vect3D(1,2,1)

p1 = [v0.x, v0.y]
p2 = [v3.x, v3.y]
p3 = [v1.x, v1.y]
p4 = [v2.x, v2.y]

xc = 1.5
yc = 1

a1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
a2 = (p4[1] - p3[1]) / (p4[0] - p3[0])

b1 = p2[1] - a1 * p2[0]
b2 = p4[1] - a2 * p4[0]




def x_1(x):
    return (b1 + x * xc - yc) / (x - a1)


def y_1(x):
    return (b1 * x + a1 * x * xc - a1 * yc) / (x - a1)


def x_2(x):
    return (b2 + x * xc - yc) / (x - a2)


def y_2(x):
    return (b2 * x + a2 * x * xc - a2 * yc) / (x - a2)

def D(x):
    return (x_1(x) - x_2(x))**2 + (y_1(x) - y_2(x))**2

t = np.linspace(-10,0,100)
m1 = fmin(D, [0])
plt.plot(t, D(t))
plt.show()

u1 = math.sqrt((xc - x_1(m1))**2 + (yc - y_1(m1))**2)
u2 = math.sqrt((xc - x_2(m1))**2 + (yc - y_2(m1))**2)
sx = (x_1(m1) + x_2(m1))/2
sy = (y_1(m1) + y_2(m1))/2
us = math.sqrt((xc - sx)**2 + (yc - sy)**2)
u = us / (u1 + u2) * 2

print(y_1(m1))
print(x_1(m1))
print(y_2(m1))
print(x_2(m1))

p1 = [v0.x, v0.y]
p2 = [v1.x, v1.y]
p3 = [v3.x, v3.y]
p4 = [v2.x, v2.y]

xc = 1.1
yc = 0.3

a1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
a2 = (p4[1] - p3[1]) / (p4[0] - p3[0])

b1 = p2[1] - a1 * p2[0]
b2 = p4[1] - a2 * p4[0]

t = np.linspace(1,10,100)

m2 = fmin(D, [2])
print(m2)
plt.plot(t, D(t))
plt.show()

print(y_1(m2))
print(x_1(m2))
print(y_2(m2))
print(x_2(m2))

v1 = math.sqrt((xc - x_1(m2))**2 + (yc - y_1(m2))**2)
v2 = math.sqrt((xc - x_2(m2))**2 + (yc - y_2(m2))**2)
sx = (x_1(m2) + x_2(m2))/2
sy = (y_1(m2) + y_2(m2))/2
vs = math.sqrt((xc - sx)**2 + (yc - sy)**2)
v = vs / (v1 + v2) * 2


print(u)
print(v)
#print("u: %s, u: %s" % m1, m2)

