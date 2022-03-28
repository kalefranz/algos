"""
746. Min Cost Climbing Stairs
Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

"""
from collections import deque
from typing import *

class Solution:
        def minCostClimbingStairs(self, cost: List[int]) -> int:
            return



TEST_CALL = Solution().minCostClimbingStairs
CASES = (
    ## expected, *input_args
    (3, [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]),
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

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

