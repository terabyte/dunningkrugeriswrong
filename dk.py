#!/usr/bin/env python3

# plotting inspired by https://matplotlib.org/3.5.0/tutorials/introductory/usage.html
import math
import matplotlib.pyplot as plt
import numpy as np
import pprint
import random


# the original dunning kruger experiment produced a graph where the data was split into quartiles for actual performance on the X axis, and perceived performance on the Y axis in percent.
# therefore, truly random data would be to produce two independent coordinates from 0 to 1, then graph them similarly.


NUM_PARTICIPANTS = 10000
NUM_GROUPS = 4

SCORES = []
GROUPS = []

for i in range(NUM_PARTICIPANTS):
    SCORES.append([random.random(), random.random()])

for i in range(NUM_GROUPS):
    GROUPS.append([])

# next, we need to sort the scores into groups (in the original experiment, quartiles)
for score in SCORES:
    group = math.floor(score[0] * NUM_GROUPS)
    GROUPS[group].append(score)

# finally, average their perceived score

FINAL_DATA = []

for i in range(NUM_GROUPS):
    average = np.mean(list(map(lambda x: x[1], GROUPS[i])))
    FINAL_DATA.append([1.0 * (i / NUM_GROUPS), average])

pprint.pprint(FINAL_DATA)

# plot it
fig, ax = plt.subplots()
fig.suptitle("Dunning Kruger or Random Data?")
ax.set_xlabel("Group by Score")
ax.set_ylabel("Perceived Performance")
ax.plot(FINAL_DATA, 'o-', label=["actual test score", "perceived ability"])

legend = ax.legend()
plt.savefig('out.png')
# plt.show()
