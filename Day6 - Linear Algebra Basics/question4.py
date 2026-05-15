# QUESTION 4 - ELEMENT WISE vs MATRIX MULTIPLICATION

import numpy as np

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print(a @ b)    # Matrix Multiplication

print(a * b)    # Element Wise Multiplication

# The Difference is that in the Element Wise Multiplication, we are multiplying each element by their corresponding index in the other vector / matrix
# While in the Matrix Multiplication, we multiply rows to columns, and add their values for a specific index
# In short, we perform the standard linear algebra multiplication in Matrix Multiplcation