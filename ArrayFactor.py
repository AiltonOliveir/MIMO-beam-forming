import numpy as np

def arrayFactorsForULA(numAntennaElements, thetas, d, lambdac, angleWithArrayNormal):
    #function [arrayFactors, thetas] = arrayFactorsForULA(numAntennaElements,...
    #    thetas,d,lambdac,angleWithArrayNormal)
    #Gets the parcels of the array factor (before summation) for all angles.
    #This allows to take precoding / steering in account later on.
    #If angleWithArrayNormal=0 (default),the angle is between the input 
    #signal and the array axis. In this case
    #when theta=0, the signal direction is parallel to the array
    #axis and there is no energy. The maximum values are for directions 90
    #and -90 degrees, which are orthogonal with array axis.
    #If angleWithArrayNormal=1, angle is with the array normal, which uses
    #sine instead of cosine. In this case, the maxima are for
    #thetas = 0 and 180 degrees.
    #References:
    #http://www.waves.utoronto.ca/prof/svhum/ece422/notes/15-arrays2.pdf
    #Book by Balanis, book by Tse.
    #Example of usage:
    # Nant=4; %number of antennas
    # N=1000; %grid resolution
    # thetas=linspace(-pi,pi,N); %angles
    # %default is distance among neighbor antennas to be 0.5 lambda
    # d=1;
    # lambdac=2;
    # angleWithArrayNormal=0; %angle is with array axis (use cosine)
    # [arrayFactors, thetas] = arrayFactorsForULA(Nant,...
    #     thetas,d,lambdac,angleWithArrayNormal);
    # angleInRad=pi/4; %choose an angle to point to
    # w=exp(1j*2*pi*(0:Nant-1)*(d/lambdac)*cos(angleInRad)); %steering
    # w=w(:) / sqrt(Nant); %make it a column vector and normalize it
    # steeredArrayFactors= arrayFactors * w;
    # polarplot(thetas,abs(steeredArrayFactors))
    # title(['Angle = ' num2str(angleInRad*180/pi) ' degrees']);

    thetas=thetas[:, np.newaxis]#thetas[:]# %make it a column vector
    normDistance=d/lambdac
    normDistance= 0.5
    #print(thetas.shape)
    if angleWithArrayNormal == 1:
        temp = -1j*2*np.pi*normDistance*np.sin(thetas)
        arrayFactors = np.exp(np.kron(np.arange(0, numAntennaElements), temp))
    else:# %default
        temp = -1j*2*np.pi*normDistance*np.cos(thetas)
        arrayFactors = np.exp(np.kron(np.arange(0, numAntennaElements), temp))
    #normalize
    arrayFactors = arrayFactors / np.sqrt(numAntennaElements)
    return arrayFactors, thetas

def ArraySteerToUPA(Nax, Nay, normDistanceX, normDistanceY, pointAzimuth, pointElevation):
    betax = -2*np.pi*normDistanceX*np.sin(pointElevation)*np.cos(pointAzimuth)
    betay = -2*np.pi*normDistanceY*np.sin(pointElevation)*np.sin(pointAzimuth)

    ax = 1/np.sqrt(Nax)*np.exp(1j*np.range(0, Nax-1)*betax)
    ay = 1/np.sqrt(Nay)*np.exp(1j*np.range(0, Nay-1)*betay)

    A = np.kron(ax, ay)
    return A