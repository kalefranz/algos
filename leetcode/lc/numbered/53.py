"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum.

A subarray is a contiguous part of an array.

https://leetcode.com/problems/maximum-subarray/
"""
from collections import deque
from itertools import accumulate
import math
from operator import itemgetter
import os.path
from typing import *

from lc.numbered import load_json


class Solution:

    def maxSubArray_divide_and_conq(self, nums: List[int]) -> int:
        def best_subarray(left, right):
            if left >= right:
                return -math.inf
            mid = (right - left) // 2 + left

            best_left_sum = max(accumulate(reversed(nums[left:mid])), default=0)
            best_right_sum = max(accumulate(nums[mid+1:right]), default=0)
            best_combined_sum = max(best_left_sum, 0) + nums[mid] + max(best_right_sum, 0)

            left_half = best_subarray(left, mid)
            right_half = best_subarray(mid+1, right)

            return max(left_half, best_combined_sum, right_half)
        return best_subarray(0, len(nums))

    def maxSubArray_divide_and_conq_1(self, nums: List[int]) -> int:
        def best_subarray(left, right):
            if left >= right:
                return -math.inf
            mid = (right - left) // 2 + left

            curr = best_left_sum = 0
            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            curr = best_right_sum = 0
            for i in range(mid+1, right):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            best_combined_sum = best_left_sum + nums[mid] + best_right_sum

            left_half = best_subarray(left, mid)
            right_half = best_subarray(mid+1, right)

            return max(left_half, best_combined_sum, right_half)
        return best_subarray(0, len(nums))

    def maxSubArray_dynamic_programming(self, nums: List[int]) -> int:
        curr_sub = max_sub = nums[0]
        for n in nums[1:]:
            curr_sub = max(n, curr_sub + n)
            max_sub = max(max_sub, curr_sub)
        return max_sub


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (6, [-2,1,-3,4,-1,2,1,-5,4]),
    (1, [1]),
    (23, [5,4,-1,7,8]),
    (1, [-2,1]),
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
