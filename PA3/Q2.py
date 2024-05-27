import numpy as np
import Carthesian_math_package

#input:
#       1) c1 (3xN): point cloud 1
#       2) c2 (3xN): point cloud 2
#output:
#       1) R (3x3): Rotation matrix of the transformationbetween the 2 clouds
#       2) p (3x1): translation vector of the transformationbetween the 2 clouds
#Using Horn's algorithm we can find the transformation matrix that maps one point cloud to another.
def Registration(c1, c2):
    H = np.zeros((3,3))
    c_c1 = Carthesian_math_package.center_point(c1)
    c_c2 = Carthesian_math_package.center_point(c2)
    for i in range(c_c1.shape[1]):
        a = c_c1[:, i]
        b = c_c2[:, i]
        #numpy tool to create H matrix as defined in class
        H += np.outer(a,b)
    #create Delta from Horn's algorithm
    Delta = np.array([H[1, 2] - H[2,1], H[2, 0] - H[0, 2], H[0, 1] - H[1, 0]])
    #create G matrix drom Horn's algorithm
    G = np.zeros((4, 4))
    G[0,0] = np.trace(H)
    G[0, 1:4] = np.transpose(Delta)
    G[1:4, 0] = Delta
    G[1:4, 1:4] = H + np.transpose(H) - np.trace(H)*np.eye(3)
    #eigenvalues and vectors (respectively) fromG matrix
    l, x = np.linalg.eig(G)
    #largest eigenvalue eigenvector is selected
    q = x[:, np.argmax(l)]
    #convert q to Rotation matrix R
    R = np.zeros([3, 3])
    R[0][0] = q[0]**2 + q[1]**2 - q[2]**2 - q[3]**2
    R[0][1] = 2*(q[1]*q[2] - q[0]*q[3])
    R[0][2] = 2*(q[1]*q[3] + q[0]*q[2])
    R[1][0] = 2*(q[1]*q[2] + q[0]*q[3])
    R[1][1] = q[0]**2 - q[1]**2 + q[2]**2 - q[3]**2
    R[1][2] = 2*(q[2]*q[3] - q[0]*q[1])
    R[2][0] = 2*(q[1]*q[3] - q[0]*q[2])
    R[2][1] = 2*(q[2]*q[3] + q[0]*q[1])
    R[2][2] = q[0]**2 - q[1]**2 - q[2]**2 + q[3]**2
    #compute translation component p
    Rc1 = Carthesian_math_package.Rotation(c1, R)
    p = c2 - Rc1
    p_average = np.mean(p, axis=1)
    p_final = np.reshape(p_average,(3, 1))
    return R, p_final

a = np.array([[1,2,3,4], [4,6,2,1], [4,9,3,5]])
b = np.array([[5,2,3,4], [6,6,2,1], [6,9,3,5]])
p = Registration(a,b)[1]
print(Registration(a,b))
print(p.shape)