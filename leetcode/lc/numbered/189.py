from typing import *


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        i = 0
        nxt = None
        while i < len(nums):
            x = (i + k) % len(nums)
            nxt = nums[x]
            nums[x] = nums[i]
            i = x



def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a

    lng = len(nums)
    k %= lng
    iterations = gcd(lng, k)
    jumps_per_iteration = lng // iterations
    for i in range(iterations):
        prev = i
        prev_save = nums[prev]
        for _ in range(jumps_per_iteration):
            this = (prev + k) % lng
            save_this = nums[this]
            nums[this] = prev_save

            prev = this
            prev_save = save_this






def rotate2(nums, k):
    nums[:] = nums[-k:] + nums[:-k]


def make_test(n, k):
    nums = list(range(n))
    expected = nums[-k:] + nums[:-k]
    error = rotate(nums, k)
    if error:
        print("GCD:", gcd(error[0], error[1]))
        print("ERROR: [%s,%s,%s]" % error)
        return 1
    else:
        return 0
    # if nums != expect:
    #     print("ERROR: [%s,%s]   %s != %s" % (len(nums), k, nums, expect))
    #     return 1
    # else:
    #     # print("CORRECT: [%s]   %s" % (k, nums,))
    #     return 0



def run_tests(n):
    errors = 0
    for q in range(n+1):
        errors += make_test(n,q)
    # if errors:
    #     print("TOTAL ERRORS for range test @ [%s]: %s" % (n, errors))
    return errors


def run_tests_2():
    for xx in range(5,30,2):
        run_tests(xx)
    for xx in range(6,30,2):
        run_tests(xx)
run_tests_2()

# run_tests(8)
# run_tests(9)
# # run_tests(54)
# make_test(54,6)

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

