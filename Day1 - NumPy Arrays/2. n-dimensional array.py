import numpy as np

#One dimensional Array
oned = np.array([1,2,3])

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

# Dimension of Array
print("Shape")
print(oned.shape)
print(twod.shape)
print(threed.shape)

# Number of Dimensions
print("Number of Dimensions")
print(oned.ndim)
print(twod.ndim)
print(threed.ndim)

# Data Type
print("Data Type")
print(oned.dtype)
print(threed.dtype)

# Total Elements
print("Total Elements")
print(twod.size)

# Accessing Individual Elements

# 1D Array
print("Accessing Element in 1D Array at Index [1]: ", end = "")
print(oned[1])
print("Accessing Element in 1D Array at Index [-1]: ", end = "")
print(oned[-1], "\n")

# 2D Array
print("Accessing Element in 2D Array at Index [1,2]: ", end = "")
print(twod[1,2])
print("Accessing Element in 2D Array at Index [-1,-2]: ", end = "")
print(twod[-1,-2], "\n")

# 3D Array
print("Accessing Element in 3D Array at Index [1,0,2]: ", end = "")
print(threed[1,0,2])
print("Accessing Element in 3D Array at Index [-1,-1,-2]: ", end = "")
print(threed[-1,-1,-2])