#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import Bernsteins


# In[19]:


def interpcoefficients(truth, distorted):
    """
    Flatten matrix and then set up a system of least squares using bernsteins polynomials to calculate the correction coefficients
    """
    if len(truth.shape) == 3:
        truthc = np.zeros((3, truth.shape[1]*truth.shape[2]))
        distortedc = np.zeros((3, distorted.shape[1]*distorted.shape[2]))
        for i in range(distorted.shape[2]):
            truthc[:,i*truth.shape[1]:(i+1)*truth.shape[1]] = truth[:,:,i]
            distortedc[:,i*distorted.shape[1]:(i+1)*distorted.shape[1]] = distorted[:,:,i]
    else:
        truthc = truth
        distortedc = distorted
    b = truthc.T
    A = np.empty([distortedc.shape[1], 216])
    maxs = np.reshape(np.max(distortedc, axis = 1)*3, (3,1)) #this is to ensure that our solution is bounded between 0 and 1 but does not equal 0 or 1
    mins = np.reshape(np.min(distortedc, axis = 1)*0.33, (3,1))
    distortedc = distortedc-mins
    distortedc = distortedc/(maxs-mins)
    for i in range(distortedc.shape[1]):
        v = distortedc[:,i]
        A[i,:] = Bernsteins.fifthbernstein(np.array(v))
    return np.linalg.lstsq(A,b)[0], maxs, mins


# In[7]:


def undistortvector(coeffs, maxs, mins, v):
    """
    Undistort a vector by creating a fifth order tensor and multiplying it by the coefficients set up above  
    """
    u = (v-mins)/(maxs-mins)
    tensor = Bernsteins.fifthbernstein(u)
    return np.sum(np.multiply(coeffs.T,tensor), axis = 1)


# In[8]:


def undistortmatrix(coeffs, maxs, mins, m):
    """
    Undistort a matrix by creating a fifth order tensor and multiplying it by the coefficients set up above  
    """
    undistorted = np.zeros(m.shape)
    for i in range(m.shape[1]):
        undistorted[:,i] = undistortvector(coeffs, maxs, mins, np.reshape(np.array(m[:,i]),(3,1)))
    return undistorted


# In[9]:


def undistortframes(coeffs, maxs, mins, f):
    """
    Undistort frames by creating a fifth order tensor and multiplying it by the coefficients set up above  
    """
    undistorted = np.zeros(f.shape)
    for i in range(f.shape[2]):
        undistorted[:,:,i] = undistortmatrix(coeffs, maxs, mins, np.array(f[:,:,i]))
    return undistorted


# In[ ]:




