# QUESTION 3 - WILL THIS WORK

import numpy as np

arr = np.array([1,2,3,4,5,6])

arr = arr.reshape(4,2)

print(arr)

#This will not work because the dimension does not suit
# 4x2 = 8, and the number of elements in the array is 6.
# Therefore, it is not compatible