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


assert not is_special({81, 88, 75, 42, 87, 84, 86, 65})
assert is_special({157, 150, 164, 119, 79, 159, 161, 139, 158})



SETS = []
with open("p105_sets.txt") as f:
    for line in f.readlines():
        A = set(map(int, line.split(",")))
        SETS.append(A)


pprint(SETS)


total = 0
for A in tqdm(SETS):
    if is_special(A):
        total += sum(A)

print(total)

# => 73702
