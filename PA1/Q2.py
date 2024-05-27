import numpy as np
import Carthesian_math_package

def Registration(c1, c2):
    H = np.zeros((3,3))
    c_c1 = Carthesian_math_package.center_point(c1)
    c_c2 = Carthesian_math_package.center_point(c2)
    for i in range(c_c1.shape[1]):
        a = c_c1[:, i]
        b = c_c2[:, i]
        H += np.outer(a,b)
    Delta = np.array([H[1, 2] - H[2,1], H[2, 0] - H[0, 2], H[0, 1] - H[1, 0]])
    G = np.zeros((4, 4))
    G[0,0] = np.trace(H)
    G[0, 1:4] = np.transpose(Delta)
    G[1:4, 0] = Delta
    G[1:4, 1:4] = H + np.transpose(H) - np.trace(H)*np.eye(3)
    l, x = np.linalg.eig(G)
    q = x[:, np.argmax(l)]
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
    Rc1 = Carthesian_math_package.Rotation(c1, R)
    p = c2 - Rc1
    p_average = np.mean(p, axis=1)
    p_average= np.reshape(p_average,(3,1)); 
    return R, p_average

#a = np.array([[1,2,3,4], [4,6,2,1], [4,9,3,5]])
#print(a.shape)
#b = np.array([[5,2,3,4], [6,6,2,1], [6,9,3,5]])
#Registration(a,b)
