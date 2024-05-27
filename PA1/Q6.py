import Carthesian_math_package
import Q2
import Q3
import Q4
import Q5
import Loadfile 
import numpy as np

#input:
#       1) opt_pivot_file: contains optical markers on dimple (H) and EM (D) in optical tracker space
#       2) body file: contains optical markers on EM in EM space
#output:
#       1) P (3x1): the coordinates of the dimple in the local device space
#       2) t (3x1): the coordinates of the dimple in the EM space
#Same exercise as Q5 but this time we start from the EM space. The EM tracker can not see
#the optical tracker but the optical one can see the EM. Therefore, we can use the inverse
#transformation of Fd which is known.

def Optical_EM_pivot(opt_pivot_file, body_file):
    #load data
    d = Loadfile.loadCalbody(body_file)[0]
    D, H = Loadfile.loadOptpivot(opt_pivot_file)
    #create empty frame set
    FdH = np.zeros(H.shape)
    for i in range(D.shape[2]):
        #create transformation matrix
        RD, pD = Q2.Registration(d, D[:, :, i])
        #calculate inverse transformation
        RD_inv = np.linalg.inv(RD)
        pD_inv = -np.dot(np.linalg.inv(RD), pD)
        #calculate new frameset
        FdH[:, :, i] = Carthesian_math_package.Transformation(H[:, :, i],RD_inv, pD_inv)
    G = FdH; 
    #calculate 'error to midpoint' point cloud
    g = Carthesian_math_package.center_point(G[:, :,0])
    #use previously defined calibration script
    t, P = Q3.pivot(g, G)
    return P