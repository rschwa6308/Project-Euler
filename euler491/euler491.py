"""
Idea: divisibility by 11 can be determined via a sort of digital checksum with alternating sign

Therefore, we can count all relevant integers by examining:
 - the multiset of digits in even position (the "positives")
 - the multiset of digits in odd  position (the "negatives")
and then counting the number of valid (i.e. no leading zeros) integers that can be formed
from the pair of multisets
"""

from itertools import combinations
from math import factorial


DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 2
DIGITS.sort()



def orderings(multiset):
    repeats = len(multiset) - len(set(multiset))

    return factorial(len(multiset)) // 2**repeats



def possible_integers(positives, negatives):
    count = 0

    for head in set(positives):
        if head == 0: continue     # no leading zeros
        tail = list(positives)
        tail.remove(head)
        count += orderings(tail)

    count *= orderings(negatives)

    return count



count = 0
for positives in set(combinations(DIGITS, 10)):     # small enough to hold in memory :)
    negatives = list(DIGITS)
    for n in positives:
        negatives.remove(n)

    checksum = sum(positives) - sum(negatives)

    if checksum % 11 == 0:
        count += possible_integers(positives, negatives)

print(count)


# 194505988824000
