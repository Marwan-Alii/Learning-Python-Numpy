import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2,3)
# Reshape changes array structures without changing the actual array

print(new_arr)

# for arr.reshape(i,j), ixj must equal the size of the array
# i.e rshape(4,2) would fail for the above array

new_arr = arr.reshape(3,-1)
# Numpy automatically calculates one dimension (i.e -1)
print(new_arr)

new_arr = arr.reshape(-1,2)
print(new_arr)


# FLATTENING MULTI-DIMENSIONAL ARRAYS
values = np.array([
    [67, 67],
    [84,76],
    [100, 84]
])

flat = values.flatten()

print(flat)

# TRANSPOSE
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print("Shape Before Transpose: ", arr.shape)
arr = arr.T
print("Shape after Transpose: ", arr.shape)