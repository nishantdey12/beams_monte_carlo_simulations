# calculate the area integral 2/root(pie) e^(-z2/2)
# random points spread on the entire area

from reprlib import aRepr
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

# two coordinates are y and z
N = 1000
eta = 2.5
ymax = 2/np.sqrt(np.pi)
# print(ymax)
y = rand(N)*ymax    # 2/root(pie)
z = rand(N)*eta/2   # here y, z are arrays

hits = (y <= (ymax * np.exp(-z**2)))
f = np.sum(hits)/N
area = f*eta/np.sqrt(np.pi)
print(area)

# true value of area is 0.923

d = np.linspace(0, 2.5, 1000)
z_function = np.exp(-np.power(d, 2))*ymax
x = np.linspace(0, 1000, 1000)
# print(z_function)
plt.plot(x, z_function, color="red")  # plotting actual curve
plt.scatter(x, ymax * np.exp(-z**2))  # plotting the random points
plt.show()

t = (ymax * np.exp(-z**2))
mean = np.mean(t)
sd = np.std(t)
var = np.var(t)
standard_error = sd/np.sqrt(N)
print(mean, sd, var, standard_error)

area_part = np.empty(1000)
for i in range(1, 999):  # cumulative approach to find the value of pi in each step
    hits_part = hits[0:i]
    f_pat = np.mean(hits_part)
    area_part[i - 1] = f_pat*eta/np.sqrt(np.pi)

pdf = plt.hist(area_part, 1000, density=True)
plt.plot(pdf[1][:-1], pdf[0])
plt.legend(["cDF","pdf"])
plt.show()
# something interesting happening
