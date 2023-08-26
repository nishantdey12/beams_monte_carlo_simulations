import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.random import rand
D, L, N = 10, 8, 1000
# y = needle centres
y = rand(N)*D
# vertical distances between needle centres and needle ends
r = np.zeros(N)   #array
yy = np.zeros(N)   #array
for i in range(N):
        R = 2
        while R>1:
                X = rand()
                Y = rand()
                R = np.sqrt(X**2 + Y**2)
        r[i] = R
        yy[i] = Y
deltay = (L/2)*yy/r
# hits = True if needle touches line or False if not
hits = (deltay>= y) + (deltay >= D - y)

# print(hits)
count=0
# print(type(hits))
# f = Fraction that cross a line
f = np.mean(hits)
# Monte-Carlo estimate of pi
PI = 2*L/(f*D)
# print(PI)

x = np.arange(1, 1001)
y = np.pi * np.ones(1000)
Pi_part = np.empty(1000)

print(x)
for i in range(1, 1000):
    hits_part = hits[0:i]
    f_pat = np.mean(hits_part)
    Pi_part[i - 1] = 2 * L / (f_pat * D)

plt.scatter(x, Pi_part, s=5)
plt.plot(x,y, color='red' )
plt.show()
