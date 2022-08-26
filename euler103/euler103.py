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


def is_special(A):
    for B in powerset(A, sizes=range(1, len(A))):
        B_comp = A - set(B)
        for C in powerset(B_comp, sizes=range(1, min(len(B_comp), len(B)) + 1)):
            assert len(B) >= len(C)
            # print(B, C)

            # condition 1
            if sum(B) == sum(C):
                return False
            
            # condition 2
            if len(B) > len(C) and sum(B) <= sum(C):
                return False
    
    return True



assert not is_special({1, 2, 3})
assert is_special({2, 3, 4})
assert is_special({6, 9, 11, 12, 13})


optimal_set = {999999999}

# Based on the provided heuristic, we expect the optimal set
# to contain values in the range of 20 to 45. We brute search
# within this range (with some buffer on either side).

for A in tqdm(combinations(range(18, 47), 7)):
    if is_special(set(A)):
        print(A)
        if sum(A) < sum(optimal_set):
            optimal_set = A


print(optimal_set)
print("".join(map(str, sorted(optimal_set))))

# => 20313839404245
