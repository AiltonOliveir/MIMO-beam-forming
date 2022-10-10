import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def spherical_plot(r,THETA,PHI):
    #theta = linspace(theta_low,theta_up,disc);
    #phi   = linspace(phi_low,phi_up,disc);

    #[THETA,PHI] = meshgrid(theta,phi);

    useOriginalPatches = 1

    fig = plt.figure()
    ax = Axes3D(fig)#fig.add_subplot(111, projection='3d')#ax = fig.gca(projection='3d')

    # spherical to rectangular conversion
    x = np.absolute(r)*np.sin(THETA)*np.cos(PHI)
    y = np.absolute(r)*np.sin(THETA)*np.sin(PHI)
    z = np.absolute(r)*np.cos(THETA)

    disc = z.shape[0]#size(z,1);

    # do the plot
    #figure; 
    surf = ax.plot_surface(x, y, z, linewidth=0, antialiased=False)#surf(x,y,z); view(135,20);
    if useOriginalPatches == 1:
        C = np.array([.8, .8, .8])# colormap(C);

    '''ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)'''
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    #plt.title('Wine Alcohol Content - Fixed Acidity - Residual Sugar', y=1.05)
    #axis off equal;

    # Draw x, y, and z axes
    '''set(line([1e-8;max(max(x))+3],[1e-8;1e-8],[1e-8;1e-8]),'Color','r');
    set(line([1e-8;1e-8],[1e-8;max(max(y))+3],[1e-8;1e-8]),'Color','r');
    set(line([1e-8;1e-8],[1e-8;1e-8],[1e-8;max(max(z))+3]),'Color','r');'''

    # Label x, y, and z axes
    '''text(max(max(x))+4,0,0,'x','FontSize',14,'FontName','Times','FontAngle','italic','Color','r');
    text(0,max(max(y))+4,0,'y','FontSize',14,'FontName','Times','FontAngle','italic','Color','r');
    text(0,0,max(max(z))+4,'z','FontSize',14,'FontName','Times','FontAngle','italic','Color','r');'''

    if useOriginalPatches == 1:
        # Fill surface using patches
        patch_1 = np.zeros((3, disc+1))
        patch_2 = np.zeros((3, disc+1))
        patch_1[0,0:disc] = x[0,:]
        patch_2[0,0:disc] = x[disc-1,:]
        patch_1[1,0:disc] = y[0,:]
        patch_2[1,0:disc] = y[disc-1,:]
        patch_1[2,0:disc] = z[0,:]
        patch_2[2,0:disc] = z[disc-1,:]
        '''patch(patch_1(1,:),patch_1(2,:),patch_1(3,:),C);
        patch(patch_2(1,:),patch_2(2,:),patch_2(3,:),C);'''
    plt.show()