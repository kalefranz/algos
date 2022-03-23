"""
410. Split Array Largest Sum
Hard

Given an array nums which consists of non-negative integers and an integer k, you can split the array into k non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these k subarrays.

"""
from collections import deque
from functools import reduce
from math import copysign
from typing import *


def get_Y(nums, x):
    segments = [0]
    for num in nums:
        if segments[-1] + num <= x:
            segments[-1] += num
        else:
            segments.append(num)
    return len(segments)


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 39 != [
        #   (25, 6), (26, 6), (27, 5), (28, 5), (29, 5), (30, 5), (31, 5),
        #   (32, 4), (33, 4), (34, 4), (35, 4), (36, 4), (37, 4), (38, 4),
        #   (39, 3), (40, 3), (41, 3), (42, 3), (43, 3), (44, 3)
        # ]
        results = []
        print(f"TARGET = {k} segments")

        Ym = Yn = int(1e3)
        Xm, Xn = 0, max(len(nums), sum(nums))

        results = [None] * (Xn + 1)
        results[Xm] = Ym
        r2 = [(Xm, Ym)]

        cnt = 0
        while 1:
            cnt += 1

            Ym = Yn
            Yn = get_Y(nums, Xn)
            results[Xn] = Yn
            r2.append((Xn, Yn))

            # of the last two results, sort pairs (X,Y) pairs in order of increasing X

            assert 1


            if (Xm - Xn == -1 and Ym == k + 1 and Yn == k):
                print()
                print(cnt, f"[({Xm},{Ym}),({Xn},{Yn})]", "..".join(f"{i}:{v}" for i, v in enumerate(results) if v is not None))
                return Xn
            # elif (Ym == k and Yn == k + 1 and Xm - Xn == 1):
            #     print()
            #     print(cnt, f"[({Xm},{Ym}),({Xn},{Yn})]", "..".join(f"{i}:{v}" for i, v in enumerate(results) if v is not None))
            #     return Xm
            elif cnt > 14:
                print()
                print(cnt, Xn, "..".join(f"{i}:{v}" for i, v in enumerate(results) if v is not None))
                return None

            # if segments > k + 1, then decrease X
            # if segments < k + 1, then increase X
            # [(0, 1000), (111, 1), (55, 3), (83, 2)]
            # if k=2, then looking for the 3->2 transition in where Ym==3,Yn==2 and => X=>q
                # if k=3, then looking for the 4->3 transition in where Ym==4,Yn==3 and => X=>q
            # the first X where Y==2

            # for k=3    looking for (Ym,Yn) == (4, 3) when Xm-Xn == -1
            # q=1: Xm < Xn  &&  Ym > 4, Yn < 3  => # Xnext needs to be smaller
            #      0    111    1000      1
            # q=2: Xm > Xn  &&  Ym < 4, Yn ==3
            #      111  56       1      3

            # if Ym > k+1, definitely move right
            # if Ym < k+1, definitely move left
            # if Yn > k, definitely move right
            # if Ym < k, definintely move left
            #   eventually need to have Xnext == Xn+1




            # if Ym > k+1 and Yn > k and cnt > 1:
            #     # larger Xnext
            #     Xnext = Xn + max(abs(Xm - Xn) // 2, 1)
            # else:
            #     # smaller Xnext
            #     Xnext = Xn - max(abs(Xn - Xm) // 2, 1)

            # if Ym < k+1, then must have smaller Xnext
            # if Yn < k, then must have smaller Xnext
            if Ym < k + 1 and Yn < k:
                # must have smaller Xnext ???
                Xnext = Xn - max(abs(Xn - Xm) // 2, 1)
            # probably some more elif conditions
            else:
                # larger Xnext
                Xnext = Xn + max(abs(Xm - Xn) // 2, 1)
                Xnext = Xnext


            should_be = [None, -1, -1, 1, 1]
            delta = Xnext - Xn
            assert copysign(1, delta) == should_be[cnt], (cnt, Xnext, Xn, delta)


            # # y = slope * x + b
            # slope = (Yn - Ym) / (Xn - Xm)
            # if slope > -1 or cnt <= 1:
            #     # smaller Xnext
            #     Xnext = Xn - max(abs(Xn - Xm) // 2, 1)
            # else:
            #     # larger Xnext
            #     Xnext = Xn + max(abs(Xm - Xn) // 2, 1)

            # if (Xm - Xn) == -1 and  Ym > Yn and Yn <= k + 1:  # Ym <= k + 1
            #     # smaller Xn
            #     Xnext = Xn - max(abs(Xn - Xm) // 2, 1)
            # else:
            #     # bigger Xn
            #     assert cnt != 1
            #     Xnext = Xn + max(abs(Xm - Xn) // 2, 1)

            assert Xnext != Xn

            Xm = Xn
            Xn = Xnext

        assert 0


    def splitArray1(self, nums: List[int], k: int) -> int:
        assert k == 2, k
        lng = len(nums)
        last_diff = last_mx = None

        mid = lng // 2
        left, right = sum(nums[:mid]), sum(nums[mid:])
        diff, mx = right - left, max(left, right)
        while last_diff is None or abs(last_diff) > abs(diff):
            if diff == 0:
                break
            elif diff > 0:  # move right
                mid = ((lng-mid) // 2) + mid
            else:  # move left
                mid = ((lng-mid) // 2)
            last_diff, last_mx = diff, mx
            left, right = sum(nums[:mid]), sum(nums[mid:])
            diff, mx = right - left, max(left, right)
        return last_mx


TEST_CALL = Solution().splitArray
CASES = (
    ## expected, *input_args
    (18, [7,2,5,10,8], 2),
    (9, [1,2,3,4,5], 2),
    (4, [1,4,4], 3),
    (59, [7,8,12,10,8,14,2,5,10,8,10,8,7,2], 2),
    (39, [7,8,12,10,8,14,2,5,10,8,10,8,7,2], 3),
    (32, [7,8,12,10,8,14,2,5,10,8,10,8,7,2], 4),
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
test(4)
