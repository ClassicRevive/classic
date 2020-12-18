# This code is for a random walk simulation of a dice rolling game
# it reads explanatorially but if a 6 is rolled, the player goes up by the
# number of steps of their next role

import numpy as np
import matplotlib.pyplot as plt

# Initialization
all_walks = []
for i in range(250):
    random_walk = [0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        random_walk.append(step)
    all_walks.append(random_walk)

np_aw = np.array(all_walks)
np_aw_t = np.transpose(np_aw)

# Plot random_walks
plt.figure()
plt.plot(np_aw_t)
plt.title("Random Walk simulation (n = 250)")

# Show the plot
plt.show()

# Select last row from np_aw_t: ends
ends = np_aw_t[:,-1]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.title("Distribution of random walks")
plt.show()
