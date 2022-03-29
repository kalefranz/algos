"""
746. Min Cost Climbing Stairs
Easy

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once
you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

https://leetcode.com/problems/min-cost-climbing-stairs/

"""
from collections import deque
from functools import cache
from typing import *


class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        minimum_costs = [0] * (len(costs) + 1)
        for q in range(2, len(costs) + 1):
            take_one_step = costs[q-1] + minimum_costs[q-1]
            take_two_steps = costs[q-2] + minimum_costs[q-2]
            minimum_costs[q] = min(take_one_step, take_two_steps)
        return minimum_costs[-1]

    def minCostClimbingStair_1(self, costs: List[int]) -> int:
        calculator = self.generate_cost_calculator(costs)
        r = calculator(0)
        return r

    @staticmethod
    def generate_cost_calculator(costs):
        COSTS = costs
        cache = {}

        def _calc(start_step):
            if start_step in cache:
                return cache[start_step]
            costs_slice = COSTS[start_step:]
            if len(costs_slice) == 1:
                rslt = costs_slice[0]
            elif len(costs_slice) == 2:
                rslt = min(costs_slice)
            elif len(costs_slice) == 3:
                start_0 = costs_slice[0] + _calc(start_step+1)
                start_1 = costs_slice[1]
                rslt = min(start_0, start_1)
            else:
                start_0 = costs_slice[0] + _calc(start_step+1)
                start_1 = costs_slice[1] + _calc(start_step+2)
                rslt = min(start_0, start_1)
            cache[start_step] = rslt
            return rslt
        _calc.cache = cache
        return _calc


TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
# TEST_CALL = Solution().minCostClimbingStairs
CASES = (
    # ## expected, *input_args
    (15, [10,15,20]),
    (6, [1,100,1,1,1,100,1,1,100,1]),
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

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())
