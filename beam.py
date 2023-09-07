#h= separation between centroidal axis and neutral axis in a bent beam
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
#r=radius if circle
#rc=radius of centroidal axis
R=1; Rc=1.5
N=1000
#s=displacement fro axis
#r=radii
r=np.sqrt(rand(N)*R**4)
# array=np.linspace(1,1000, 1000)
# plt.scatter(array,r)
plt.show()
theta=rand(N)*2*np.pi
s=r*np.sin(theta) #take reference of polar coord
#s =distance between any point of beam measured from center of bending axis

#these are the numerator and denominator of h
deno=1/(Rc-s)#array
num=s*deno

h=np.trapz(num)/np.trapz(deno)
print(h)

#distribute points all over the cross section