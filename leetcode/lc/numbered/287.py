"""
287. Find the Duplicate Number
Medium

### Duplicate of 1905 ###

Given an array of integers nums containing n + 1 integers where each integer is in the range
[1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

https://leetcode.com/problems/find-the-duplicate-number/

"""
from importlib import import_module

p1905 = import_module("lc.numbered.1905")
test = p1905.test

if __name__ == "__main__":
    import sys
    sys.exit(test())
