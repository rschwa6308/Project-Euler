# Some notes:
#
# We check 30 different species, corresponding
# to the 30 partitions of 9.

from itertools import combinations, permutations, product

from tqdm import tqdm
from pprint import pprint


# MAX = 10**9
# sieve = [True] * (MAX + 1)
# sieve[0] = False
# sieve[1] = False

# for n, _ in tqdm(enumerate(sieve)):
#     if not sieve[n]: continue

#     for i in range(n*2, MAX, n):
#         sieve[i] = False


# # pprint(sieve)



# def is_prime(n):
#     return sieve[n]


def is_prime(n):
    for d in range(2, int(n ** 0.5) + 2):
        if n%d == 0: return False
    
    return True



assert is_prime(17)




# https://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p









def union(*sets):
    if len(sets) == 0:
        return set()

    if len(sets) == 1:
        return sets[0]
    
    return sets[0].union(*sets[1:])


DIGITS = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def lexless(A, B):
    if len(A) < len(B): return True
    return all(a < b for a, b in zip(sorted(A), sorted(B)))


def tuple2int(s):
    return int("".join(map(str, s)))


total = 0

for species in partitions(9):
    # if 7 in species or 8 in species or 9 in species: continue
    print(species)


    partitionings = [[]]
    for k in species:
        partitionings = [
            x+[set(y)]
            for x in partitionings
            for y in combinations(DIGITS - union(*x), k)
            if len(x) == 0 or lexless(x[-1], y)
        ]
    
    # ^this would have been so much easier with a tail-recursive function
    # why am i like this

    # pprint(partitionings)

    def primes_count(s):
        # can immediately disqualify all permutations if mult of 3 (slight speedup)
        if tuple(s) != (3,) and sum(s) % 3 == 0:
            return 0
        
        nums_from_s = map(tuple2int, permutations(s))
        
        primes_from_s = [n for n in nums_from_s if is_prime(n)]
        return len(primes_from_s)

            


    for partition in partitionings:
        # print(f"{partition=}")
        p = 1
        for s in partition:            
            # print(s, primes_count(s))
            p *= primes_count(s)

        # if p > 0:
        #     print(f"{str(partition):<35} => {p}")
        
        total += p

print(total)

# TODO: find the off-by-one-like error lurking in here

