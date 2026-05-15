import numpy as np

students = np.array([
    [78, 85, 90, 88],
    [92, 76, 81, 95],
    [67, 72, 70, 68],
    [88, 91, 89, 84],
    [75, 80, 79, 83]
])

# Each Row = Student    | Total 5 Students
# Each Column = Subject | Total 4 Subjects

def assign_grade(arr, low, high):
    return (arr >= low) & (arr < high)