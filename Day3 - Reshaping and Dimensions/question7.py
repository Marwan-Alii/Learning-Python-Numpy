# QUESTION 7 - WHAT IS THE DIFFERENCE

import numpy as np

arr = np.array([[1,2,3],
 [4,5,6]])

print(arr[:,1])     # [2 4]
print(arr[:,1:2])   # [[2] [4]]

# The difference between them is of the dimension
# The first one uses integer indexing, therefore returns 1D Array
# The second one uses Slicing Technique which maintains the original dimensions of the array