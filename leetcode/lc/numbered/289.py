"""
289. Game of Life
Medium

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular
automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live
(represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors
(horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia
article):

    Any live cell with fewer than two live neighbors dies as if caused by under-population.
    Any live cell with two or three live neighbors lives on to the next generation.
    Any live cell with more than three live neighbors dies, as if by over-population.
    Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current
state, where births and deaths occur simultaneously. Given the current state of the m x n grid
board, return the next state.

https://leetcode.com/problems/game-of-life/

"""
from collections import deque
from itertools import product, starmap
import os.path
from typing import *

from lc.numbered import load_json


def iterate(board):
    """
    1. Any live cell with two or three live neighbours survives.
    2. Any dead cell with three live neighbours becomes a live cell.
    3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    """
    nr, nc = len(board), len(board[0])

    toggle_set = set()

    # def next_state(r, c):
    #     living_neighbors = sum(
    #         1 for rp, cp in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1))
    #         if 0 <= rp < nr and 0 <= cp < nc and board[rp][cp] == 1
    #     )
    #     if living_neighbors == 3 or board[r][c] == 1 and living_neighbors == 2:
    #         return 1
    #     else:
    #         return 0

    def add_toggle(r, c):
        live_neighbs = sum(
            1 for rp, cp in (
                (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
                (r + 1, c + 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1),
            )
            if 0 <= rp < nr and 0 <= cp < nc and board[rp][cp] == 1
        )
        if board[r][c] == (live_neighbs == 3 or board[r][c] == 1 and live_neighbs == 2):
            toggle_set.add((r, c))

    any(add_toggle(*rc) for rc in product(range(nr), range(nc)))

    toggle = lambda r, c: int(not board[r][c])
    any(toggle(r, c) for r, c in toggle_set)
    return board


class Solution:
    def gameOfLife(self, board: List[List[int]]):
        nr, nc = len(board), len(board[0])
        toggle_set = set()

        def add_toggle(r, c):
            live_neighbs = sum(
                1 for rp, cp in (
                    (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1),
                    (r + 1, c + 1), (r - 1, c - 1), (r - 1, c + 1), (r + 1, c - 1),
                )
                if 0 <= rp < nr and 0 <= cp < nc and board[rp][cp] == 1
            )
            if board[r][c] != (live_neighbs == 3 or board[r][c] == 1 and live_neighbs == 2):
                toggle_set.add((r, c))

        any(add_toggle(*rc) for rc in product(range(nr), range(nc)))
        for r, c in toggle_set:
            board[r][c] = int(not board[r][c])

        return board


TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    ([[0,0,0],[1,0,1],[0,1,1],[0,1,0]], [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]),
    ([[1,1],[1,1]], [[1,1],[1,0]]),
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

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())
