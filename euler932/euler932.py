from math import log10, sqrt


POWERS_OF_TEN = [10**i for i in range(20)]


def is_2025(s):
    "Determine if N = s^2 is a '2025' number"
    N = s**2

    num_digits = int(log10(N)) + 1

    for i in range(1, num_digits):
        a = N // POWERS_OF_TEN[i]
        b = N % POWERS_OF_TEN[i]

        if (N // POWERS_OF_TEN[i-1]) % 10 == 0:
            continue

        if a + b == s:
            return True

    return False


assert(is_2025(45))
assert(not is_2025(99))

def T(n):
    s = 1
    total = 0

    for s in range(1, 10**(n//2)):
        if is_2025(s):
            total += s**2
            print(s**2)
    
    return total


print(T(4))
assert(T(4) == 5131)

print(T(16))
