from math import sqrt



def is_square(N):
    r = round(sqrt(N))
    return r * r == N


def is_prime(n):
    for d in range(2, int(sqrt(n))):
        if n%d == 0:
            return False
    return True


found = []

for n in range(1, 50_000_000, 2):
    # only loop over perfect squares
    N = n*n

    if N % 10 not in [1,9]: continue

    s = str(N)

    if s[0] not in '19': continue    

    N_rev = int(s[::-1])

    # eliminate palindromes
    if N == N_rev: continue

    # eliminate if reverse is not also a perfect square
    if not is_square(N_rev): continue

    n_rev = int(sqrt(N_rev))

    # do primality check as late as possible
    if is_prime(n) and is_prime(n_rev):
        print(N)
        found.append(N)

        if len(found) == 50: break

print(sum(found))

# 3807504276997394
