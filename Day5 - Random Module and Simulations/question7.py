# QUESTION 7 - AI LABEL GENERATION
# Generate 50 Labels
# Cat = 0 | Dog = 1
# Count Cats and Dogs

import numpy as np

values = np.random.randint(0,2,50)

print(values)
print(values)

cat_mask = (0 == values)
dog_mask = (1 == values)

num_cat = np.sum(cat_mask)
num_dog = np.sum(dog_mask)

print("Cats:", num_cat)
print("Dogs:", num_dog)

# Can I optimize this code even more?