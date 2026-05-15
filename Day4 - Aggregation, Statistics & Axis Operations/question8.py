# QUESTION 8 - MEAN WITH AXIS

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

axis0 = np.mean(arr, axis = 0)
axis1 = np.mean(arr, axis = 1)

print("Axis 0 Mean:", axis0)
print("Axis 1 Mean:", axis1)