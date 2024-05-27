import numpy as np

def Rotation(v, R):
    return np.dot(R, v)

def Transformation(v, R, p):
    return Rotation(v, R) + p

def Inverse_transformation(v, R, p):
    return Rotation(v, np.linalg.inv(R)) - Rotation(p, np.linalg.inv(R))

#rot = np.array([[1, -1, 0], [0, 1, 0],[0, 0, 1]])
#tran = np.array([0, 0, 1])
#inp = np.array([1, 2, 3])
#print(np.linalg.inv(rot))
#print(Inverse_transformation(inp, rot, tran))

def center_point(cloud):
    #point cloud is 3xN matrix, first row is X-component ofevery point, second row Y,thirs Z
    centroid = np.mean(cloud, axis=1)
    updated_cloud = cloud - np.reshape(centroid,(3, 1))
    return updated_cloud

#cloud = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
#print(np.shape(cloud))
#print(center_point(cloud))
