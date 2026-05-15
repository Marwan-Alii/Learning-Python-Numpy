# QUESTION 3 - FIND ARGMAX AND ARGMIN

import numpy as np

arr = np.array([10,50,20,5])

max_idx = np.argmax(arr)
min_idx = np.argmin(arr)

print(f"Maximum {arr[max_idx]} at Index {max_idx}")
print(f"Minimum {arr[min_idx]} at Index {min_idx}")