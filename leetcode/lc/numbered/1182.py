"""
1182. Shortest Distance to Target Color
Medium

You are given an array colors, in which there are three colors: 1, 2 and 3.

You are also given some queries. Each query consists of two integers i and c, return the shortest distance between the given index i and the target color c. If there is no solution return -1.

https://leetcode.com/problems/shortest-distance-to-target-color/

"""
from bisect import bisect
from collections import defaultdict, deque
from itertools import groupby
import json
from typing import *


def find_nearest(nums, val):
    # ex: [4, 7, 8], 1
    lnums = len(nums)
    if lnums == 0:
        return -1
    if lnums == 1:
        return nums[0]

    i, j = 0, lnums - 1
    if nums[i] >= val:
        return nums[i]
    if nums[j] <= val:
        return nums[j]

    while j - i > 1:
        mid = (j - i) // 2 + i
        if nums[mid] == val:
            return nums[mid]
        elif val > nums[mid]:
            i = mid
        else:
            j = mid

    if val - nums[i] < nums[j] - val:
        return nums[i]
    else:
        return nums[j]


class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        return self.shortestDistanceColor_python2(colors, queries)

    def shortestDistanceColor_algo(self, colors: List[int], queries: List[List[int]]):
        color_map = {}
        for q, color in enumerate(colors):
            color_map.setdefault(color, []).append(q)

        results = []
        for idx, color in queries:
            positions = color_map.get(color, ())
            n = find_nearest(positions, idx)
            steps = abs(n - idx) if n >= 0 else n
            results.append(steps)

        return results

    def shortestDistanceColor_python1(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        def steps_to_nearest(nums, val):
            if not nums:
                return -1
            for q in range(1, len(nums)):
                if abs(nums[q - 1] - val) < abs(nums[q] - val):
                    return abs(nums[q - 1] - val)
            else:
                return abs(nums[-1] - val)

        colormap = {1: [], 2: [], 3: []}
        any(colormap[color].append(q) for q, color in enumerate(colors))  # populate colormap
        return [
            # min((abs(idx - x) for x in colormap.get(color, ())), default=-1)
            steps_to_nearest(colormap.get(color, ()), idx)
            for idx, color in queries
        ]

    def shortestDistanceColor_python2(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        def steps_to_nearest(nums, val):
            if not nums:
                return -1
            if val <= nums[0]:
                return nums[0] - val
            x = bisect(nums, val)
            if x >= len(nums):
                return val - nums[-1]
            return min(val - nums[x-1], nums[x] - val)

        colormap = {1: [], 2: [], 3: []}
        any(colormap[color].append(q) for q, color in enumerate(colors))  # populate colormap
        return [
            steps_to_nearest(colormap.get(color, ()), idx)
            for idx, color in queries
        ]





TEST_CALL = Solution().shortestDistanceColor
try:
    data = json.load(open(__file__[:-3] + ".json"))
except FileNotFoundError:
    data = {}
CASES = (
    # ## expected, *input_args
    ([3], [1,1,2,1,3,2,2,3,3], [[1,3]]),
    ([3,0,3], [1,1,2,1,3,2,2,3,3], [[1,3],[2,2],[6,1]]),
    ([-1], [1,2], [[0,3]]),
    (data["result3"], data["colors3"], data["queries3"])
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

if __name__ == "__main__":
    test()
