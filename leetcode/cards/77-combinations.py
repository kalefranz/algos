"""
77. Combinations
Medium

Implement n choose k.

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2798/

I didn't understand what this had to do with backtracking.
The first sentence of the solution though:
  Backtracking is an algorithm for finding all solutions by exploring (exploding?) all potential candidates.

NOTES:
  the enumeration of candidates is done in two levels
    1) at the first level, the function is implemented as recursion. At each occurrence of
       recursion, the function is one step further to the final solution
    2) within the recursion, we have an iteration that allows us to explore all the candidates
       **that are of the same progress to the final solution**

# ## shortened template
# def backtrack(candidate):
#     if find_solution(candidate):
#         output(candidate)
#         return
#     for next_candidate in list_of_candidates:
#         if is_valid(next_candidate):
#             place(next_candidate)
#             backtrack(next_candidate)
#             remove(next_candidate)


"""
from collections import deque
from typing import *

from itertools import combinations

class Solution:
    def combine_punkForm(self, n: int, k: int):
        nums = tuple(range(1,n+1))
        return set(combinations(nums, k))

    def combine(self, n: int, k: int):
        nums = tuple(range(1,n+1))

        output = []

        def backtrack(nxt, curr_combo):
            if len(curr_combo) == k:
                output.append(tuple(curr_combo))
            for nxt_candidate in range(nxt, n+1):
                # place
                curr_combo.append(nxt_candidate)
                # backtrack
                backtrack(nxt_candidate+1, curr_combo)
                # remove
                curr_combo.pop()

        backtrack(nums[0], [])

        return set(output)


TEST_CALL = Solution().combine
CASES = (
    # ## expected, *input_args
    (((1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)), 4, 2),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        expected = set(expected)
        print(tuple(sorted(expected)))
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
test()
