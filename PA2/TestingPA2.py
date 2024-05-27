#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Interpolation as interpolate 
import numpy as np
import Q4_mod as Q4
import LoadfilePA2
import PA2


# In[2]:


def testdistortioncorrectionfunc():
    """
    Test distortion by creating a random 3D matrix; adding some noise to create a distorted matrix; comparing the error between the matrices before and after distortion correction algorithm 
    """
    for i in range(10):
        Cundistorted = np.random.rand(3,20,10)*10
        noise = np.random.normal(0.0, np.random.rand(1)[0]*3, (3,20))
        Cdistorted = np.array(Cundistorted)
        for i in range(Cundistorted.shape[2]):
            Cdistorted[:,:,i] += noise
        coeffs, maxs, mins = interpolate.interpcoefficients(Cundistorted, Cdistorted)
        pre_distortion_error = np.zeros(Cundistorted.shape[:2])
        error = np.zeros(Cdistorted.shape[:2])
        for j in range(Cdistorted.shape[2]):
            slice_test = j
            undistorted = interpolate.undistortmatrix(coeffs, maxs, mins, Cdistorted[:,:,slice_test])
            pre_distortion_error += np.abs(Cundistorted[:,:,slice_test]-Cdistorted[:,:,slice_test])
            error += np.abs(Cundistorted[:,:,slice_test]-undistorted)
        print("Pre-distortion error: " + str(np.mean(pre_distortion_error)/Cundistorted.shape[2]))
        print("Post-distortion error: " + str(np.mean(error)/Cundistorted.shape[2])+"\n")


# In[3]:


testdistortioncorrectionfunc()


# In[4]:


def testdistortiondebugdatasets():
    """
    Test distortion similar to above but with datasets give to us instead of random ones
    """
    testchars = ['a','b','c','d','e','f']
    path = "data/pa2-debug-"
    calbodysuffix = "-calbody.txt"
    calreadingssuffix = "-calreadings.txt"
    for i in range(len(testchars)):
        slice_test = 0
        calbodyFile = path+testchars[i]+calbodysuffix
        calreadingsFile = path+testchars[i]+calreadingssuffix
        Cdistorted,Ctruth = Q4.distortion_calibration(calbodyFile, calreadingsFile)
        coeffs, maxs, mins = interpolate.interpcoefficients(Ctruth, Cdistorted)
        pre_distortion_error = np.zeros(Ctruth.shape[:2])
        error = np.zeros(Cdistorted.shape[:2])
        for j in range(Ctruth.shape[2]):
            slice_test = j
            undistorted = interpolate.undistortmatrix(coeffs, maxs, mins, Cdistorted[:,:,slice_test])
            pre_distortion_error += np.abs(Ctruth[:,:,slice_test]-Cdistorted[:,:,slice_test])
            error += np.abs(Ctruth[:,:,slice_test]-undistorted)
        print("Testing debug dataset: " + testchars[i])
        print("Pre-distortion error: " + str(np.mean(pre_distortion_error)/Ctruth.shape[2]))
        print("Post-distortion error: " + str(np.mean(error)/Ctruth.shape[2])+"\n")


# In[5]:


testdistortiondebugdatasets()


# In[10]:


def testprocedure():
    """
    Test the output from the main script against given output and print the errors for each data set 
    """
    test_chars = ['a', 'b', 'c', 'd', 'e', 'f']
    path = "data/pa2-debug-"
    for char in test_chars:
        ground_truth = LoadfilePA2.loadOutput2(path+char+"-output2.txt")
        output=PA2.runscript(path,char)
        #print(output)
        #print(ground_truth)
        print("Average error in dataset " + char + ": " + str(np.mean(np.abs(ground_truth-output))))


# In[11]:


testprocedure()


# In[12]:


def main():
    testdistortioncorrectionfunc()
    testdistortiondebugdatasets()
    testprocedure()
    return


# In[13]:


if __name__ == '__main__':
    main()


# In[ ]:




