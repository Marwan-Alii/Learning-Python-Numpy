# QUESTION 6 - COIN TOSS SIMULATION

import numpy as np

coin_result = ["Head", "Tails"]

simulation = np.random.choice(coin_result, 20)

print(simulation)

head_mask = ("Head" == simulation)
num_head = np.sum(head_mask)

tail_mask = ("Tails" == simulation)
num_tail = np.sum(tail_mask)

print("Heads:", num_head)
print("Tails:", num_tail)