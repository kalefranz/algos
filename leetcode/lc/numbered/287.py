"""
287. Find the Duplicate Number
Medium

Given an array of integers nums containing n + 1 integers where each integer is in the range
[1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

https://leetcode.com/problems/find-the-duplicate-number/


"""
from collections import deque, Counter
from typing import *


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return self.findDuplicate_toggle(nums)

    def findDuplicate_counter(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]

    def findDuplicate_toggle(self, nums: List[int]) -> int:
        def get_first_dup(nums):
            store = prev = 0
            for num in nums:
                store ^= (1 << num)
                if prev > store:
                    return num
                prev = store
            return -1
        return get_first_dup(nums)

    def findDuplicate_bitmask(self, nums: List[int]) -> int:
        def get_first_dup(nums):
            store = 0
            for num in nums:
                if (store >> num) & 1:
                    return num
                else:
                    store |= (1 << num)
            return -1
        return get_first_dup(nums)


TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
CASES = (
    # ## expected, *input_args
    (2, [1,3,4,2,2]),
    (3, [3,1,3,4,2]),
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
