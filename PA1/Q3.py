import numpy as np
import Carthesian_math_package
import Q2

#input:
#       local_points (3xN): N different points in the local device space
#       frames (3xNxM): N different calibration points in base frame for M frames
#output:
#       1) the pivot point in the local device frame
#       2) the pivot point in base frame
#The local_points helpus define a local device system for which we then compute the
#transformation to in every frame. This then boils down to a least-squares problem
#as seen in class. Numpy has the necessary tools to easily solve this.
def pivot(local_points, frames):
    #load data
    A = np.zeros([frames.shape[2]*3, 6])
    b = np.zeros([frames.shape[2]*3, 1])
    for i in range(frames.shape[2]):
        #calculate transformation matrix
        R, p = Q2.Registration(local_points, frames[:, :, i])
        #setup least-squares form as Ax=b
        A[i*3:i*3+3,0:3] = R
        A[i*3:i*3+3,3:6] = -1*np.eye(3)
        b[i*3:i*3+3] = -1*p
    #calculate x using least-squares
    x = np.linalg.lstsq(A,b)[0]
    return x[0:3], x[3:6]

#G = np.array([[[1,2,3],[4,6,5],[5,9,3]],[[5,2,8],[2,9,6],[9,2,6]],[[5,2,8],[2,9,6],[9,2,6]]])
#print(pivot(G))