from operator import truediv
from statistics import variance
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.random import rand
D, L, N = 10, 8, 2000
# y = needle centres
y = rand(N)*D
# vertical distances between needle centres and needle ends
r = np.zeros(N)  # array
yy = np.zeros(N)  # array
for i in range(N):
    R = 2
    while R > 1:
        X = rand()
        Y = rand()
        R = np.sqrt(X**2 + Y**2)
    r[i] = R
    yy[i] = Y
deltay = (L/2)*yy/r
# hits = True if needle touches line or False if not
hits = (deltay >= y) + (deltay >= D - y)
# print(hits)
count = 0
# print(type(hits))
# f = Fraction that cross a line
f = np.mean(hits)  # this is the probablity that the needle will cross a line
# print (f)
# Monte-Carlo estimate of pi
PI = 2*L/(f*D)
print(PI)

x = np.arange(1, 1001)
y = np.pi * np.ones(2000)
Pi_part = np.empty(2000)

# print(x)

for i in range(1, 999):  # cumulative approach to find the value of pi in each step
    hits_part = hits[0:i]
    f_pat = np.mean(hits_part)
    Pi_part[i - 1] = 2 * L / (f_pat * D)

# effort to find the histogram
min = np.min(Pi_part)
max = np.max(Pi_part)
sub_intervals = (max-min)/100  # 100 intervals

No_of_values_in_interval = np.zeros(100)
start = min
for i in range(0, 100, 1):
    end = start+sub_intervals
    t = np.where((Pi_part >= start) & (Pi_part < end))
    # print(t[0])
    No_of_values_in_interval[i] = len(t[0])

pdf=plt.hist(Pi_part, 2000, range=[0, 5], density=True)
plt.show()
#pdf and cdf thing going on
plt.plot(pdf[1][:-1], pdf[0])
plt.show()
plt.scatter(x, Pi_part, s=5)
plt.plot(x, y, color='red')  # the pie line
plt.show()

# calculate mean
mean = np.mean(Pi_part)
std = np.std(Pi_part)
variance = np.std(Pi_part)
print("Mean=", mean)
print("Standard deviation", std)
print("variance ", variance)
