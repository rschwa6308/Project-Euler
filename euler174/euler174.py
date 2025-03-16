from math import sqrt
import numpy as np
from tqdm import tqdm


def get_exact_laminae_counts_table(T):
    "Compute a table `tab` such that `tab[t]` is the number of possible square laminae using *exactly* `t` tiles"

    LAMINAE_COUNTS_EXACT = np.zeros(T+1, dtype=np.uint64)

    for d in tqdm(range(1, T//4)):
        # enumerate all integers D satisfying
        #   • D^2 - d^2 <= T
        #   • D > d
        #   • D == d (mod 2)

        D_max = int(sqrt(T + d**2))     # inclusive
        D_min = d+1                     # inclusive

        Ds = np.arange(D_min, D_max+1, dtype=np.uint64)[1::2]
        # print(d, Ds)

        tile_counts = Ds**2 - d**2
        LAMINAE_COUNTS_EXACT[tile_counts] += 1

    return LAMINAE_COUNTS_EXACT


LAMINAE_COUNTS_EXACT = get_exact_laminae_counts_table(1_000_000)

assert(LAMINAE_COUNTS_EXACT[8] == 1)
assert(LAMINAE_COUNTS_EXACT[32] == 2)

def N(n):
    return np.count_nonzero(LAMINAE_COUNTS_EXACT == n)

assert(N(15) == 832)

print(sum(N(n) for n in range(1, 10+1)))
