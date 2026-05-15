import numpy as np

# VECTOR OPERATIONS
arr_a = np.array([1,2,9,3])
arr_b = np.array([23, 42, 22, -7])

# 1. Vector Addition
print("Vector Addition:", arr_a + arr_b)

# 2. Vector Subtraction
print("Vector Subtraction:",arr_a - arr_b)

# 3. Scalar Multiplication
print("Scalar Multiplication by 5:", arr_a * 5)

# DOT PRODUCT
# A.B = (a1 x b1) + (a2 x b2) + (a3 x b3) + ....
print("Dot Product:", np.dot(arr_a, arr_b))