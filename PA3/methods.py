import numpy as np
import Carthesian_math_package


def CreateSphere(v1, v2, v3):
    #input:
    #       1) Vec1 (3x1): vertex 1 of the triangle
    #       2) Vec2 (3x1): vertex 2 of the triangle
    #       3) Vec3 (3x1): vertex 3 of the triangle

    a, b, c = Carthesian_math_package.sort_by_longest_edge(v1.ravel(), v2.ravel(), v3.ravel())
    f = (a + b)/2.0
    u = a - f
    v = c - f
    d = np.cross(np.cross(u, v), u)
    gamma = float((np.dot(v, v) - np.dot(u, u))/np.dot(2*d, (v-u)))
    lam = max(gamma, 0.0)
    center = f + lam*d
    radius = np.linalg.norm(center - a)
    return np.reshape(center, (3, 1)), radius



def ClosestPointTriangle(Vec1, Vec2, Vec3, point):
    #input:
    #       1) Vec1 (3x1): vertex 1 of the triangle
    #       2) Vec2 (3x1): vertex 2 of the triangle
    #       3) Vec3 (3x1): vertex 3 of the triangle
    #       4) point (3x1): point we want to know the closest point to be on the triangle
    #output:
    #       1) closest (3x1): closest point on the triangle to point
    #Find the closest point on a triangle by setting up a least squares problem while
    #making sure the solution falls within the right boundary.

    a = point-Vec1
    mat = np.hstack((np.reshape(Vec2-Vec1, (3, 1)), np.reshape(Vec3-Vec1, (3, 1))))
    lambd, mu = np.linalg.lstsq(mat, a)[0].reshape(-1)
    closest = Vec1 + lambd*(Vec2-Vec1) + mu*(Vec3-Vec1)
    if lambd < 0:
        l = max(0.0, min(1.0, float(np.dot((closest-Vec3).reshape(-1), (Vec1-Vec3).reshape(-1))/np.dot((Vec1-Vec3).reshape(-1), (Vec1-Vec3).reshape(-1)))))
        closest = Vec3 + l*(Vec1-Vec3)
    if mu < 0:
        l = max(0.0, min(1.0, float(np.dot((closest-Vec1).reshape(-1), (Vec2-Vec1).reshape(-1))/np.dot((Vec2-Vec1).reshape(-1), (Vec2-Vec1).reshape(-1)))))
        closest = Vec1 + l*(Vec2-Vec1)
    if lambd + mu > 1:
        l = max(0.0, min(1.0, float(np.dot((closest-Vec2).reshape(-1), (Vec3-Vec2).reshape(-1))/np.dot((Vec3-Vec2).reshape(-1), (Vec3-Vec2).reshape(-1)))))
        closest = Vec2 + l*(Vec3-Vec2)
    return closest

def ClosestPointLinearSearch(triangles, Vec, point):
    #input:
    #       1) triangle (3xN): list of points in space representing the vertices   
    #       2) Vec (3xM): list of indices of the vertices of a triangle
    #       3) point (3x1): point we want to know the closest point to be on the triangle
    #output:
    #       1) closest (3x1): closest point on the triangle to point
    #Look for closest point on the mesh using linear search
    closest = None
    min_distance = float("inf")
    for i in range(triangles.shape[1]):
        triangle = triangles[:, i]
        Vec1 = np.reshape(Vec[:, triangle[0]], (3, 1))
        Vec2 = np.reshape(Vec[:, triangle[1]], (3, 1))
        Vec3 = np.reshape(Vec[:, triangle[2]], (3, 1))
        c = ClosestPointTriangle(Vec1, Vec2, Vec3, point)
        distance = np.linalg.norm(c-point)
        if distance < min_distance:
            min_distance = distance
            closest = c
    return closest

def ClosestPointMeshBoundingSpheres(triangles, Vec, point):
    #input:
    #       1) triangle (3xN): list of points in space representing the vertices    min_distance = float("inf")
    #       2) Vec (3xM): list of indices of the vertices of a triangle
    #       3) point (3x1): point we want to know the closest point to be on the triangle
    #output:
    #       1) closest (3x1): closest point on the triangle to point
    #Look for closest point on the mesh using bounding spheres

    min_distance = float("inf")
    closest = None
    for i in range(triangles.shape[1]):
        triangle = triangles[:, i]
        Vec1 = np.reshape(Vec[:, triangle[0]], (3, 1))
        Vec2 = np.reshape(Vec[:, triangle[1]], (3, 1))
        Vec3 = np.reshape(Vec[:, triangle[2]], (3, 1))
        center, radius = CreateSphere(Vec1, Vec2, Vec3)
        if np.linalg.norm(point-center) - radius < min_distance:
            c = ClosestPointTriangle(Vec1, Vec2, Vec3, point)
            distance = np.linalg.norm(c-point)
            if distance < min_distance:
                min_distance = distance
                closest = c
    return closest

def BuildOctree(Vec, triangles):
    #input:
    #       1) Vec (3xN): list of indices of the vertices of a triangle
    #       2) triangle (3xM): list of points in space representing the vertices
    #output:
    #       1) object of the class BoundingBoxTreeNode: root of the octree
    #Create octree using the spheres around each triangle of the mesh

    spheres = []
    for i in range(triangles.shape[1]):
        triangle = triangles[:, i]
        Vec1 = np.reshape(Vec[:, triangle[0]], (3, 1))
        Vec2 = np.reshape(Vec[:, triangle[1]], (3, 1))
        Vec3 = np.reshape(Vec[:, triangle[2]], (3, 1))
        sphere = octree.Sphere(Vec1, Vec2, Vec3)
        spheres.append(sphere)
    return octree.BoundingBoxTreeNode(spheres)

def ClosestPointOctree(tree, point):
    #Gives the closest point in a mesh using an octree optimization algorithm.    
    
    return tree.FindClosestPoint(point, float("inf"), None)[1]