import numpy as np
import matplotlib.pyplot as plt

import ArrayFactor
import ArrayPattern
import PointingPattern

# Definitions
def dft_codebook(dim):
    seq = np.matrix(np.arange(dim))
    mat = seq.conj().T * seq
    w = np.exp(-1j * 2 * np.pi * mat / dim)
    return w

#test pointing ULA
Na=32 #num antennas
Npointing=16 #num of pointing angles
N=1000 #grid resolution
thetas=np.linspace(-np.pi,np.pi,N) #angles
'''d=1
lambdac=2
normDistance=d/lambdac
angleWithArrayNormal=0
arrayFactors, thetas = ArrayFactor.arrayFactorsForULA(Na, thetas, d, lambdac, angleWithArrayNormal)
a = 0
angleInRad=np.pi/4 #choose an angle to point to'''

Nant=32# number of antennas
N=1000 #grid resolution
thetas=np.linspace(-np.pi,np.pi,N) #angles
# %default is distance among neighbor antennas to be 0.5 lambda
d=4
lambdac=2
angleInRad=np.pi/4
angleWithArrayNormal=0 #angle is with array axis (use cosine)
arrayFactors, thetas = ArrayFactor.arrayFactorsForULA(Nant,thetas,d,lambdac,angleWithArrayNormal)
antenna_index = 17
use_DFT = True
if use_DFT:
    w = dft_codebook(Nant) / np.sqrt(Nant) # Rx Codebook
    w=w[:, antenna_index] #make it a column vector and normalize it
else:
    w=np.exp(1j*2*np.pi*np.arange(0, Nant)*(d/lambdac)*np.cos(angleInRad)) #steering
    w=w[:, np.newaxis] #make it a column vector and normalize it

steeredArrayFactors= np.matmul(arrayFactors,w)
plt.polar(thetas,np.absolute(steeredArrayFactors))
plt.show()