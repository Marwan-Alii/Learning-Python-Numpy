# QUESTION 10 - HARD AI ORIENTED QUESTION
# Find brightest pixel
# Find darkest pixel
# Find average brightness per row
# Find average brightness per column
# Normalize image by dividing all values by 255
# Explain:
#   why normalization is important in AI/image processing.

import numpy as np

image = np.random.randint(0,256,size=(6,6))
print(image)

brightest = np.max(image)
print("Brightest Pixel:",brightest)

darkest = np.min(image)
print("Darkest:", darkest)

avg_br_row = np.mean(image, axis=1)
print("Average Brightness per Row:", avg_br_row)

avg_br_col = np.mean(image, axis=0)
print("Average Brightness per Column:", avg_br_col)

image = image / 255

print("After Normalization")
print(image)

# Normalization is important in AI because this makes the values digestable for the AI model