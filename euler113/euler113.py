import math


def I(n, d):
    return math.comb(n + d - 1, d - 1)

def D(n, d):
    return math.comb(n + d - 1, d - 1)


nonbouncy_total = 0
for n in range(1, 101):
    nonbouncy_total += I(n, 9) + D(n, 10) - 10
    #   (no leading zeros) ^^^             ^^^^ (constant sequences double counted)

    print(f"Nonbouncy numbers < 10^{n}: {nonbouncy_total} ({nonbouncy_total / 10**n:%}) ")

# => 51161058134250
