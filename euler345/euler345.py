M_str_small = """\
  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303\
"""

M_small = [
    [int(n) for n in row.split()]
    for row in M_str_small.splitlines()
]


M_str = """\
  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805\
"""

M = [
    [int(n) for n in row.split()]
    for row in M_str.splitlines()
]

from pprint import pprint
from random import sample, shuffle


def greedy(M):
    assert len(M) == len(M[0])

    nums = set()
    s = len(M)

    coords = [(x, y) for x in range(s) for y in range(s)]
    coords.sort(key=lambda c: M[c[1]][c[0]], reverse=True)

    xs = []
    ys = []
    for _ in range(s):
        for x, y in coords:
            if len(xs) == s: break
            if x not in xs and y not in ys:
                xs.append(x)
                ys.append(y)

    pprint(list(zip(xs, ys)))
    return sum(M[y][x] for x, y in zip(xs, ys))



from itertools import combinations


def iterative_swapping(M, randomize=False):
    s = len(M)

    xs = list(range(s))
    ys = list(range(s))

    if randomize:
        shuffle(xs)

    def get(x, y):
        return M[y][x]

    converged = False
    while not converged:
        converged = True

        for i, j in combinations(range(s), 2):
            if get(xs[i], ys[i]) + get(xs[j], ys[j]) < get(xs[j], ys[i]) + get(xs[i], ys[j]):
                xs[i], xs[j] = xs[j], xs[i]
                converged = False

        
    return sum(M[y][x] for x, y in zip(xs, ys))



def iterative_swapping_retry(M, num_attempts=100):
    return max(iterative_swapping(M, randomize=True) for _ in range(num_attempts))



assert iterative_swapping_retry(M_small) == 3315

print(iterative_swapping_retry(M))
# 13938