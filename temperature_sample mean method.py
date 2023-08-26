import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

N=500
eta=2.5
ymax=2/np.sqrt(np.pi)
z=rand(N)*eta/2   # here y, z are arrays
y=ymax* np.exp(-z**2)    # 2/root(pie)

y_avg=np.mean(y)
area=y_avg*eta/2  #area=average*range
print(area)

