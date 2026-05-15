# QUESTION 8 - BOOLEAN MASKING TO EXTRACT VALUES GREATER THAN 50

import numpy as np

arr = np.array([10, 55, 23, 80, 90])

mask = arr > 50

print(arr[mask])