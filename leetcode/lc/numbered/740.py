"""
740. Delete and Earn
Medium

You are given an integer array nums. You want to maximize the number of points you get by
performing the following operation any number of times:

    Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every
    element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number
of times.

https://leetcode.com/problems/delete-and-earn/

"""
from collections import defaultdict, deque
from functools import cache, partial, reduce
from operator import getitem
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(lambda: 0)
        for n in nums:
            points[n] += n

        @cache
        def max_points(n):
            if n == 0:
                return 0
            if n == 1:
                return points[1]
            return max(max_points(n-1), points[n] + max_points(n-2))

        return max_points(max(points.keys()))

    def deleteAndEarn_1(self, nums: List[int]) -> int:
        vmap = defaultdict(lambda: 0)
        for n in nums:
            vmap[n] += n

        groups = []
        def apply(x, y):
            if y - x == 1:
                groups[-1].add(y)
            else:
                groups.append({y})
            return y
        reduce(apply, sorted(vmap.keys()), -5)
        # print(groups)

        def earn(remaining: AbstractSet):
            if not remaining:
                return 0
            if len(remaining) == 1:
                return vmap[next(iter(remaining))]
            n = max(remaining, key=partial(getitem, vmap))
            branches = {n-1, n, n+1} & remaining
            # print(n, len(remaining), remaining)
            return max(vmap[b] + earn(remaining - {b-1, b, b+1}) for b in branches)
            # return vmap[n] + earn(remaining - {n-1, n, n+1})

        # print(list(sorted(vmap.keys())))
        # return earn(vmap.keys())

        # for group in groups:
        #     print(earn(group))
        return sum(earn(group) for group in groups)




data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (6, [3,4,2]),
    (9, [2,2,3,3,3,4]),
    (3451, data["nums2"]),
    (1, [1]),
    (61, [8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]),
    (14251, data["nums5"]),
)
TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
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
