"""
37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2796/


NOTES:
  the enumeration of candidates is done in two levels
    1) at the first level, the function is implemented as recursion. At each occurrence of
       recursion, the function is one step further to the final solution
    2) within the recursion, we have an iteration that allows us to explore all the candidates
       **that are of the same progress to the final solution**




"""
from collections import deque
from itertools import chain, product
from pprint import pprint
from typing import *

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

boxes = (
    (((0, 3), (0, 3)), ((0, 3), (3, 6)), ((0, 3), (6, 9)),),
    (((3, 6), (0, 3)), ((3, 6), (3, 6)), ((3, 6), (6, 9)),),
    (((6, 9), (0, 3)), ((6, 9), (3, 6)), ((6, 9), (6, 9)),),
)
complete = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}


def get_box_set(board, r, c):
    rspan, cspan = boxes[r // 3][c // 3]
    rows = board[slice(*rspan)]
    box_vals = set(chain.from_iterable(r[slice(*cspan)] for r in rows))
    return box_vals


def generate_possibles(board, r, c):
    """
    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    """
    possibles = (
        complete - set(board[r]) - set(board[q][c] for q in range(len(board))) - get_box_set(board, r, c)
    )
    return possibles


def complete_board(board):
    return not any(board[r][c] == "." for r, c in product(range(9),range(9)))


def correct_board(board):
    if not complete_board(board):
        return False
    cols = (set(board[q][c] for q in range(len(board))) for c in range(len(board)))
    boxes = (get_box_set(board, *x) for x in product(range(0, 9, 3), range(0, 9, 3)))
    return (
        all(len(complete - set(row)) == 0 for row in board)
        and all(len(complete - col) == 0 for col in cols)
        and all(len(complete - box) == 0 for box in boxes)
    )


def space_is_empty(board, r, c):
    return board[r][c] == "."


class SolutionFound(Exception): pass


class Solution:

    def solveSudoku(self, board: List[List[str]]):
        nr, nc = len(board), len(board[0])

        def backtrack(r, c):
            if correct_board(board):
                # return board
                raise SolutionFound()

            if space_is_empty(board, r, c):
                # explore this partial candidate solution, and mark the attacking(?) zone
                for possible in generate_possibles(board, r, c):
                    board[r][c] = possible
                    if r+1 == nr and c+1 == nc:
                        # we reach the bottom, i.e. we find a solution!
                        # return board
                        raise SolutionFound()
                    else:
                        if c+1 == nc:
                            backtrack(r+1, 0)
                        else:
                            backtrack(r, c+1)
                    board[r][c] = "."
            else:
                if c + 1 == nc:
                    backtrack(r + 1, 0)
                else:
                    backtrack(r, c + 1)

        try:
            return backtrack(0, 0)
        except SolutionFound:
            return board


unsolved1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
solved1 = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]


TEST_CALL = Solution().solveSudoku
CASES = (
    # ## expected, *input_args
    (solved1, unsolved1),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        result = TEST_CALL(*input_args)
        pprint(result)
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
