# Matrix Algebra

import numpy as np

A = np.array([[1,2,3],
	[2,7,4]])

B = np.array([[1,-1],
	[0,1]])

C = np.array([[5,-1],
	[9,1],
	[6,0]])

D = np.array([[3,-2,-1],
	[1,2,3]])

u = np.array([6,2,-3,5])

v = np.array([3,5,-1,4])

w = np.array([[1],
	[8],
	[0],
	[5]])

# 1. Matrix Dimensions 
print ("Matrix Dimensions:")
print (A.shape) # 2 rows, 3 cols
print (B.shape) # 2 rows, 2 cols
print (C.shape) # 3 rows, 2 cols
print (D.shape) # 2 rows, 3 cols
print (u.shape) # 1 row, 4 cols
print (w.shape) # 4 rows, 1 col

# 2. Vector Operations
print("Vector Operations:") 
print (u+v) # [9 7 -4 9]
print (u-v) # [3 -3 -2 1]
print (6*u) # [36 12 -18 30]
print (np.dot(u,v)) # 51
print (np.linalg.norm(u)) # 8.602

#3 Matrix Operations
print ("Matrix Operations:")
print ("Undefined")
print (A - C.transpose()) # [-4 -7 -3] / [3 6 4]
print (C.transpose() + 3*D) # [14 3 3 ] / [2 7 9]
print (np.dot(B, A)) #[ -1 -5 -1] / [2 7 4]
print ("Undefined. cannot multiply B times transpose A")

print ("Optional:")
print ("Undefined")
print (np.dot(C, B)) # [5 -6] / [9 -8] / [6 -6]
print (np.dot(np.dot(np.dot(B,B),B),B)) # [1 -4] / [0 1 ]
print (np.dot(A, A.transpose())) # [14 28] / [28 69]
print (np.dot(D.transpose(), D)) # [10 -4 0] / [-4 8 8] / [0 8 10]




