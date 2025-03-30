import numpy as np
from itertools import product


PETER_NUM_DICE = 9
PETER_DICE_TYPE = 4

COLIN_NUM_DICE = 6
COLIN_DICE_TYPE = 6


peter = np.zeros(PETER_NUM_DICE*PETER_DICE_TYPE+1, dtype=int)
colin = np.zeros(COLIN_NUM_DICE*COLIN_DICE_TYPE+1, dtype=int)

for rolls in product(range(1, PETER_DICE_TYPE+1), repeat=PETER_NUM_DICE):
    score = sum(rolls)
    peter[score] += 1


for rolls in product(range(1, COLIN_DICE_TYPE+1), repeat=COLIN_NUM_DICE):
    score = sum(rolls)
    colin[score] += 1


colin_cum = np.cumsum(colin)

peter_win_count = 0

for score in range(1, PETER_NUM_DICE*PETER_DICE_TYPE+1):
    peter_win_count += peter[score] * colin_cum[score - 1]


peter_win_prob = peter_win_count / (np.sum(peter) * np.sum(colin))
print(f"{peter_win_prob:0.7f}")
