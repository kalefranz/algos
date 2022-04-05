"""
4. Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

https://leetcode.com/problems/median-of-two-sorted-arrays/

"""
from collections import deque
from math import inf
import os.path
from typing import *

from lc.numbered import load_json


def bounds(arry, pivot):
    if 1 <= pivot <= len(arry) - 1:
        lower_val, upper_val = arry[pivot - 1], arry[pivot]
    elif pivot == 0:
        lower_val, upper_val = -inf, arry[pivot]
    elif pivot < 0:
        lower_val, upper_val = -inf, -inf
    elif pivot == len(arry):
        lower_val, upper_val = arry[pivot - 1], inf
    elif pivot > len(arry):
        lower_val, upper_val = inf, inf
    else:
        raise NotImplementedError()
    return lower_val, upper_val


def median(arry):
    if len(arry) == 1:
        return arry[0]
    if len(arry) % 2 == 0:
        p = len(arry) // 2
        return (arry[p-1] + arry[p]) / 2
    else:
        p = len(arry) // 2
        return arry[p]


class Solution:
    def findMedianSortedArrays(self, a1: List[int], a2: List[int]) -> float:
        def control_vals(piv):
            p1 = piv
            p2 = PIVOT - p1
            if not ODD:
                p2 += 1

            a1l, a1u = bounds(a1, p1)
            a2l, a2u = bounds(a2, p2)

            len_balance = (len(a1[:p1]) + len(a2[:p2])) - (len(a1[p1:]) + len(a2[p2:]))
            lower_max = max(a1l, a2l)
            upper_min = min(a1u, a2u)

            next_piv_dxn = "up" if a1l < a2l and a1u < a2u else "down"

            return len_balance, lower_max, upper_min, next_piv_dxn

        LTOT = len(a1) + len(a2)  # total length
        if len(a1) == 0:
            from statistics import median
            return median(a2)
        if len(a2) == 0:
            from statistics import median
            return median(a1)
        ODD = LTOT % 2  # even_odd
        PIVOT = LTOT // 2  # piv1 + piv2
        if ODD:
            LEN_BALANCE = 1
        else:
            PIVOT -= 1
            LEN_BALANCE = 2

        pivot = int(LTOT / 4)
        len_balance, lower_max, upper_min, next_piv_dxn = control_vals(pivot)

        cnt = 0
        while abs(len_balance) > LEN_BALANCE or lower_max > upper_min:
            # print(pivot, next_piv_dxn, len_balance, lower_max > upper_min)
            cnt += 1
            if next_piv_dxn == "up":
                # pivot = pivot + (LTOT - pivot) // 2
                pivot += 1
            else:
                # pivot = pivot - pivot // 2
                pivot -= 1
            len_balance, lower_max, upper_min, next_piv_dxn = control_vals(pivot)

        return upper_min if ODD else (upper_min + lower_max) / 2


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (6, [0,1,2,3,8], [6,10,11,12]),  # odd LTOT
    (6, [0,0,0,0,1,2,3,8], [6,10,11,12,12,12,12]),  # odd LTOT
    (5, [1,2,5,5,5], [5,5,5,6,7,8]),  # odd LTOT
    (2.0, [1,3], [2]),  # odd LTOT
    (2.5, [1,2], [3,4]),  # even LTOT
    (7.0, [0,0,0,1,2,3,8], [6,10,11,12,12,12,12]),  # even LTOT
    (1, [1], []),
    (1, [], [1]),
    (2.5, [], [2,3])
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
