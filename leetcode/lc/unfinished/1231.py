"""
1231. Divide Chocolate
Hard

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given
by the array sweetness.

You want to share the chocolate with your k friends so you start cutting the chocolate bar into
k + 1 pieces using k cuts, each piece consists of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces
to your friends.

Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

https://leetcode.com/problems/divide-chocolate/

"""
from collections import deque
from math import ceil, floor
from typing import *


# def calculate_segments(nums, cutoff):
#     segment_values = [0]
#     for q, swt in enumerate(nums):
#         if segment_values[-1] + swt <= cutoff:
#             segment_values[-1] += swt
#         else:
#             segment_values.append(swt)
#     num_segments, min_segment_val, max_segment_val = len(segment_values), min(segment_values), max(segment_values)
#     return num_segments, min_segment_val, max_segment_val


class Helper:
    _last = None

    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

        self.bounds = {}  # Dict[num_segs, (min_cutoff, max_cutoff)]
        self.cutoffs = {}  # Dict[cutoff, num_segs]
        self.cutoff_path = []

        self.prev_point = ()
        self.__class__._last = self

    def add_cutoff(self, cutoff):
        num_segments = self._calculate_segments(cutoff)
        self._add_point(num_segments, cutoff)
        return num_segments

    def _calculate_segments(self, cutoff):
        segment_values = [0]
        for q, swt in enumerate(self.nums):
            if segment_values[-1] + swt <= cutoff:
                segment_values[-1] += swt
            else:
                segment_values.append(swt)
        for _ in range(segment_values.count(0)):
            segment_values.remove(0)
        num_segments = len(segment_values)
        return num_segments

    def _add_point(self, num_segments, cutoff):
        # segments: (min_cutoff, max_cutoff)
        if cutoff in self.cutoffs:
            print("FAIL", cutoff, num_segments)
            breakpoint()
        self.cutoff_path.append(cutoff)
        self.prev_point = (cutoff, num_segments)
        self.cutoffs[cutoff] = num_segments
        segbound = self.bounds.setdefault(num_segments, (cutoff, cutoff))
        self.bounds[num_segments] = min(cutoff, *segbound), max(cutoff, *segbound)

    def get_best_bounds(self):
        # looking for transition of num_segments between k+1 and k+2
        lower_cutoff = upper_cutoff = None
        q = 0
        while lower_cutoff is None:
            lower_cutoff = self.bounds.get(self.k+2+q)
            q += 1
        lower_cutoff = max(lower_cutoff)
        q = 0
        while upper_cutoff is None:
            upper_cutoff = self.bounds.get(self.k+1-q)
            q += 1
        upper_cutoff = min(upper_cutoff)
        # ## upper - lower == 1 and cutoff_upper == k+2 and cutoff_lower == k+1
        # ##
        # ## if self.prev_point = (72185,10) and (lower,cut),(upper,cut) == ((72185, 10), (125696, 7))
        # ##    and k=6
        lower_num_segs, upper_num_segs = self.cutoffs[lower_cutoff], self.cutoffs[upper_cutoff]
        return (lower_cutoff, lower_num_segs), (upper_cutoff, upper_num_segs)

    def has_answer(self):
        (lower_cutoff, lower_ns), (upper_cutoff, upper_ns) = self.get_best_bounds()
        _has_answer = (
            lower_ns >= self.k + 2 and upper_ns == self.k + 1 and upper_cutoff - lower_cutoff == 1
        )
        return _has_answer and upper_cutoff

    def get_next(self):
        (lower_cutoff, lower_ns), (upper_cutoff, upper_ns) = self.get_best_bounds()
        next_cutoff = (upper_cutoff - lower_cutoff) // 2 + lower_cutoff
        return next_cutoff

    def plot_cutoffs(self):
        import matplotlib.pyplot as plt
        x = list(self.cutoffs)
        y = [self.cutoffs[e] for e in x]
        plt.xlabel("cutoff")
        plt.ylabel("num_segments")
        plt.scatter(x, y)
        plt.show()


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        return self.maximizeSweetness_guessAndCheckApproach2(sweetness, k)

    def maximizeSweetness_guessAndCheckApproach2(self, sweetness: List[int], k: int) -> int:
        if len(sweetness) == k + 1:
            return min(sweetness)
        helper = Helper(sweetness, k)

        total_sweetness = sum(sweetness)
        CUTOFF_MAX = ceil(total_sweetness / k)  # max val should mean min num_segs
        num_segs_MAX = helper._calculate_segments(CUTOFF_MAX)
        helper._add_point(num_segs_MAX, CUTOFF_MAX)

        CUTOFF_MIN = min(sweetness)  # min val should mean max num_segs
        num_segs_MIN = helper._calculate_segments(CUTOFF_MIN)
        helper._add_point(num_segs_MIN, CUTOFF_MIN)

        cnt = 0
        while True:
            cnt += 1
            next_cutoff = helper.get_next()
            # num_segs, _, _ = calculate_segments(sweetness, next_cutoff)
            num_segs = helper.add_cutoff(next_cutoff)
            # helper._add_point(num_segs, next_cutoff)

            if answer_num_segs := helper.has_answer():
                print("cutoff_path:", helper.cutoff_path)
                helper.plot_cutoffs()
                return answer_num_segs



TEST_CALL = Solution().maximizeSweetness
CASES = (
    # ## expected, *input_args
    (6, [1, 2, 3, 4, 5, 6, 7, 8, 9], 5),
    (5, [1, 2, 2, 1, 2, 2, 1, 2, 2], 2),
    (1, [5, 6, 7, 8, 9, 1, 2, 3, 4], 8),
    (52832, [52832, 63820, 96186, 1623, 88717], 3),
    (55382, [90670, 55382, 95298, 95795, 73204, 41464, 18675, 30104, 47442, 55307], 6),
    (641293,
     [87002, 22650, 61737, 4432, 87341, 67643, 13454, 83823, 87836, 2978, 99313, 82797, 77350, 55994, 31403, 73836,
      54451, 54807, 60146, 72381, 7271, 37633, 32603, 33752, 78004, 76288, 94608, 3516, 98287, 16577, 36186, 40401,
      70733, 35764, 76303, 74279, 18351, 74113, 26480, 64253, 49402, 47512, 37185, 42488, 43068, 3542, 55773, 91365,
      86770, 52915], 3),
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
    test(3)
