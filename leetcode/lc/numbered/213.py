"""
213. House Robber II
Medium

You are a professional robber planning to rob houses along a street. Each house has a certain
amount of money stashed. All houses at this place are arranged in a circle. That means the first
house is the neighbor of the last one. Meanwhile, adjacent houses have a security system
connected, and it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

https://leetcode.com/problems/house-robber-ii/

"""
from collections import deque
from functools import cache
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)

        cache = {}

        def rob_simple(start, end):
            ckey = start, end
            if (_v := cache.get(ckey)) is not None:
                return _v
            if end - start <= 0:
                cache[ckey] = _v = 0
                return _v
            elif end - start == 1:
                cache[ckey] = _v = nums[start]
                return _v
            start_0 = nums[start] + rob_simple(start + 2, end)
            start_1 = nums[start + 1] + rob_simple(start + 3, end)
            cache[ckey] = _v = max(start_0, start_1)
            return _v

        return max(rob_simple(0, len(nums)-1), rob_simple(1, len(nums)))

    def rob_2(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)

        @cache
        def rob_simple(start, end):
            arry = nums[start:end]
            if len(arry) == 0:
                return 0
            elif len(arry) == 1:
                return arry[0]
            start_0 = nums[start] + rob_simple(start + 2, end)
            start_1 = nums[start + 1] + rob_simple(start + 3, end)
            return max(start_0, start_1)

        return max(rob_simple(0, len(nums)-1), rob_simple(1, len(nums)))

    def rob_1(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)

        @cache
        def rob_simple(arry):
            if len(arry) == 0:
                return 0
            elif len(arry) == 1:
                return arry[0]
            start_0 = arry[0] + rob_simple(arry[2:])
            start_1 = arry[1] + rob_simple(arry[3:])
            return max(start_0, start_1)

        nums = tuple(nums)
        return max(rob_simple(nums[:-1]), rob_simple(nums[1:]))


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (3, [2,3,2]),
    (4, [1,2,3,1]),
    (3, [1,2,3]),
    (27, [6,6,4,8,4,3,3,10]),
    (3, [2,1,1,2]),
    (1, [1]),
    (4388, data["nums6"]),
)
TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
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
