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
