import numpy as np

num = np.random.randint(1, 10)
# randint(start, end)
# start - included
# end - excluded

print(num)

# GENERATING MULTIPLE RANDOM VALUES

arr = np.random.randint(1, 99, size = 5)
print(arr)

# 2D Random Values

arr = np.random.randint(0,256, size = (4,3))
print(arr)

# RANDOM FLOATS (rand)
random_values = np.random.rand(5)
print(random_values)

twoD_rand_floats = np.random.rand(2,3)
print(twoD_rand_floats)

# RANDOM CHOICE

rgb = ["Red", "Green", "Blue"]

color_choice = np.random.choice(rgb)
print(color_choice)

# MULTIPLE RANDOM CHOICES
color_choice = np.random.choice(rgb, size=10)

print(color_choice)

# PROBABILITY BASED CHOICES
probability = [0.432, 0.068, 0.32, 0.08, 0.06, 0.04]
options = ['A',       'B',   'C',  'D',  'E',  'F' ]

rand_choice = np.random.choice(options, p = probability)
print(rand_choice)

# SHUFFLING DATA
np.random.shuffle(options)
print(options)

# RANDOM SEED
np.random.seed(33232)
num = np.random.randint(1,5,5)

print(num)