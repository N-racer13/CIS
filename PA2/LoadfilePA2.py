import os 
import numpy as np

def loadCalbody(filepath):
    """
    Loads in the data in files of the format NAME-CALBODY.TXT.
    Three 2-D matrices are produced, holding vectors d, a, c, respectively.
    Each matrix has 3 rows and N_d, N_a, N_c columns respectively.
    Each column corresponds to a vector, and each row corresponds to a dimension of the vectors.
    """

    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    datacalbody=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Nd=(firstline[0]);
    Na=(firstline[1]); 
    Nc=(firstline[2]);

    dmatrix=datacalbody[0:Nd]; 
    amatrix=datacalbody[Nd:Na+Nd];
    cmatrix=datacalbody[Na+Nd:Na+Nd+Nc];
    return dmatrix.T, amatrix.T, cmatrix.T 

def loadCalReadings(filepath):
    """
    Loads in the data in files of the format NAME-CALREADINGS.TXT.
    Three 3-D matrices are produced, holding vectors D, A, C, respectively.
    each matrix has 3 row, N_D, N_A, N_C columns, and N_frames height.
    Each row corresponds to a vector, each column corresponds to a physical dimension, each height  to a frame.
    """
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    datacalreading=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Nd=(firstline[0]);
    Na=(firstline[1]); 
    Nc=(firstline[2]);
    Nf=(firstline[3]);
    
    Dmatrix=np.zeros((3,Nd,Nf));
    Amatrix=np.zeros((3,Na,Nf));
    Cmatrix=np.zeros((3,Nc,Nf));
    
    for i in range(Nf):
        index=i*(Nd+Na+Nc);
        Dmatrix[:,:,i]=datacalreading[index:Nd+index].T;
        Amatrix[:,:,i]=datacalreading[Nd+index:Nd+Na+index].T; 
        Cmatrix[:,:,i]=datacalreading[Nd+Na+index:Nd+Na+Nc+index].T; 

    return Dmatrix, Amatrix, Cmatrix


def loadEMPivot(filepath):
    """
    Loads in the data in files of the format NAME-EMPIVOT.TXT.
    One 3-D matrix is produced, holding vectors G, respectively.
    each matrix has 3 columns, N_G rows, and N_frames height.
    Each row corresponds to a vector, each column corresponds to a physical dimension, each height  to a frame.
    """
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    dataempivot=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Ng=(firstline[0]);
    Nf=(firstline[1]); 
 
    Gmatrix=np.zeros((3,Ng,Nf));
    
    for i in range(Nf):
        index=i*(Ng);
        Gmatrix[:,:,i]=dataempivot[index:Ng+index].T;
    return Gmatrix

def loadOptpivot(filepath):
    """
    Loads in the data in files of the format NAME-OPTPIVOT.TXT.
    Two 3-D matrices are produced, holding vectors D and H respectively.
    each matrix has 3 columns, N_D, N_H rows, and N_frames height.
    Each row corresponds to a vector, each column corresponds to a physical dimension, each height  to a frame.
    """
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    dataempivot=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Nd=(firstline[0]);
    Nh=(firstline[1]); 
    Nf=(firstline[2]); 
    
    Dmatrix=np.zeros((3,Nd,Nf));
    Hmatrix=np.zeros((3,Nh,Nf))
    

    for i in range(Nf):
        index=i*(Nd+Nh);
        Dmatrix[:,:,i]=dataempivot[index:Nd+index].T;
        Hmatrix[:,:,i]=dataempivot[Nd+index:Nd+Nh+index].T;
    return Dmatrix,Hmatrix


def loadOutput1(filepath):
    """
    Loads in the data in files of the format NAME-OUTPUT-1.TXT.
    Three 3-D matrices are produced, holding vectors D and H respectively.
    each matrix has 3 columns, N_D, N_H rows, and N_frames height.
    Each row corresponds to a vector, each column corresponds to a physical dimension, each height  to a frame.
    """
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    Pem=np.double(np.genfromtxt(filepath,skip_header=1,max_rows=1,delimiter=","));
    Pom=np.double(np.genfromtxt(filepath,skip_header=2,max_rows=1,delimiter=","));
    dataoutput=np.double(np.genfromtxt(filepath,skip_header=3,delimiter=","));
    Nc=(firstline[0]);
    Nf=(firstline[1]); 


    Cmatrix=np.zeros((3,Nc,Nf));

    for i in range(Nf):
        index=i*(Nc);
        Cmatrix[:,:,i]=dataoutput[index:Nc+index].T;
    return Cmatrix,Pem,Pom,
      


def writeOutput1(filepath, ECMatrix, EMprobepos, optprobepos):
   
    outFile = open(filepath, 'w')
    outFile.write(str(ECMatrix.shape[1]) + ",\t" + str(ECMatrix.shape[2]) + ",\t" + filePath + "\n")
    outFile.write("\t%.2f,\t%.2f,\t%.2f\n" % (EMprobepos.ravel()[0],
                             EM_probe_pos.ravel()[1], EMprobepos.ravel()[2]))
    outFile.write("\t%.2f,\t%.2f,\t%.2f\n" % (optprobepos.ravel()[0],
                             optprobepos.ravel()[1], optprobepos.ravel()[2]))
    for k in range(ECMatrix.shape[2]):
        for i in range(ECMatrix.shape[1]):
            vec = ECMatrix[:,i,k]
            outFile.write("\t%.2f,\t%.2f,\t%.2f\n" % (vec[0], vec[1], vec[2]))
    outFile.close()

def loadOutput2(filepath):
    """
    Loads in the data in files of the format NAME-OUTPUT-2.TXT.
    A 3xNf numpy matrix that contains probe tip locations in CT coordinate system.
    """
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    dataoutput=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Nf=(firstline[0]); 
    CTprobe= np.zeros((3,Nf))
    for i in range(Nf):
        CTprobe[:,i]=dataoutput[i,:].T;
    return CTprobe

def writeOutput2(filePath, ctpoints):
    """
    Writes the output file given the results for expected C_Matrix EM- and optical pivot calibration.
    This is the output that corresponds to assignment 1.
    :param filePath: path to file to be saved
    :param ct_nav_points: 3xF numpy array, where N is the number of points and F the number of frames
    """
    outFile = open(filePath, 'w')
    outFile.write(str(ctpoints.shape[1]) + ",\t" + filePath + "\n")
    for i in range(ctpoints.shape[1]):
        vec = ctpoints[:,i]
        outFile.write("\t%.2f,\t%.2f,\t%.2f\n" % (vec[0], vec[1], vec[2]))
    outFile.close()

def loadEMNav(filepath):
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    dataemnav=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Ng=(firstline[0]);
    Nf=(firstline[1]); 
 
    GEMmatrix=np.zeros((3,Ng,Nf));
    
    for i in range(Nf):
        index=i*(Ng);
        GEMmatrix[:,:,i]=dataemnav[index:Ng+index].T;
    return GEMmatrix

def loadEMFiducial(filepath):
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    dataemfid=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Ng=(firstline[0]);
    Nf=(firstline[1]); 
 
    Gfidmatrix=np.zeros((3,Ng,Nf));
    
    for i in range(Nf):
        index=i*(Ng);
        Gfidmatrix[:,:,i]=dataemfid[index:Ng+index].T;
    return Gfidmatrix

def loadCTFiducial(filepath):
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int); 
    dataCTfid=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Nb=(firstline[0]);
 
    CTfid=np.zeros((3,Nb));
    
    for i in range(Nb):
        CTfid[:,i]=dataCTfid[i,:].T;
    return CTfid


