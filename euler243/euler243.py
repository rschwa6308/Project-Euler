

import math
import sympy
from tqdm import tqdm
from pprint import pprint


def build_prime_factorizations(MAX):
    """
    Using a modified sieve of Eratosthenes, generate full 
    prime factorizations of all positive integers `n < MAX`

    Return format is a list of dictionaries
    (e.g. `res[18] = {2: 1, 3: 2}`)
    """

    factorizations = [{} for _ in range(MAX)]

    for p in tqdm(range(2, MAX)):
        if factorizations[p]: continue   # composite

        print(f"{p=}")

        multiplicity = 1
        while p**multiplicity < MAX:
            for n in range(p**multiplicity, MAX, p**multiplicity):
                if n%1_000_000 == 0: print(f"{n=} {multiplicity=}")
                factorizations[n][p] = multiplicity
            
            multiplicity += 1

    return factorizations



MAX = 100_000_000
FACTORIZATIONS = build_prime_factorizations(MAX)

# for i, factorization in enumerate(FACTORIZATIONS):
#     print(f"{i}: {factorization}")




def phi(n):
    return math.prod(p**(e-1)*(p-1) for p, e in FACTORIZATIONS[n].items())


for n in range(2, 100):
    assert phi(n) == sympy.totient(n)


def R(d):
    return phi(d) / (d - 1)


assert R(12) == 4/11


for d in tqdm(range(2, MAX)):
    if R(d) < 15499/94744:
        print(d)
        break

