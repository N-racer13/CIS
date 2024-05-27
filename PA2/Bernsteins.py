#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
import numpy as np


# In[3]:


def bernsteinpoly(N,k,v):
    """
    Calculates a Bernstein polynomial coefficecnt as defined in class slides 
    """
    return float(math.comb(N,k))*((1-v)**(N-k))*(v**k)


# In[12]:


def fifthbernstein(v):
    """
    Creates a 5th order bernstein polynomial and then creates a tensor from this based on the methods in class slides 
    """
    vx = v[0]
    vy = v[1]
    vz = v[2]
    bernstein_x = []
    bernstein_y = []
    bernstein_z = []

    for i in range(6):
        bernstein_x.append(bernsteinpoly(6,i,vx))
        bernstein_y.append(bernsteinpoly(6,i,vy))
        bernstein_z.append(bernsteinpoly(6,i,vz))
    index = 0
    tensor = np.zeros((1,216))
    for i in range(6):
        for j in range(6):
            for k in range(6):
                tensor[0,index] = bernstein_x[i]*bernstein_y[j]*bernstein_z[k]
                index+=1
    return tensor


# In[6]:


#bernsteinpoly(5,1,2)


# In[13]:


#fifthbernstein([4,4,2])


# In[ ]:




