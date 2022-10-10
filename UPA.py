import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.collections import PatchCollection
#import seaborn as sns

import ArrayPattern
import PointingPattern
import ArrayFactor
import spherical_plot

d=1
lambdac=2
normDistanceX=d/lambdac
normDistanceY=d/lambdac
N=90 #angle grid resolution

Nax=4 # Number of Tx antennas in x axis
Nay=4

if 0:
    azimuths = np.linspace(0,2*np.pi,N) #angles
    elevations = np.linspace(0,np.pi,N) #angles
    THETAele, PHIazi = np.meshgrid(elevations,azimuths)

## Test towards specific angle
pointAz=np.pi/2
pointEl=np.pi/4
upaArrayFactor, THETAele, PHIazi = PointingPattern.pointingPatternUPA(Nax, Nay, normDistanceX, normDistanceY, pointAz, pointEl, N)
spherical_plot.spherical_plot(np.absolute(upaArrayFactor),THETAele,PHIazi)