"""

Given an array of integers nums, sort the array in ascending order.

https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/

"""
from collections import deque
from typing import *




class Solution:
    def sortArray1(self, nums: List[int]) -> List[int]:
        def merge(vec1, vec2):
            while vec1 and vec2:
                if vec1[0] < vec2[0]:
                    yield vec1.pop(0)
                else:
                    yield vec2.pop(0)
            while vec1:
                yield vec1.pop(0)
            while vec2:
                yield vec2.pop(0)

        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        a, b = nums[:mid], nums[mid:]
        return list(merge(self.sortArray1(a), self.sortArray1(b)))

    def sortArray(self, nums: List[int]) -> List[int]:
        return list(reversed(self._sortArray(nums)))

    def _sortArray(self, nums: List[int]) -> List[int]:
        def merge(vec1, vec2):
            while vec1 and vec2:
                if vec1[-1] > vec2[-1]:
                    yield vec1.pop()
                else:
                    yield vec2.pop()
            while vec1:
                yield vec1.pop()
            while vec2:
                yield vec2.pop()

        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        a, b = nums[:mid], nums[mid:]
        return list(merge(self.sortArray(a), self.sortArray(b)))

TEST_CALL = Solution().sortArray
CASES = (
    # ## expected, *input_args
    ([1,2,3,5], [5,2,3,1]),
    ([0,0,1,1,2,5], [5,1,1,2,0,0]),
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
