"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2804/


# Backtracking Psuedocode
# https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2793/

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return

    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)



"""
from collections import deque
from typing import *


# def backtrack_nqueen(row = 0, count = 0):
#     # from https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2654/
#     # I think I'm supposed to be able to use this
#     for col in range(n):
#         # iterate through columns at the curent row.
#         if is_not_under_attack(row, col):
#             # explore this partial candidate solution, and mark the attacking zone
#             place_queen(row, col)
#             if row + 1 == n:
#                 # we reach the bottom, i.e. we find a solution!
#                 count += 1
#             else:
#                 # we move on to the next row
#                 count = backtrack_nqueen(row + 1, count)
#             # backtrack, i.e. remove the queen and remove the attacking zone.
#             remove_queen(row, col)
#     return count



class Solution:
    def totalNQueens(self, n: int) -> int:
        queens = set()

        def queen_attacks_loc(qr, qc, row, col):
            return row == qr or col == qc or abs((row - qr) / (col - qc)) == 1

        def is_not_under_attack(row, col):
            return not any(queen_attacks_loc(qr, qc, row, col) for qr, qc in queens)

        def place_queen(row, col):
            queens.add((row, col))

        def remove_queen(row, col):
            queens.remove((row, col))

        def backtrack_nqueen(row, count):
            # iterate through columns at the current row
            for col in range(n):
                # explore this partial candidate solution, and mark the attacking zone
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack_nqueen(row+1, count)
                    # Now backtrack. I.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
            return count

        return backtrack_nqueen(0, 0)



TEST_CALL = Solution().totalNQueens
CASES = (
    # ## expected, *input_args
    (2, 4),
    (1, 1),
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
test()
