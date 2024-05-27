import numpy as np
import Carthesian_math_package
import Q2
import Q3
import Loadfile

#input:
#      1) body file: contains optical markers on EM in EM space 
#      2) readings_file: contains optical markers on EMand calibration object in optical space
#output:
#      C_expected (3xNxM): N expected C vectors for every frame M 
#Instead of using the C vectors measured in the EM frame, we can transform the
#optical c markers to the optical space and then transform them to the EM space
#using the inverse transformation of Fd.

def distortion_calibration(body_file, readings_file):
    #load data
    d, a, c = Loadfile.loadCalbody(body_file)
    D, A = Loadfile.loadCalReadings(readings_file)[:2]
    #create empty C expected
    C_expected = np.zeros((3, c.shape[1], D.shape[2]))
    for i in range(D.shape[2]):
        #create transformation matrices
        RD, pD = Q2.Registration(d, D[:, :, i])
        RA, pA = Q2.Registration(a, A[:, :, i])
        #calculate inverse transformation
        RD_inv = np.linalg.inv(RD)
        pD_inv = -np.dot(np.linalg.inv(RD), pD)
        #calculate Fc
        RC = np.dot(RD_inv, RA)
        pC = np.dot(RD_inv, pA) + pD_inv
        #calculate C expected
        C_expected[:, :, i] = np.dot(RC, c) + pC

    return C_expected