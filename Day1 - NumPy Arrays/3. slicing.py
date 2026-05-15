import numpy as np

#One dimensional Array
oned = np.array([0,1,2,3,4,5,6,7,8,9])

#2D Array
twod = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# 3D Array
threed = np.array([
    [ [1, 2, 3], [4, 5, 6] ],
    [ [7, 8, 9], [10, 11, 12] ]
])

# Slicing in 1D Array
# Syntax: [start : end : jump]
# Start: Included | Stop: Excluded

print("1D Slicing")
print(oned[2:6]) # Accesses Indices 2,3,4 and 5 Excludes 6

print(oned[1:6:2]) # 1,3,5

print(oned[::2]) #Accesing each 2nd element

print(oned[::-1]) #Reverse Array

# 2D Slicing
print("\n2D Slicing")
print(twod[1])
print(twod[:,1])
print(twod[0:2, 1:3]) # Submatrix

