"""
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same
element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/

"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {target - nums[0]: 0}
        for i in range(1, len(nums)):
            if nums[i] in store:
                return [store[nums[i]], i]
            store[target - nums[i]] = i
        return [-1,-1]


TEST_CALL = Solution().twoSum
CASES = (
    # ## expected, *input_args
    ([0,1], [2,7,11,15], 9),
    ([1,2], [3,2,4], 6),
    ([0,1], [3,3], 6),
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
