# QUESTION 3 - NEURAL NETWORK WEIGHT SIMULATIONS

import numpy as np

weights = np.random.randn(3,4)
print(weights)

weights_mean = np.mean(weights)
weights_std = np.std(weights)

print("Mean:", weights_mean)
print("Standard Deviation:", weights_std)

# The negative values are there because randn generates values from standard normal distribution.
# The are centerd either side of zero, (i.e left side of zero is negative)