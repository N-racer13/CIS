Code structure
------------------------
methods.py
Script with the algorithms for finding the closest point on a mesh. The methods are based on the approaches seen in class.
ios.py 
Contains all input/output methods. This is used to load in information from files, as well as write our outputs.
Carthesian_math_package.py
This script uses the same functions as the ones developed during the previous assignments and will therefore not be explained again. As a brief summary, it comprises basic transformations like: Rotation, Transformation and inverse Transformation, calculate the center, quaternion to matrix. On top of that, a function was added to order the vertices of a triangle according to its length.
assignment3.py
The main script that runs the octree algorithm to determine the c and d vectors. This is done by first preprocessing the data using ios.py




Running the code
------------------------
The main script is assignment3.py

This script takes an argument which is the character identifying the unknown set to be processed (G, H or J).
Simply typ the letter of the dataset you want to use. The output data will be presented in the data folder.
Our OUTPUT folder is simply a copy paste of the necessary results from the data folder.