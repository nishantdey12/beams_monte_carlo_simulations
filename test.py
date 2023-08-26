# eta = x/sqrt(alpha*t), ymax = rectangle height
import numpy as np
from numpy.random import rand
eta = 2.5
ymax = 2/np.sqrt(np.pi)
# Number of points
N = 1000
# N random values of z and y
z = rand(N)*eta/2
y = rand(N)*ymax
# hits = True if points lie on or below curve
hits = y<=ymax*np.exp(-z**2)
# f = Fraction of points lying on or below curve.
f = np.sum(hits)/N
# Corresponding estimate of the area.
area = f*eta/np.sqrt(np.pi)
print(area)
t=ymax*np.exp(-z**2)
mean=np.mean(t)
sd=np.std(t)
var=np.var(t)
standard_error=sd/np.sqrt(N)
print(mean, sd, var, standard_error)