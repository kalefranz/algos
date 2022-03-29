"""
198. House Robber
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed, the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected and it will automatically contact the police if
two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

https://leetcode.com/problems/house-robber/
"""
from collections import deque
from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        sums = [0] * len(nums)
        sums[0], sums[1] = nums[0], max(nums[:2])
        for q in range(2, len(nums)):
            take_this_and_two_back = nums[q] + sums[q-2]
            take_prev = sums[q-1]
            sums[q] = max(take_this_and_two_back, take_prev)
        return max(sums[-2:])


TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
CASES = (
    # ## expected, *input_args
    (4, [1,2,3,1]),
    (12, [2,7,9,3,1]),
    (0, [0]),
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
