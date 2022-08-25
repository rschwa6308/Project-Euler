import math
from prime_factorizations import build_prime_factorizations, divisors

from itertools import product

from tqdm import tqdm


FACTORIZATIONS = build_prime_factorizations(1_000_001)


def divsum_naive(n):
    total = 0
    for d in range(1, n):
        if n % d == 0:
            total += d
    
    return total



def divsum(n):
    total = sum(divisors(n, FACTORIZATIONS))
    total -= n      # for this problem, we only want proper divisors
    return total



assert divsum(12496) == 14288


divsum_array = [None] * 1_000_001
# divsum_array = [None] * 1_000

print("Computing divsum array")
for n in tqdm(range(1, len(divsum_array))):
    divsum_array[n] = divsum(n)


print(divsum_array[:10])


# Find chains (don't have to be very efficient lol)
CHAINS = []

print("Finding chains")
for start in tqdm(range(1, len(divsum_array))):
    # print(f"{start=}")
    curr = start
    path = [curr]
    while True:
        curr = divsum_array[curr]
        if curr == 0: break
        if curr > 1_000_000: break
        if curr in path:
            CHAINS.append(path[path.index(curr):])
            break

        path.append(curr)


longest_chain = max(CHAINS, key=lambda chain: len(chain))
print(longest_chain)
print(min(longest_chain))

# => 14316
