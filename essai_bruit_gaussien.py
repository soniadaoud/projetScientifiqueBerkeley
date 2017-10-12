import numpy
from matplotlib.pyplot import *
import math
import random


def aleaGauss(sigma):
    U1 = random.random()
    U2 = random.random()
    return sigma*math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2)

def signal(t):
    return 1.0*math.cos(2*math.pi*t)+0.5*math.cos(6*math.pi*t+math.pi/3)


N=1000
T = 2.0
dt = T/N
y = numpy.zeros(N)
t = numpy.zeros(N)
sigma = 0.1
for k in range(N):
    t[k] = k*dt
    y[k] = signal(t[k])+aleaGauss(sigma)
figure(figsize=(12,4))
plot(t,y)
show()
