# QUESTION 8 - SOLVE LINEAR EQUATIONS
# x + y = 5
# 2x - y = 1

import numpy as np

A = np.array([
    [1, 1],
    [2, -1]
])

B = np.array([5, 1])

answers = np.linalg.solve(A, B)

print(f"x = {answers[0]}")
print(f"y = {answers[1]}")