from math import ceil

def search(nums, target):
    left, right = 0, len(nums)
    while left < right:
        test = (right - left) // 2 + left
        if target == nums[test]:
            return test
        elif target < nums[test]:
            right = test
        else:
            left = test + 1
    return -1


x = [-1,0,3,5,9,12]
for y in x:
    print(search(x, y))
print(search(x, 4))
print(search(x, 2))
print(search([1], 1))
print(search([1], 0))
print(search([], 1))

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

