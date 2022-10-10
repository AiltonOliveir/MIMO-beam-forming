import numpy as np

import ArrayPattern

def pointingPatternULA(arrayFactors, pointAngle, normDistance):
    #function steeredArrayFactors= pointingPatternULA(arrayFactors, ...
    #    pointAngle,normDistance)
    #If we want to point to specific direction pointAngle
    #for steering.
    numAntennas = arrayFactors.shape[1]#size(arrayFactors,2)
    w=np.exp(1j*2*np.pi*np.arange(0, numAntennas)*normDistance*np.cos(pointAngle)) #steering
    w=w[:, np.newaxis] / np.sqrt(numAntennas) #make it a column vector and normalize it
    steeredArrayFactors = np.matmul(arrayFactors,w)#arrayFactors * w
    return steeredArrayFactors

def pointingPatternUPA(Nax, Nay, normDistanceX, normDistanceY, pointAzimuth, pointElevation, N):
    azimuths=np.linspace(0,2*np.pi,N) #angles
    elevations=np.linspace(0,np.pi,N) #angles

    betax = -2*np.pi*normDistanceX*np.sin(pointElevation)*np.cos(pointAzimuth)
    betay= -2*np.pi*normDistanceY*np.sin(pointElevation)*np.sin(pointAzimuth)

    #linear phase
    wx = np.exp(1j*np.arange(0, Nax)*betax)
    wy = np.exp(1j*np.arange(0, Nay)*betay)

    THETAele, PHIazi = np.meshgrid(elevations,azimuths)

    upaArrayFactor = ArrayPattern.arrayPatternUPA(Nax, Nay, PHIazi, THETAele, normDistanceX, normDistanceY, wx, wy)
    return upaArrayFactor, THETAele, PHIazi
