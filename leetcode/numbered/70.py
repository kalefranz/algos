"""
70. Climbing Stairs
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""
from collections import deque
from functools import cache
from typing import *

class Solution:

    @cache
    def climbStairs1(self, n: int) -> int:
        if n <= 3:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n: int) -> int:
        ans = [0,1,2,3]
        for q in range(4, n+1):
            ans.append(ans[q-1] + ans[q-2])
        return ans[n]


# 0, 0
# 1, 1
# 2, 2
# 3, 3
# 4, 5 [1,1,1,1],[1,1,2],[1,2,1],[2,1,1],[2,2]
# 5, 8  [1,1,1,1,1],[1,1,1,2],[1,1,2,1],[1,2,1,1][2,1,1,1],[1,2,2],[2,1,2],[2,2,1]
# apparently this is just fib /shrugz/


TEST_CALL = Solution().climbStairs
CASES = (
    ## expected, *input_args
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (5, 4),
    (8, 5),
    (13, 6),
    (21, 7),
    (34, 8),
    (55, 9),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        result = TEST_CALL(*input_args)
        if result == expected:
            print(f"{q}: passed")
        else:
            print(f"{q}: FAILED")
            print(f"  {expected} != {result}")
            failed += 1
    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")
test()
