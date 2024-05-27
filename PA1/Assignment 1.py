#!/usr/bin/env python
# coding: utf-8

# In[3]:


import Carthesian_math_package

import Q2

import Q4

import Q5

import Q6

import Loadfile

from math import cos
from math import sin
from math import pi
from math import sqrt
import numpy as np
import os


# In[9]:


def main():
    """
    Runs the program on "unknown" input identified by character given as argument.
    Writes equivalent output file and prints results.
    """
    np.set_printoptions(precision=2, suppress=True)
    char = input('Enter letter of unknown file');

    path = "data/pa1-unknown-"
    calbodyFile = path+char+"-calbody.txt"
    calreadingsFile = path+char+"-calreadings.txt"
    EMPivotFile = path+char+"-empivot.txt"
    optPivotFile = path+char+"-optpivot.txt"
    outputFile = path+char+"-output1.txt"
    
    Cexp = Q4.distortion_calibration(calbodyFile, calreadingsFile)
    print("expected values for C:")
    print(Cexp)
    EMprobe = Q5.EM_pivot(EMPivotFile)[1].T
    print("Location of dimple using EM tracker:")
    print(EMprobe)
    optprobe = Q6.Optical_EM_pivot(optPivotFile, calbodyFile).T
    print("Location of dimple using optical tracker:")
    print(optprobe)
    Loadfile.writeOutput1(outputFile, Cexp,  EMprobe, optprobe)
    print("Writing output to " + outputFile)
    return


if __name__ == '__main__':
    main()


# In[ ]:




