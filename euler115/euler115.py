import math


# def partitions(n, I=1):
#     yield (n,)
#     for i in range(I, n//2 + 1):
#         for p in partitions(n-i, i):
#             yield (i,) + p


def partitions_restricted(n, k, I=1):
    """partitions of n into parts of size >= k"""
    if n < k: yield
    yield (n,)
    for i in range(max(I, k), n//2 + 1):
        for p in partitions_restricted(n-i, i):
            yield (i,) + p


def multiset_orderings(mset):
    """number of ways to order the given multiset"""
    repeats = []
    for x in set(mset):
        if (c := mset.count(x)) > 1:
            repeats.append(c)
    
    return math.factorial(len(mset)) // math.prod(math.factorial(r) for r in repeats)


def fill_count(N, m):
    RED_SIZES = []

    for red_total in range(m, N+1):
        for parts in partitions_restricted(red_total, m):
            if red_total + len(parts) - 1 <= N:
                RED_SIZES.append(parts)

    total = 0
    for red_sizes in RED_SIZES:
        reds = len(red_sizes)
        grays = N - sum(red_sizes)

        # how many ways to order the reds?
        red_orderings = multiset_orderings(red_sizes)

        # how many ways to distribute the grays?
        grays -= reds - 1     # put one gray between each adjacent red
        gray_distributions = math.comb(grays + reds, reds)

        total += red_orderings * gray_distributions

    return total + 1        # add 1 for all gray



for N in range(1000):
    if fill_count(N, 50) > 10**6:
        print(N)
        break

# => 168
