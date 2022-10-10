import numpy as np

import ArrayFactor

def arrayPatternULA(numAntennaElements, thetas, normalizedDist, w, angleWithArrayNormal):
    arrayFactors = ArrayFactor.arrayFactorsForULA(numAntennaElements, thetas, normalizedDist, 1, angleWithArrayNormal)
    w=w[:, np.newaxis] #make it a column vector if not
    steeredArrayFactors = arrayFactors * w
    return steeredArrayFactors

def arrayPatternUPA(numAntennasX, numAntennasY, azimuths, elevations, normalizedDistX, normalizedDistY, wx, wy):
    #function upaArrayFactor = arrayPatternUPA(numAntennasX, numAntennasY, ...
    #    azimuths, elevations, normalizedDistX, normalizedDistY, wx, wy)
    #Adapted from Eqs. (6.7) and (6.85) of Balanis' book. It is more general
    #than Eqs. (6.7) and (6.85) in the sense
    #that supports arbitrary precoding vectors wx and wy, while (6.85) assumes
    #linear phase beta.
    phi=azimuths
    theta=elevations
    #Angle Psi but without incorporating the pointing angle beta in (6.85)
    psiAngleX=2*np.pi*normalizedDistX*np.sin(theta)*np.cos(phi)
    #consider below the case of n=0: all angles x are zero and e^jx = 1
    arrayFactorsX = np.zeros((psiAngleX.shape))#np.zeros(size(psiAngleX))
    #complete the summation with other parcels:
    for n in range(0, numAntennasX):#n=1:numAntennasX
        #arrayFactorsX = arrayFactorsX + exp(1j*((n-1)*psiAngleX + wx(n)));
        arrayFactorsX = arrayFactorsX + np.exp(1j*((n-1)*psiAngleX))*wx[n]
        #print(wx[n])
    #print(arrayFactorsX)
    #print(arrayFactorsX)
    #Angle Psi but without incorporating the pointing angle beta in (6.85)
    psiAngleY=2*np.pi*normalizedDistY*np.sin(theta)*np.sin(phi)
    #consider below the case of n=0: all angles x are zero and e^jx = 1
    arrayFactorsY = np.zeros((psiAngleY.shape))#np.zeros(size(psiAngleY))
    #complete the summation with other parcels:
    for n in range(0, numAntennasY):#n=1:numAntennasY
        #arrayFactorsY = arrayFactorsY + exp(1j*((n-1)*psiAngleY + wy(n)));
        arrayFactorsY = arrayFactorsY + np.exp(1j*((n-1)*psiAngleY))*wy[n]

    upaArrayFactor = arrayFactorsX * arrayFactorsY
    #normalize
    upaArrayFactor = upaArrayFactor / np.sqrt(numAntennasX*numAntennasY)
    return upaArrayFactor
