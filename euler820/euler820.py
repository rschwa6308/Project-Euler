
def multiplicative_order(a, n):
    for k in range(1, n):
        if (a**k) % n == 1:
            return k
    
    raise RuntimeError()


assert(multiplicative_order(10, 3) == 1)
assert(multiplicative_order(10, 7) == 6)



def get_2_5_factors(n):
    twos = 0
    fives = 0

    while n % 2 == 0 and n > 0:
        n /= 2
        twos += 1
    
    while n % 5 == 0 and n > 0:
        n /= 5
        fives += 1
    
    return twos, fives


assert(get_2_5_factors(60) == (2, 1))


def d_unit_frac(n, k):
    "Compute $d_n(1/k)$"

    # compute period of decimal expansion analytically
    twos, fives = get_2_5_factors(k)
    k_reduced = k // (2**twos * 5**fives)
    if k_reduced == 1:
        return 0

    period = multiplicative_order(10, k_reduced)
    offset = max(twos, fives)

    # compute repeating portion
    # TODO: correct this
    digits = str((10**period - 1) // k_reduced)

    print(f"k={k} => period={period}, offset={offset}, digits={digits}")

    # get nth digit
    # TODO
    return -1



print(d_unit_frac(7, 1))
print(d_unit_frac(7, 3))
print(d_unit_frac(7, 6))
print(d_unit_frac(7, 7))



def S(n):
    total = 0
    for k in range(1, n+1):
        total += d_unit_frac(n, k)


# print(S(7))
# print(S(100))
# print(S(10_000_000))
