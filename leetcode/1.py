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
