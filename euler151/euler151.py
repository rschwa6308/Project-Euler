import array
from copy import deepcopy
from dataclasses import dataclass
from functools import lru_cache
import random

from tqdm import tqdm


@dataclass
class Envelope:
    counts: list[int]

    def num_sheets_total(self) -> int:
        return sum(self.counts)

    def num_sheets_of_size(self, n) -> int:
        return self.counts[n]

    def draw(self, n):
        assert self.num_sheets_of_size(n) > 0

        # remove drawn sheet
        self.counts[n] -= 1

        # add back in children sheets (exlcuding the consumed A5)
        for m in range(n):
            self.counts[m] += 1
    
    def __hash__(self):
        return hash(tuple(self.counts))


@lru_cache(maxsize=10_000)
def expected_num_singles(envelope: Envelope):
    # print(f"expected_num_singles({envelope})")

    if envelope.num_sheets_total() == 0:
        return 0

    val = 0

    if envelope.num_sheets_total() == 1:
        val += 1

    for n in range(5):
        num = envelope.num_sheets_of_size(n)
        if num == 0: continue

        prob = num / envelope.num_sheets_total()
        envelope_new = deepcopy(envelope)
        envelope_new.draw(n)        # in-place

        val += prob * expected_num_singles(envelope_new)

    return val



if __name__ == "__main__":
    E = expected_num_singles(Envelope([0, 0, 0, 0, 1]))
    E -= 2  # exclude first and last batch
    print(round(E, 6))
