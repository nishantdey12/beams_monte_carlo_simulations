#cylinder will buckle
#E=70+-10Gpa uniform distribution
#wall thickness 2mm Normal distribution of standard deviation 0.1 mm
#load P =300Kn and standard deviation 10kn
#poisson ratio constant 0.33
# we can count the number of trials in which a cylinder buckles. This will give us the fraction of failures, or, in other words, the probabilityof buckling.
'''
some clarification
uniform distribution means that all values will have equal probablity of occuring, which means rectangular shaped distribution
normal distribution has bell shaped curve, having more probablility towards mean and how spread out depends on standard deviation

https://www.varsitytutors.com/hotmath/hotmath_help/topics/normal-distribution-of-data#:~:text=The%20standard%20deviation%20is%20the,mean%20and%20the%20standard%20deviation.
'''
from numpy.random import rand, randn
import numpy as np

#  data
v = 0.33  # Poisson’s ratio
tnom = 0.002  # Nominal thickness [m]
Enom = 70E9  # Nominal Young’s modulus [Pa]
Pnom = 300000  # Nominal compressive  load[N]
sd_t = 1E-4  # Standard deviation of t [m]
r_E = 10E9  # Half range of E [Pa]
sd_P = 10000  # Standard deviation of P [N]

Pcal = 0.4*2*np.pi/np.sqrt(3*(1-v**2))
# print(Pcal)

N = 10**6

E = Enom + (2*rand(N)-1)*r_E  #uniform
t = tnom + randn(N)*sd_t  #normal
P = Pnom + randn(N)*sd_P  #normal
# print("Young modulus",E)
# print("Thickness",t)
# print("Load",P)
# P/Pcrit
Pratio = P/(Pcal*E*t**2)
failures = Pratio >= 1
print(failures)
# Overall failure probability
failprob = np.mean(failures)
print(failprob)


'''
Wilks method
target- reduce the number of runs in mc sim

we can only decide whether fail or no fail
so only two groups 
but here we will use continuous measure of probability to fail so that we can adopt order statistic method

IMPLEMENTATION
p/pcrit close to 1 means more close to failure
how many simul we run and how to use the worst values

confidence c
trials N
find the max value of p/pcrit, the value should be as large that it lies in top fraction f of normal distribution of p/pcrit
relation in book
'''
#still lot of things to understand
