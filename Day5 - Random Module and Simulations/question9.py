# QUESTION 9 - NOISE SIMULATION
# Generate 10 Random Gaussian Values
# Find Mean and Explain Why values are around 0

import numpy as np

values = np.random.randn(10)
print(values)

values_mean = np.mean(values)
print("Mean:", values_mean)

# The values are around 0 because it follows a standard normal distribution, where mean is 0