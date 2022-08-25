import math
from pprint import pprint
from tqdm import tqdm


def pentagonal_number(k):
    return int(k*(3*k-1) / 2)

def compute_partitions(goal):
    partitions = [1]
    for n in tqdm(range(1,goal+1)):
        partitions.append(0)
        k_min = math.ceil(-((24*n + 1)**0.5 - 1) / 6)
        k_max = math.floor(((24*n + 1)**0.5 + 1) / 6)
        for k in range(k_min, k_max + 1):
            if k == 0: continue
            coeff = 1 if k%2 else -1
            partitions[n] += coeff*partitions[n - pentagonal_number(k)]
            # for t in [pentagonal_number(k), pentagonal_number(-k)]:
            #     if (n-t) >= 0:
            #         partitions[n] += coeff*partitions[n-t]
    return partitions



N = 10 ** 5
parts = compute_partitions(N)

pprint(parts[:10])

for n in range(N):
    if parts[n] % (10 ** 6) == 0:
        print(n)
        break


# NOTES
# What we likely know about the answer n:
#   n = 4 (mod 5)       (see https://en.wikipedia.org/wiki/Ramanujan%27s_congruences)