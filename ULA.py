import numpy as np
import matplotlib.pyplot as plt

import ArrayFactor
import ArrayPattern
import PointingPattern

#test pointing ULA
Na=32 #num antennas
Npointing=16 #num of pointing angles
N=1000 #grid resolution
thetas=np.linspace(-np.pi,np.pi,N) #angles
d=1
lambdac=2
normDistance=d/lambdac
angleWithArrayNormal=0
arrayFactors, thetas = ArrayFactor.arrayFactorsForULA(Na, thetas, d, lambdac, angleWithArrayNormal)
a = 0
angleInRad=np.pi/4 #choose an angle to point to

Nant=4# number of antennas
N=1000 #grid resolution
thetas=np.linspace(-np.pi,np.pi,N) #angles
# %default is distance among neighbor antennas to be 0.5 lambda
d=1
lambdac=2
angleWithArrayNormal=0 #angle is with array axis (use cosine)
arrayFactors, thetas = ArrayFactor.arrayFactorsForULA(Nant,thetas,d,lambdac,angleWithArrayNormal)

w=np.exp(1j*2*np.pi*np.arange(0, Nant)*(d/lambdac)*np.cos(angleInRad)) #steering
w=w[:, np.newaxis] / np.sqrt(Nant) #make it a column vector and normalize it
steeredArrayFactors= np.matmul(arrayFactors,w)
plt.polar(thetas,np.absolute(steeredArrayFactors))
plt.show()