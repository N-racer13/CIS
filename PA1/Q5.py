import numpy as np
import Carthesian_math_package
import Q2
import Q3
import Q4
import Loadfile 

#input:
#       EM_data (3xNxM): the N points in the EM space for M frames
#output:
#       1) P (3x1): the coordinates of the dimple in the local device space
#       2) t (3x1): the coordinates of the dimple in the EM space
#We essentially use the same code as in Q2 only here the calibration points in the local
#device space are calculated as the 'error' of every vector G in the first frame.
#Using least-squares for every callibration frame like in class gives the dimple position
#in both EM space and local device space.

def EM_pivot(EM_data):
    #load data
    G = Loadfile.loadEMPivot(EM_data)
    #calculate 'error to midpoint' point cloud
    g = Carthesian_math_package.center_point(G[:, :,0])
    #use previously defined calibration script
    P, t = Q3.pivot(g, G)
    return P, t