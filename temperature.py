#calculate the area integral 2/root(pie) e^(-z2/2)
# random points spread on the entire area

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

# two coordinates are y and z
N=10000
eta=2.5
ymax=2/np.sqrt(np.pi)
# print(ymax)
y=rand(N)*ymax    # 2/root(pie)
z=rand(N)*eta/2   # here y, z are arrays

hits= (y<=(ymax* np.exp(-z**2)))
f=np.sum(hits)/N
area=f*eta/np.sqrt(np.pi)
print(area)

d=np.linspace(0,2.5,10000)
z_function=np.exp(-np.power(d,2))*ymax
x = np.linspace(0, 10000,10000)
# print(z_function)
plt.plot(x,z_function, color="red")
plt.scatter(x,ymax* np.exp(-z**2))
plt.show()

t=(ymax* np.exp(-z**2))
mean=np.mean(t)
sd=np.std(t)
var=np.var(t)
standard_error=sd/np.sqrt(N)
print(mean, sd, var, standard_error)

#something interesting happening