import numpy as np 
import matplotlib.pyplot as plt

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
A  #array([[11, 12, 13],
       [21, 22, 23],
       [31, 32, 33]])
       
       
A.ndim   #2
A.shape  #(3, 3)
A.size   #9

#ACCESS
A[1, 2]  #23
A[1][2]  #23
A[0][0:2]  #array([11, 12])


#OPERATIONS
X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 
Z = X + Y
Z   #array([[3, 1], [1, 3]])

Z = 2 * Y
Z   #array([[4, 2], [2, 4]])

Z = X * Y
Z   #array([[2, 0], [0, 2]])


#MATRIX MULTIPLICATION
A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
Z = np.dot(A,B)
Z   #array([[0, 2], [0, 2]])
np.sin(Z)   #array([[0.        , 0.90929743], [0.        , 0.90929743]])


#TRANSPOSE
C = np.array([[1,1],[2,2],[3,3]])
C.T        #array([[1, 2, 3], [1, 2, 3]])







