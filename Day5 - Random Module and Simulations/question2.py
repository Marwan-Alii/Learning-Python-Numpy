# QUESTION 2 - RANDOM GRAYSCALE IMAGE GENERATION

import numpy as np

grayscale_image = np.random.randint(0,256, (5,5))
print("Grayscale Image")
print(grayscale_image)

color_image = np.random.randint(0,256,(5,5,3))
print("Colored Image")
print(color_image)

max_pixel = np.max(grayscale_image)

avg_brightness = np.mean(grayscale_image)

print(max_pixel)
print(avg_brightness)