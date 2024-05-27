#!/usr/bin/env python
# coding: utf-8

# In[17]:


import LoadfilePA2 as Loadfile 
import Interpolation as interpolate 
import Q2
import Carthesian_math_package
import numpy as np


# In[12]:


def getcoordtransformations(Gframes, gvecs):
    """
    Finds the transformation between a center frame and the other frames
    """
    Rlist = []
    plist = []
    for f in range(Gframes.shape[2]):
        R, p = Q2.Registration(gvecs, Gframes[:, :, f])
        Rlist.append(R)
        plist.append(p)
    return Rlist, plist


# In[13]:


def gettiplocations(emfiducialsdata, tg, gvecs):
    """
    Calculates the transformation of the tip of the fiducial relative to each frame in the EM space
    """
    Rlist, plist = getcoordtransformations(emfiducialsdata, gvecs)
    fiducials = np.zeros((3, emfiducialsdata.shape[2]))
    for i in range(len(plist)):
        fiducials[:, i] = Carthesian_math_package.Transformation(np.reshape(tg, (3,1)),Rlist[i], plist[i]).ravel()
    return fiducials


# In[14]:


def computetrackerfiducials(emfiducialsfile, tg, gvecs, coeffs, maxs, mins):
     """
       Undistorts the EM fiducial data and calculates the locations of fiducials 
    """
    EMFiducials=Loadfile.loadEMFiducial(emfiducialsfile)
    emfiducialsdata = interpolate.undistortframes(coeffs, maxs, mins,EMFiducials)
    fiducials=gettiplocations(emfiducialsdata, tg, gvecs)
    return fiducials


# In[15]:


def calculateFreg(ctfiducialsfile, emfiducials):
    """
    Calculates transformation between em and ct space
    """
    ctfiducials = Loadfile.loadCTFiducial(ctfiducialsfile)
    return Q2.Registration(emfiducials,ctfiducials)


# In[16]:


def findnavctpoints(emnavfile, tg, gvecs, Rreg, preg, coeffs, maxs, mins):
    """
    Undistorts the CT fiducial data and calculates the locations of fiducials in CT space   
    """
    EMNav=Loadfile.loadEMNav(emnavfile)
    emnavdata = interpolate.undistortframes(coeffs, maxs, mins,EMNav)
    locations=gettiplocations(emnavdata, tg, gvecs)
    return Carthesian_math_package.Transformation(locations, Rreg, preg)


# In[ ]:





# In[ ]:




