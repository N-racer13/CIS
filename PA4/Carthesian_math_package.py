import numpy as np

def Rotation(v, R):
    return np.dot(R, v)

def transform(R, p, v):
    return Rotation(v, R) + np.reshape(p, (3, 1))

def invert_transformation(R, p):
    R_inv = np.linalg.inv(R)
    p_inv = -np.dot(R_inv, p)
    return R_inv, p_inv

def center_point(cloud):
    #point cloud is 3xN matrix, first row is X-component of every point, second row Y,third Z
    centroid = np.mean(cloud, axis=1)
    updated_cloud = cloud - np.reshape(centroid,(3, 1))
    return updated_cloud

def quaternion_to_matrix(q):
    M = np.zeros([3, 3])
    M[0][0] = q[0]**2 + q[1]**2 - q[2]**2 - q[3]**2
    M[0][1] = 2*(q[1]*q[2] - q[0]*q[3])
    M[0][2] = 2*(q[1]*q[3] + q[0]*q[2])
    M[1][0] = 2*(q[1]*q[2] + q[0]*q[3])
    M[1][1] = q[0]**2 - q[1]**2 + q[2]**2 - q[3]**2
    M[1][2] = 2*(q[2]*q[3] - q[0]*q[1])
    M[2][0] = 2*(q[1]*q[3] - q[0]*q[2])
    M[2][1] = 2*(q[2]*q[3] + q[0]*q[1])
    M[2][2] = q[0]**2 - q[1]**2 - q[2]**2 + q[3]**2
    return M

def sort_by_longest_edge(v1, v2, v3):
    d12 = np.linalg.norm(v2-v1)
    d23 = np.linalg.norm(v3-v2)
    d31 = np.linalg.norm(v1-v3)
    longest = max(d12, d23, d31)
    if longest == d12:
        return v1, v2, v3
    elif longest == d23:
        return v2, v3, v1
    else:  # longest == d31
        return v3, v1, v2

