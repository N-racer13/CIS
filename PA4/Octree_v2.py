#!/usr/bin/env python
# coding: utf-8

# In[10]:


import methods
import numpy as np
MIN_COUNT = 8


# In[9]:


a=np.array([1,2,1]).T
b=np.array([1,3,1]).T
c=np.array([1,3,2]).T


# In[2]:


class Sphere:
    # Class for object sphere holding a triangle with following members:
    # v1, v2, v3 (3x1): triangle vertices
    # center (3x1): sphere center
    # radius (float): sphere radius

    def __init__(self, v1, v2, v3):
        # Create sphere object, initiates the vertices

        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        center, self.radius = methods.CreateSphere(self.v1, self.v2, self.v3)
        self.center = center.ravel()


# In[11]:


class BoundingBoxTreeNode:
    # Class for object node of the octree with following members:
    # spheres (Nx1): list of spheres in the node
    # ns (int): number of spheres in the node
    # center (3x1): average center of the spheres in the object
    # max_radius (float): radius of the biggest sphere in the node
    # LB (3x1): lower limit of the cube
    # UB (3x1): upper limit of the cube
    # has_subtrees (bool): if node has children
    # subtrees (8x1): contains children of the node

    def __init__(self, bounding_spheres):
        # create BoundingBoxTreeNode object, takeslist of sphere objects to be included in the node

        self.spheres = bounding_spheres
        self.nS = len(self.spheres)
        self.center, self.max_radius, self.LB, self.UB = self.get_properties()
        self.has_subtrees = self.nS > MIN_COUNT
        self.subtrees = [None] * 8
        if self.has_subtrees:
            self.construct_subtrees()
    
    def get_properties(self):
        # Compute properties of the node: center, radius, boundaries
        # returns center, max_radius, LB, UB properties

        if self.nS == 0:
            return None, 0, None, None
        center_mat = np.empty((3, len(self.spheres)))
        max_radius = 0
        for i in range(len(self.spheres)):
            sphere = self.spheres[i]
            center_mat[:, i] = sphere.center
            if sphere.radius > max_radius:
                max_radius = sphere.radius
        return np.mean(center_mat, axis=1), max_radius, np.min(center_mat, axis=1), np.max(center_mat, axis=1)

            
    def construct_subtrees(self):
        # creates subtrees of the node

        sphere_bins = self.split_sort()
        for i in range(8):
            self.subtrees[i] = BoundingBoxTreeNode(sphere_bins[i])
    def split_sort(self):
        # Splits list of spheres based on the location of the sphere relative to the average center
        # returns 8 list of spheres which specified sections containing the ordered spheres
        
        sphere_bins = list()
        for i in range(8):
            sphere_bins.append(list())
        for sphere in self.spheres:
            bin_num = 0
            center = sphere.center
            if center[0] < self.center[0]:
                bin_num += 1
            if center[1] < self.center[1]:
                bin_num += 2
            if center[2] < self.center[2]:
                bin_num += 4
            sphere_bins[bin_num].append(sphere)
        return sphere_bins
    def find_closest_point(self, v, bound, closest):
        # Finds the closest point to v, bound is closest distance so far, closest isclosest point so far
        # returns the updated bound and closest
        
        if self.nS == 0:
            return bound, closest
        dist = bound + self.max_radius
        #print(v)
        #print(bound)
        if (v[0] > (dist + self.UB[0]) or v[0] < self.LB[0] - dist or
                v[1] > dist + self.UB[1] or v[1] < self.LB[1] - dist or
                v[2] > dist + self.UB[2] or v[2] < self.LB[2] - dist):
            return bound, closest
        if self.has_subtrees:
            for subtree in self.subtrees:
                bound, closest = subtree.find_closest_point(v, bound, closest)
        else:
            for sphere in self.spheres:
                cp = methods.ClosestPointTriangle(sphere.v1, sphere.v2, sphere.v3, v)
                dist = np.linalg.norm(cp-v)
                if dist < bound:
                    bound = dist
                    closest = cp
        return bound, closest
    


# In[ ]:





# In[ ]:



        


# In[ ]:




