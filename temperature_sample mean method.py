import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
'''
the area under the curve is average value of curve multiplied over the range of interval
function is to be integrated for a number of z values taken randomly from 0 to eta/2. we calculate the value of function at these points, take mean and then multiply with range of z
'''
N=500
eta=2.5
ymax=2/np.sqrt(np.pi)
z=rand(N)*eta/2   # here y, z are arrays
y=ymax* np.exp(-z**2)    # 2/root(pie)

y_avg=np.mean(y)
area=y_avg*eta/2  #area=average*range
print(area)
plt.scatter(np.linspace(1,500,500),y)
plt.show()
