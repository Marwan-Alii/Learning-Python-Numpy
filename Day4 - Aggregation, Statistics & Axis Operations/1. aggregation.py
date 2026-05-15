# Aggregation means combining many values into fewer values
# Examples are total sum, average, minimum and maximum

import numpy as np

arr = np.array([5,85,-34, 74,39, 0, 124, -84, 77])

# SUM
print(np.sum(arr))
print(arr.sum())

# MEAN OR AVERAGE
# MEAN = Sum of Values / No. of Values
print(np.mean(arr))

# MEDIAN: MIDDLE VALUE AFTER SORTING
print(np.sort(arr))     # Sorted Data, To Spot Median Easily
print(np.median(arr))

even_arr = np.array([1,2,3,4])
print(np.median(even_arr))
# For even size, the average of the 2 middle elements is taken
# (2+3)/2

# MINIMUM AND MAXIMUM
print("Minimum:", np.min(arr), sep = "")
print("Maximum: ", np.max(arr), sep = "")

# ARGMAX AND ARGMIN
# They returns the Indices of the Maximum and Minimum Element

print("Argmin:", np.argmin(arr))
print("Argmax:", np.argmax(arr))