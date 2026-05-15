# QUESTION 8 - HARDER AXIS QUESTION
# Generate 4x4 random integers between 1 and 20
# Row Sum
# Column Mean
# Maximum Values in each row

import numpy as np

values = np.random.randint(1,21,(4,4))

print(values)

row_sum = np.sum(values, axis=1)
print("Row Sum")
print(row_sum)

col_mean = np.mean(values, axis=0)
print("Column Mean")
print(col_mean)

max_row = np.max(values, axis=1)
print("Maximum in Row")
print(max_row)