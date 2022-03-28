from collections import Counter
from random import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        def cumsum(xs):
            tot = 0
            for x in xs:
                tot += x
                yield tot

        self.cumsums = tuple(cumsum(w))
        self.total = self.cumsums[-1]

    def pickIndex(self) -> int:
        target = random() * self.total
        low, high = 0, len(self.cumsums)
        while low < high:
            mid = (high - low) // 2 + low
            if self.cumsums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

s = Solution([0,1,3,0])
iters = 5000
c = Counter([s.pickIndex() for _ in range(iters)])
print([(q, c[q]/iters) for q in sorted(c)])

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

