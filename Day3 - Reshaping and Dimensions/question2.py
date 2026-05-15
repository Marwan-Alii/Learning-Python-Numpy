# QUESTION 2 - RESHAPE INTO (2,3) and (3,2)

import numpy as np

arr = np.array([1,2,3,4,5,6])

arr = arr.reshape(2,3)
print(arr)

arr = arr.reshape(3,2)
print(arr)