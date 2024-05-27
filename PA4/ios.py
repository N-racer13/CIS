#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[23]:


def loadbody(filepath):
    # Input:
    #       1) filepath: filepath to the body data
    # Output:
    #       1) bodymatrix: reformatted data of the body
    #       2) tip: reformatted data of the tip
    # Reformats the raw data

    data=np.double(np.genfromtxt(filepath,skip_header=1));
    bodymatrix = data[:data.shape[0]-1,:].T
    tip=data[data.shape[0]-1,:].T
    return bodymatrix, tip  


# In[93]:


def loadmesh(filepath):
    # Input:
    #       1) filepath: filepath to the mesh data
    # Output:
    #       1) vertices: extracts data of the xyz coordinqtes of the vertices
    #       2) triangles: extracts data of the indices of the vertices
    # Reformats the raw data

    numvert=np.genfromtxt(filepath,max_rows=1).astype(int); 
    vertices=np.double(np.genfromtxt(filepath,skip_header=1,max_rows=numvert)).T;
    numtriangles=np.double(np.genfromtxt(filepath,skip_header=1+numvert,max_rows=1));
    triangles=np.double(np.genfromtxt(filepath,skip_header=2+numvert,max_rows=numtriangles))
    triangles=triangles[:,:3].astype(int).T; 
   
    return vertices,triangles
    
    
    


# In[94]:


vertices, triangles = loadmesh('data/Problem3MeshFile.sur')
    
print('Number of vertices: ' + str(vertices.shape[1]))
print('First 10 vertices: ')
for i in range(10):
    print('Vertex: ' + str(i+1) + str(vertices[:, i]))
print('Last 10 vertices: ')
for i in range(1, 11):
    print('Backwards Index: ' + str(i) + str(vertices[:, -i]))
print(' ')

print('Number of triangles: ' + str(triangles.shape[1]))
print('First 10 triangles: ')
for i in range(0, 10):
    print('Triangle: ' + str(i+1) + str((triangles[:, i])))
print('Last 10 triangles: ')
for i in range(1, 11):
    print('Backwards Index: ' + str(i) + str(triangles[:, -i]))
print(' ')


# In[71]:


def loadsamplereadings(filepath, na, nb):
    # Input:
    #       1) filepath: filepath to the sample readings
    #       2) na: number of coordinates body A
    #       3) nb: number of coordinates body B
    # Output:
    #       1) amatrix: extracts data to create matrix A
    #       2) bmatrix: extracts data to create matrix B
    # Reformats the raw data 
    firstline=np.genfromtxt(filepath,max_rows=1,delimiter=",").astype(int);     
    data=np.double(np.genfromtxt(filepath,skip_header=1,delimiter=","));
    Ns=firstline[0];
    Nf=firstline[1];
    Nd=Ns-na-nb;
    index=0
    sample=0; 
    amatrix = np.empty((3, na, Nf))
    bmatrix = np.empty((3, nb, Nf))
    while index<data.shape[0]:
        for i in range(na):
            amatrix[:, i, sample] = data[index,:].T
            index += 1
        for i in range(nb):
            bmatrix[:, i, sample] = data[index,:].T
            index += 1
        index += Nd
        sample += 1
    return amatrix, bmatrix
    


# In[79]:


def loadoutput(filepath):
    # Creates the right format for the D and C matrices

    Nf=np.genfromtxt(filepath,max_rows=1).astype(int); 
    data=np.double(np.genfromtxt(filepath,skip_header=1));
    dmatrix=data[:,0:3].T;
    cmatrix=data[:,3:6].T; 

    return dmatrix, cmatrix


# In[87]:


def write_output(file_name, d_matrix, c_matrix):
    # Writes the d and cmatrices to the output file

    out_file = open(file_name, 'w')
    out_file.write(str(d_matrix.shape[1]) + ',\t' + file_name + '\n')
    for i in range(d_matrix.shape[1]):
        to_write = "%.2f, %.2f, %.2f,\t%.2f, %.2f, %.2f,\t%.2f" % (d_matrix[0, i], d_matrix[1, i], d_matrix[2, i],
                                                                   c_matrix[0, i], c_matrix[1, i], c_matrix[2, i],
                                                                   np.linalg.norm(d_matrix[:, i] - c_matrix[:, i]))
        out_file.write(to_write+'\n')
    out_file.close()