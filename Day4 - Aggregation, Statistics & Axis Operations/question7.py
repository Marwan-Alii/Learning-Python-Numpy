# QUESTION 7 - SUM WITH AXIS

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

axis0 = np.sum(arr, axis = 0)
axis1 = np.sum(arr, axis = 1)

print("Axis 0 Sum:", axis0)
print("Axis 1 Sum:", axis1)