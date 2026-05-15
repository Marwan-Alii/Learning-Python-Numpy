import numpy as np

my_arr = np.array([1,2,3,4,5]) #Creating Array

print(my_arr)
#Notice there are no commas in between in Output

print("\nAdding two lists vs Arrays")
a = [1,2,3]
b = [4,5,6]
print("List Addition")
print(a, "+", b, "=" ,a+b)

arr_a = np.array([1,2,3])
arr_b = np.array([4,5,6])
print("Array Addition")
print(arr_a, "+", arr_b, "=", arr_a + arr_b)