"""
763. Partition Labels
Medium

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {target - nums[0]: 0}
        for x in range(1, len(nums)):
            if nums[x] in store:
                return store[nums[x]], x
            store[target - nums[x]] = x
        return None

print(Solution().twoSum([2,7,11,15], 9))

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

