# QUESTION 5 - TRANSPOSE OF A MATRIX
# ALSO FIND THE SHAPE OF THE MATRIX BEFORE AND AFTER THE TRANSPOSE

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
 ])

print("Before Transpose:", arr.shape)
arr = arr.T
print("After Transpose:", arr.shape)