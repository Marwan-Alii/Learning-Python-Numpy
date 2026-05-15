# STUDENT DATASET ANALYZER

import dataset as ds

# DATASET ANALYSIS
print("\n=== DATA SET ANALYSIS ===")
print("Dataset Shape", ds.students.shape)
print("Number of Dimensions:", ds.students.ndim)
print("Total Elements:", ds.students.size)

# STUDENT WISE ANALYSIS
print("\n=== STUDENT WISE ANALYSIS ===")
total_marks = ds.np.sum(ds.students, axis=1)
print("Total Marks:", total_marks)
avg_marks = ds.np.mean(ds.students,axis=1)
print("Average Marks:", avg_marks)

# SUBJECT WISE ANALYSIS
print("\n=== SUBJECT WISE ANALYSIS ===")
avg_sub = ds.np.mean(ds.students,axis=0)
print("Average Marks:", avg_sub)
high_sub = ds.np.max(ds.students,axis=0)
print("Highest Marks:", high_sub)
low_sub = ds.np.min(ds.students, axis=0)
print("Lowest Marks:", low_sub)

# BEST STUDENT
best_idx = total_marks.argmax()
print(f"\nStudent at Index {best_idx} has the Highest Marks")

# NORMALIZATION
normalized = ds.students / 100
print(normalized)

# STANDARD DEVIATION
subj_std = ds.np.std(ds.students, axis=0)
print(subj_std)

# High Standard Deviation - The marks are spread out
# Low Standard Deviation  - All Students have performed similarly

subj_std_mean = ds.np.mean(subj_std)
print(subj_std_mean)

high_std = subj_std > subj_std_mean
low_std = subj_std <= subj_std_mean

print(high_std)
print(low_std)

# TOP SCORING SUBJECT
high_avg_sub = ds.np.argmax(avg_sub)
print(f"\nSubject {high_avg_sub} has the Highest Average Marks\n")

# PASS FAIL ANALYSIS
status = ds.students > 50
print(status)

grade_A = ds.assign_grade(ds.students, 85, 100)
grade_B = ds.assign_grade(ds.students, 70, 85)
grade_C = ds.assign_grade(ds.students, 0, 70)

print("A Grades")
print(grade_A)

print("B Grades")
print(grade_B)

print("C Grades")
print(grade_C)

# FINAL INTERPRETATION
# Student (Index: 3) performed the best scoring 352
# Subject at Index 0 was the hardest as It had the lowest Average Marks (80)
# Normalization helps here because we can store large values easily, also it can help with finding the percentage (simply mulitply by 100)
# Subject (Index: 1) had the most consistent marks because of the lowest STD(Standard Deviation: 6.6753)