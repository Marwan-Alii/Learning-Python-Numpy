import numpy as np

# 0D Scalar
zerod = np.array(5)
print(zerod.ndim)   # 0
print(zerod.shape)
one = np.array([5])     # 1D Array
print(one.ndim)    # 1
print(one.shape)

# 1D Array
oned = np.array([32,52,342,23])
print(oned.ndim)
print(oned.shape)

# 2D Array
twod = np.array([
    [1,2,3,4],
    [23,532,321,455]
])
print(twod.ndim)
print(twod.shape)

# 3D Array
threed = np.array([
    [
        [1,2,3,4],
        [4,5,6,3],
        [6,3,2,32]
    ],
    [
        [10,11,13,12],
        [32,52,84,32],
        [32,32,9,74]
    ]
])

print(threed.ndim)
print(threed.shape)

