"""
35. Search Insert Position
Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""

def searchInsert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (right - left) // 2 + left
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left

x = [1,3,5,6]
for y in range(10):
    print(y, searchInsert(x, y))

# print(searchInsert(x, 2))
