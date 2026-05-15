import numpy as np

# COIN SIMULATIONS
coin = ["Tails", "Heads"]

sim = np.random.choice(coin, size=5)
print("Simulated Coin:", sim, "\n")

# DICE SIMULATIONS

sim = np.random.randint(1,7,size=5)
print("Simulated Dice:", sim, "\n")

# RANDOM IMAGE GENERATION
image = np.random.randint(0,256,(5,5,3))
print("Simulated Image:",image)

# NOISE GENERATION
noise = np.random.randn(4)
print(noise)

