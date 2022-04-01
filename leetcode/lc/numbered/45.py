"""
45. Jump Game II
Medium

Given an array of non-negative integers nums, you are initially positioned at the first index
of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

https://leetcode.com/problems/jump-game-ii/

"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = current_jump_end = farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (2, [2,3,1,1,4]),
    (2, [2,3,0,1,4]),
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
