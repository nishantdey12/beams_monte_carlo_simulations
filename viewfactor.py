import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

X, Y, Z = 1, 1, 2
trials = 400
N = 1000
vf = np.zeros(trials)  # view factors

for trial in range(0, trials):
    # generates array of random N random numbers unformly distributed
    x = rand(N)*X
    yh = rand(N)*Y
    theta = np.arccos(1-2*rand(N))/2  # weighted random numbers
    # n is a random number uniformly distributed
    # input ranfe of cos inv
    phi = rand(N)*np.pi-np.pi/2

    # points on vertical plane
    dy = x*np.tan(phi)
    yv = yh+dy
    z = np.sqrt(x**2+dy**2)*np.tan(np.pi/2-theta)

    # number of points that hits the surface
    hits = sum((z > 0)*(z < Z)*(yv > 0) * (yv < Y))
    vf[trial] = hits/(2*N)

# print(vf)

trial_array = np.linspace(1, 401, 400)

plt.scatter(trial_array, vf)  # plotting actual view factors
mu = np.mean(vf)
sigma = np.std(vf)
se = sigma/np.sqrt(trials)
print(mu, sigma, se)
mu = np.full(400, mu)  # plotting mean
plt.plot(trial_array, mu, "red")
plt.legend()
plt.show()
