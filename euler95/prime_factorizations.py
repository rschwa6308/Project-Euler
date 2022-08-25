import math
import itertools
from tqdm import tqdm


def build_prime_factorizations(MAX):
    """
    Using a modified sieve of Eratosthenes, generate full 
    prime factorizations of all positive integers `n < MAX`

    Return format is a list of dictionaries
    (e.g. `res[18] = {2: 1, 3: 2}`)
    """

    factorizations = [{} for _ in range(MAX)]

    print(f"Generating prime factorizations of all positive integers less than {MAX}")
    for p in tqdm(range(2, MAX)):
        if factorizations[p]: continue   # composite

        # print(f"{p=}")

        multiplicity = 1
        while p**multiplicity < MAX:
            for n in range(p**multiplicity, MAX, p**multiplicity):
                # if n%1_000_000 == 0: print(f"{n=} {multiplicity=}")
                factorizations[n][p] = multiplicity
            
            multiplicity += 1

    return factorizations


def divisors(n, factorizations):
    """
    Return a generator for all of the divisors of `n`
    by iterating over the powerset of the multiset of
    prime factors.

    Argument `factorizations` is expected to be the
    output of `build_prime_factorizations`.

    NOTE: divisors not necessarily returned in order 
    """

    prime_factors = list(factorizations[n].items())
    prime_factors.sort(key=lambda item: item[0])

    exp_ranges = (range(max_exp+1) for _, max_exp in prime_factors)
    for exps in itertools.product(*exp_ranges):
        d = math.prod(p**e for (p, _), e in zip(prime_factors, exps))
        yield d
