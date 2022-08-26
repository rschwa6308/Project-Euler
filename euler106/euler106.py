from itertools import combinations

from tqdm import tqdm
from pprint import pprint

def powerset(A, sizes=None):
    if sizes is None:
        sizes = range(len(A) + 1)

    for size in sizes:
        for subset in combinations(A, size):
            yield subset



assert len(list(powerset(range(5)))) == 2**5



# Since we are assuming that condition 2 is always satisfied,
# we need only compare subsets of equal size. 
# 
# Say B "dominates" C iff every element of B is > its
# corresponding element in C. If B dominates C, then
# necessarily S(B) > S(C).
# 
# Thus, we only need only compare pairs where there neither B
# nor C dominate the other.



def dominates(B, C):
    return all(b > c for b, c in zip(B, C))



A = set(range(12))

total = 0

for B in powerset(A, sizes=range(1, len(A))):
    B_comp = A - set(B)
    for C in powerset(B_comp, sizes=range(1, min(len(B_comp), len(B)) + 1)):
        if len(B) == len(C) and B[0] < C[0]: continue   # ensure B is lexicographically larger 
        assert len(B) >= len(C)

        # only examine pairs of equal length
        if len(B) != len(C): continue

        if not dominates(B, C):
            # print(B, C)
            total += 1


print(total)

# => 21384
