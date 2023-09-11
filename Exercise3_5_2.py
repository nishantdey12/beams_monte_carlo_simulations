# Exercise3_5_2.py
# Monte-Carlo calculation of integral of y = sqrt(x)/

# sample mean method

from numpy.random import rand
import matplotlib.pyplot as plt
import numpy as np
# (1+0.1*sin(pi*x))
# from x = 0 to x = 1


def y_fn(x):
    return np.sqrt(x)/(1+0.1*np.sin(np.pi*x))


trials = 500
area = np.zeros(trials)
for i in range(trials):
    N = 500
    x = rand(N)
    yave = np.mean(y_fn(x))
    area[i] = yave*1
# summary statistics
mu = np.mean(area)
sigma = np.std(area)
se = sigma/np.sqrt(trials)
lo95 = mu - 1.96*se
hi95 = mu + 1.95*se

hist = plt.hist(area, 100, density=True)
plt.show()
plt.plot(hist[1][:-1], hist[0])
plt.show()

print("Mean area ", mu, "standard dev", sigma)
print("lower limit ", lo95)
print("higher limit ", hi95)
