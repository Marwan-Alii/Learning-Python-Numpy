import numpy as np

mat_a = np.array([
    [5, 3, 4],
    [4, 3, 2]
])

mat_b = np.array([
    [32, 31],
    [83, 9],
    [3, 1]
])

print(mat_a @ mat_b)
print(np.matmul(mat_a, mat_b))

# A @ B is only applicable only if:
# No. of Columns of A == No. of Rows of B

# a * b is Element Wise Multiplication

# TRANSPOSE
print("Transpose of A")
print(mat_a.T)

# IDENTITY MATRIX
Identity = np.eye(3)

print(mat_a @ Identity)

# DETERMINANT
my_mat = np.array([
    [3,4,5],
    [6,3,7],
    [8,2,4]
])
print("Determinant of mat_a:", np.round(np.linalg.det(my_mat)))

# INVERSE
my_inv = np.linalg.inv(my_mat)
print(my_inv)

# Verification of Inverse
my_I = my_mat @ my_inv
print(my_I)
my_I_clean = np.where(np.abs(my_I) < 1e-15, 0, my_I)
print(my_I_clean)

# SOLVING LINEAR EQUATIONS
# Suppose the Following Linear Equations
# 2x + 3y = 14
# 5x - 7y = 1

coeff = np.array([
    [2, 3],
    [5, -7]
])

vals = np.array([14,1])

solution = np.linalg.solve(coeff, vals)
print(solution)

# VECTOR MAGNITUDE
my_vector = np.array([5,3,2])
mag = np.linalg.norm(my_vector)
print(mag)