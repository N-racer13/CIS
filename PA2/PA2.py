#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import Q4_mod as Q4
import LoadfilePA2
import Interpolation
import Q5_mod as Q5
import Fiducials


# In[5]:


def runscript(path,char):
    """
    Main script; commented below 
    """
    calbodyFile = path+char+"-calbody.txt"
    calreadingsFile = path+char+"-calreadings.txt"
    EMPivotFile = path+char+"-empivot.txt"
    optPivotFile = path+char+"-optpivot.txt"
    emFiducialsFile=path+char+"-em-fiducialss.txt"
    ctFiducialsFile=path+char+"-ct-fiducials.txt"
    emNavFile=path+char+"-EM-nav.txt"

    Cexpect,C = Q4.distortion_calibration(calbodyFile, calreadingsFile)

    # Procedure part 2 interpolation coefficients using bernsteins polynomials 
    coeffs, maxs, mins = Interpolation.interpcoefficients(Cexpect, C)

    # Procedure part 3 do the pivot calibration with correction 
    tg,Pdimple,gvecs = Q5.EM_pivot(EMPivotFile, coeffs, maxs, mins)

    # Procedure part 4 compute the location of the tracker location relative to the EM space
    tracker_fiducials = Fiducials.computetrackerfiducials(emFiducialsFile, tg, gvecs, coeffs, maxs, mins)

    # Procedure part 5 compute the transformation between the EM and the CT space 
    R_reg, p_reg = Fiducials.calculateFreg(ctFiducialsFile, tracker_fiducials)

    # Procedure part 6 use the previous transformation to compute the location corrections within the CT space
    ct_nav_points = Fiducials.findnavctpoints(emNavFile, tg, gvecs, R_reg, p_reg, coeffs, maxs, mins)
    return ct_nav_points


# In[3]:


def main():
    char=input('What dataset do you want to test: ')
    path= "data/pa2-unknown-"
    output=runscript(path,char); 
    path2 = "output/pa2-unknown-"
    outputFile = path2+char+"-output2.txt"
    LoadfilePA2.writeOutput2(outputFile, output)


# In[ ]:


if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




