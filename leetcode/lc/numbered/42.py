"""
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

https://leetcode.com/problems/trapping-rain-water/

"""
from collections import deque
from itertools import accumulate
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def trap_two_pointer(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        total = left_max = right_max = 0
        while left < right:
            if heights[left] < heights[right]:
                if heights[left] > left_max:
                    left_max = heights[left]
                else:
                    total += left_max - heights[left]
                left += 1
            else:
                if heights[right] > right_max:
                    right_max = heights[right]
                else:
                    total += right_max - heights[right]
                right -= 1
        return total

    def trap_stack(self, heights: List[int]) -> int:
        stack = []
        total = 0
        for q in range(len(heights)):
            while stack and heights[q] > heights[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = q - stack[-1] - 1
                bounded_height = min(heights[stack[-1]], heights[q]) - heights[top]
                total += distance * bounded_height
            stack.append(q)
        return total

    def trap_dynamic_programming(self, heights: List[int]) -> int:
        reverse_maxes: List[int] = list(accumulate(reversed(heights), func=max))
        prev_l_max = 0
        total = 0
        for q in range(0, len(heights)):
            prev_l_max = max(prev_l_max, heights[q])
            this_height = min(prev_l_max, reverse_maxes[len(heights)-1-q])
            total += this_height - heights[q]
        return total



data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (6, [0,1,0,2,1,0,1,3,2,1,2,1]),
    (9, [4,2,0,3,2,5]),
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
