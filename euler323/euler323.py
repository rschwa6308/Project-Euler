import numpy as np
import scipy.stats

def expected_iters_until_all_on(n: int) -> float:
    T = np.zeros(n + 1)     # T[k] = expected days starting with k bits on
    T[n] = 0                # base case: all bits are on

    # fill out table from back to front
    for num_on in range(n-1, -1, -1):
        num_off = n - num_on

        expected = 0.0

        # cost for this iteration
        expected += 1.0

        # expected cost for future iterations
        probs = scipy.stats.binom.pmf(np.arange(0, num_off + 1), num_off, 0.5)
        for num_on_new in range(1, num_off + 1):
            expected += probs[num_on_new] * T[num_on + num_on_new]

        # recurrence solution accounting for chance we stay in the same state (i.e. 0 new bits turn on)
        T[num_on] = expected / (1 - probs[0])

    return T[0]

result = expected_iters_until_all_on(32)
print(round(result, 10))
