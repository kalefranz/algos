"""
35. Search Insert Position
Easy

Given a sorted array of distinct integers and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

https://leetcode.com/problems/search-insert-position/

"""
from collections import deque
from typing import *
from bisect import bisect_left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.searchInsert_1(nums, target)

    def searchInsert_2(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)

    def searchInsert_1(self, nums: List[int], target: int) -> int:
        left, right, mid = 0, len(nums) - 1, None
        while left <= right:
            mid = (right - left) // 2 + left
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left


TEST_CALL = Solution().searchInsert
CASES = (
    # ## expected, *input_args
    (2, [1,3,5,6], 5),
    (1, [1,3,5,6], 2),
    (4, [1,3,5,6], 7),
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
