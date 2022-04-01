"""
55. Jump Game
Medium

You are given an integer array nums. You are initially positioned at the array's first index, and
each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

https://leetcode.com/problems/jump-game/
"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for j in range(len(nums)-1, -1, -1):
            if j + nums[j] >= last:
                last = j
        return last == 0

    def canJump_1(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = list(reversed(nums))
        pos_or_0 = lambda x: x if x >= 0 else 0

        for q in range(len(nums)):
            k = nums[q]
            first, last = pos_or_0(q-k+1), q+1
            nums[first:last] = [True] * (last - first)

        return all(nums[1:])


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (True, [2,3,1,1,4]),
    (False, [3,2,1,0,4]),
    (True, [1]),
    (True, [0]),
    (False, [0,1]),
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
