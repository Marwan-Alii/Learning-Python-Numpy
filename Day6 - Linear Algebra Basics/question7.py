# QUESTION 7 - DETERMINANT AND INVERSE

import numpy as np

arr = np.array([
    [2,1],
    [5,3]
 ])

print("Determinant:", np.linalg.det(arr))
print("Inverse\n", np.linalg.inv(arr))