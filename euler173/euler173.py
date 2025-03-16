from math import sqrt
import numpy as np


def count_laminae(T):
    "Get number of possible square laminae using at most `t` tiles"
    total = 0

    for d in range(1, T//4):
        # count all integers D satisfying
        #   • D^2 - d^2 <= T
        #   • D > d
        #   • D == d (mod 2)

        num_possible = (int(sqrt(T + d**2)) - d) // 2
        print(d, num_possible)

        total += num_possible

    return total


assert(count_laminae(100) == 41)

print(count_laminae(1_000_000))
