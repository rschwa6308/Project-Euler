from math import log, prod


def is_prime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    
    return True

assert is_prime(17)
assert not is_prime(26)


def least_pandivisible(N):
    "compute the least number `n` s.t. `n` is divisible by all `d <= N`"

    primes = filter(is_prime, range(2, N+1))

    n = 1
    factorization = {}
    for p in primes:
        e = int(log(N, p))
        n *= p**e
        factorization[p] = e
    
    return n, factorization


# print(least_pandivisible(100))

def phi(factorization):
    return prod(p**(e-1)*(p-1) for p, e in factorization.items()) 


def R(d, factorization):
    return phi(factorization) / (d - 1)


for N in range(5, 100):
    d, factorization = least_pandivisible(N)
    print(phi(factorization))
    if R(d, factorization) < 15499/94744:
        print(N)
        print(d)
        break
