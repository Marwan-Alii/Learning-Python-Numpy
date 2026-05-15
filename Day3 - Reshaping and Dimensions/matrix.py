import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6]
])

# A matrix is basically a 2D Array

# MATRIX ADDITION
a = np.array([
    [1,3], 
    [4,6]
])

b = np.array([
    [8,9],
    [10,12]
])

sum = a + b
print(a + b)

# MATRIX MULTIPLICATION
element_wise = a * b
print(a * b)    # This is Element Wise Multiplication

matx_mul = a @ b

print(matx_mul)

# We can also use the following:
print(np.matmul(a,b))

