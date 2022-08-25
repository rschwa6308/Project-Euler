import math
from tqdm import tqdm


PERFECT_SQUARES = set()
for n in tqdm(range(1_000_000_000 // 3)):
    PERFECT_SQUARES.add(n**2)

# print(len(PERFECT_SQUARES))
# print(sorted(PERFECT_SQUARES, key=lambda x: abs(1643897025 - x))[:10000])

assert 1643897025 in PERFECT_SQUARES

def area_is_integer(a, b):
    h_squared = a**2 - (b//2)**2
    # print(h_squared)
    if math.sqrt(h_squared).is_integer(): print(h_squared)
    return h_squared in PERFECT_SQUARES


assert area_is_integer(17, 16)

# In order for area to be an integer, (b/2, h, a) must form a
# pythagorean triple. Thus, there is a correspondence between
#  - pythagorean triples of the form (k, _, 2k±1) and
#  - triangles with sides b = 2k and a = 2k±1
# 
# However, a billion isn't actually that big so we can brute force
# it by checking all odd a values and corresponding even b values :)


MAX_PERIMETER = 1_000_000_000
# MAX_PERIMETER = 100

total = 0
for a in tqdm(range(3, MAX_PERIMETER // 3, 2)):
    for b in (a - 1, a + 1):
        if area_is_integer(a, b):
            print(a, a, b)
            total += a + a + b

print(total)