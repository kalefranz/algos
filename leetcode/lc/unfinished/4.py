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


def median(p1, a1, a2):
    LEN = len(a1) + len(a2)
    EVEN = LEN % 2 == 0
    PIVOT = LEN // 2
    if EVEN:
        PIVOT -= 1
    p2 = PIVOT - p1

    a1l, a1u = bounds(a1, p1)
    a2l, a2u = bounds(a2, p2)

    len_balance = (len(a1[:p1]) + len(a2[:p2])) - (len(a1[p1:]) + len(a2[p2:]))
    lower_max = max(a1l, a2l)
    upper_min = min(a1u, a2u)

    p12, lmum = f"{p1},{p2}", f"{lower_max},{upper_min}"
    lowers, uppers = f"({a1l},{a2l})", f"({a1u},{a2u})"
    return f"{p12:>8} {len_balance:>6} {lowers:>14} {uppers:>14} {lmum:>12}"


a12 = [0,1,2,3,8], [6,10,11,12]  # odd
# a12 = [0,0,0,0,1,2,3,8], [6,10,11,12,12,12,12]  # odd
# a12 = [1,2,5,5,5], [5,5,5,6,7,8]  # odd
ltot = len(a12[0]) + len(a12[1])
for q in range(-ltot, ltot):
    print(median(q, *a12))


class Solution:
    def findMedianSortedArrays(self, a1: List[int], a2: List[int]) -> float:
        def control_vals(piv):
            p1 = piv
            p2 = PIVOT - p1

            a1l, a1u = bounds(a1, p1)
            a2l, a2u = bounds(a2, p2)

            len_balance = (len(a1[:p1]) + len(a2[:p2])) - (len(a1[p1:]) + len(a2[p2:]))
            lower_max = max(a1l, a2l)
            upper_min = min(a1u, a2u)

            next_piv_dxn = "up" if a1l < a2l and a1u < a2u else "down"

            return len_balance, lower_max, upper_min, next_piv_dxn


        LTOT = len(a1) + len(a2)  # total length
        ODD = LTOT % 2  # even_odd
        PIVOT = LTOT // 2  # piv1 + piv2
        if not ODD:
            PIVOT -= 1

        pivot = int(LTOT / 4)
        len_balance, lower_max, upper_min, next_piv_dxn = control_vals(pivot)

        cnt = 0
        while abs(len_balance) > 1 or lower_max > upper_min:
            print(pivot, next_piv_dxn, abs(len_balance) > 1, lower_max > upper_min)
            cnt += 1
            if cnt > 12:
                print(f"FAILLLLLLLLL {cnt}")
                break
            if next_piv_dxn == "up":
                pivot = pivot + (LTOT - pivot) // 2
            else:
                pivot = pivot - pivot // 2
            len_balance, lower_max, upper_min, next_piv_dxn = control_vals(pivot)

        return -1


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (6, [0,1,2,3,8], [6,10,11,12]),  # odd LTOT
    (6, [0,0,0,0,1,2,3,8], [6,10,11,12,12,12,12]),  # odd LTOT
    (5, [1,2,5,5,5], [5,5,5,6,7,8]),  # odd LTOT
    (2.0, [1,3], [2]),
    (2.5, [1,2], [3,4]),
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
    sys.exit(test(0))
