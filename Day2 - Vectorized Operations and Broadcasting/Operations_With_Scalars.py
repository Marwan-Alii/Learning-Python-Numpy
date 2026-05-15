# OPERATIONS WITH SCALARS

import numpy as np

my_arr = np.array([1,2,63,32,52,22])

print(f"{my_arr} + 10 = {my_arr + 10}")
print(f"{my_arr} *  4 = {my_arr *  4}")
print(f"{my_arr} /  7 = {my_arr /  7}")

# Comparison Operations

print("\nComparison Operations")
print(my_arr > 10)
print(my_arr < 10)
print(52 == my_arr)

# We can also store the result
mask = my_arr > 10
print("mask:", mask)
print(my_arr[mask])

# There is also a shorter form for this
print(my_arr[my_arr < 30])


# BROADCASTING
print("\nBROADCASTING")
print(f"{my_arr} + 10 = {my_arr + 10}\n")
# Internally, my_arr + [10, 10, 10]
# internally, numpy treats 10 as [10, 10, 10] without actaully creating it
# This is called Broadcasting
# The Same happens for nD Arrays

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

# internally, [[1,2,3], [4,5,6]] + [[10,20,30], [10,20,30]]

print(a + b)

# Two Dimensions are Compatible either if they are equal or one of them is 1


# Square Root
my_array = np.array([1,4,9,16,25,36,49,64,81,100])
print("Square Root: ", end = "")
print(np.sqrt(my_array))

# Exponential
print("Exponential: ", end = "")
print(np.exp(my_array))

# Sin Function
print("Sin: ", end = "")
print(np.sin(my_array))

# Absolute Value
abs_array = np.array([3,-3,4,-7,-2,3])
print("Absolute Value of ", abs_array,end = ": ")
print(np.abs(abs_array))