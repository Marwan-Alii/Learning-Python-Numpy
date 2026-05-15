# QUESTION 10 - HARD QUESTION
# 1. Compute Prediction scores using Dot Product
# 2. Find Feature means (Average) Column Wise
# 3. Normalize features by dividing each column by its maximum value
# 4. Why normalization helps in Machine Learning

import numpy as np

features = np.array([
    [2,4],
    [1,3],
    [5,2]
])

weights = np.array([0.6,0.4])

# PREDICTION USING DOT PRODUCT
predict = np.dot(features, weights)
print("Predictions", predict)

# FEATURE MEANS
feature_mean = np.mean(features, axis=0)
print("Feature Means:", feature_mean)

# NORMALIZATION - Divide the Column by Its Max
col_max = np.max(features, axis=0) # Finding Column Wise Max [5,4]
print(col_max)

# features[:,n] accessing all elements of nth column
# Then Divide my nth column's maximum col_max[n]
# col1_norm = features[:,0] / col_max[0]
# col2_norm = features[:,1] / col_max[1]


# print(col1_norm)
# print(col2_norm)

# normalized = np.array([col1_norm, col2_norm])
# normalized = normalized.T
# print(normalized)

new_normal = features / col_max
print(new_normal)

# Normalization is Important in Machine Learning because it lowers the values of the features
# Smallers values helps the models train easily
# Also, it does not create any biaseness due to weight