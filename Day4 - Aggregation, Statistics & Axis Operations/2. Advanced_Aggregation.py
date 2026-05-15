import numpy as np

# STANDARD DEVIATION

arr = np.array([10, 12, 14, 16, 18])
print("Standard Deviation:", np.std(arr))

# VARIANCE
print("Variation:", np.var(arr))

# CUMULATIVE SUM
print("Cumulative Sum: ", np.cumsum(arr))

# PRODUCT OPERATION
print("Product:", np.prod(arr))

# CUMULATIVE PRODUCT
print("Cumulative Product:", np.cumprod(arr))

# SUM WITH AXIS
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.sum(arr, axis=0)) # Vertical   (Axis = 0)
print(np.sum(arr, axis=1)) # Horizontal (Axis = 1)

# MEAN WITH AXIS
print(np.mean(arr, axis=0))
print(np.mean(arr, axis=1))

# MAX AND MIN WITH AXIS
print(np.max(arr, axis=0))
print(np.min(arr, axis=1))

# KEEP DIMENSIONS
newer = np.sum(arr, axis = 0, keepdims = True)
print(newer)