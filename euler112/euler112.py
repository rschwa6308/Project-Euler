# import math


# def I(n, d):
#     return math.comb(n + d - 1, d - 1)

# def D(n, d):
#     return math.comb(n + d - 1, d - 1)

# def B(n):
#     return 9 * 10**(n-1) - I(n, 9) - D(n, 10) + 10
#     #                          ^^^ (no leading zeros)


# bouncy_total = 0
# for n in range(1, 8):
#     bouncy_total += B(n)
#     print(f"Bouncy numbers < 10^{n}: {bouncy_total} ({bouncy_total / 10**n:%}) ")


# LOL looks like the answer is < 10^7... brute force will work just fine :)


def is_increasing(n):
    digits = list(map(int, str(n)))
    for i in range(len(digits) - 1):
        if digits[i] > digits[i+1]:
            return False
    
    return True

def is_decreasing(n):
    return is_increasing(int(str(n)[::-1]))

def is_bouncy(n):
    return not is_increasing(n) and not is_decreasing(n)


bouncy_count = 0
for n in range(1, 10**7):
    if is_bouncy(n):
        bouncy_count += 1
    
    if bouncy_count / n == 0.99:
        print(n)
        break


# => 1587000
