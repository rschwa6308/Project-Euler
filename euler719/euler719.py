from math import sqrt
from tqdm import tqdm


def split_sum_exists(digits: str, target: int):
    """
    Determine if there exists a 'split' of `digits` into a sequence of base-10 numbers which sum to `target`.

     - `split_sum_exists("1234", 46) => True` `(12 + 34 = 46)`
     - `split_sum_exists("1234", 127) => True` `(123 + 4 = 127)`
     - `split_sum_exists("1234", 28) => True` `(1 + 23 + 4 = 28)`
     - `split_sum_exists("1234", 80) => False`
    """

    # early rejection cases
    if int(digits) < target:
        return False

    # base case
    if int(digits) == target:
        return True

    # recursive case
    for i in range(1, len(digits)):
        head = digits[:i]
        tail = digits[i:]
        if split_sum_exists(tail, target - int(head)):
            return True
    
    return False



def is_S_number(n):
    n_sqrt = int(sqrt(n))

    if n_sqrt**2 != n:
        return False

    return split_sum_exists(str(n), n_sqrt)



def T(N):
    total = 0
    for k in tqdm(range(2, int(sqrt(N))+1)):        # (exclude 1)
        n = k**2

        if is_S_number(n):
            total += n
            # print(n)

    return total


assert(split_sum_exists("4", 4))
assert(split_sum_exists("81", 9))
assert(split_sum_exists("6724", 82))
assert(not split_sum_exists("6725", 82))
assert(split_sum_exists("8281", 91))
assert(split_sum_exists("9801", 99))

assert(T(1e4) == 41333)


if __name__ == "__main__":
    print(T(1e12))

    # 128088830547982
