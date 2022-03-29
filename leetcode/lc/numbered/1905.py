"""
1905. Count Sub Islands
Medium

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water)
and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or
vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the
cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

https://leetcode.com/problems/count-sub-islands/

"""
from collections import deque
from itertools import chain, count, product
from operator import itemgetter
import os.path
from typing import *

from lc.numbered import load_json


def print_grid(grid):
    rows = []
    for row in grid:
        rows.append("".join(f" {c} " for c in row))
    print("\n".join(rows))


def get_islands_recursive(grid):
    nr, nc = len(grid), len(grid[0])
    visited = set()

    def valid(rc):
        return 0 <= rc[0] < nr and 0 <= rc[1] < nc and grid[rc[0]][rc[1]] == 1 and rc not in visited

    def moves(r, c):
        return (
            rcp for rcp in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)) if valid(rcp)
        )

    def dfs_collect(rc):
        visited.add(rc)
        return chain((rc,), *(dfs_collect(rcp) for rcp in moves(*rc)))

    islands = tuple(
        set(dfs_collect(rc)) for rc in product(range(nr), range(nc)) if valid(rc)
    )
    return islands


def get_islands_stack(grid):
    nr, nc = len(grid), len(grid[0])
    visited = set()

    def valid(rc):
        return 0 <= rc[0] < nr and 0 <= rc[1] < nc and grid[rc[0]][rc[1]] == 1 and rc not in visited

    def moves(r, c):
        return (
            rcp for rcp in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)) if valid(rcp)
        )

    def dfs_collect(rc):
        stack = []
        island = set()
        add = lambda rcpp: visited.add(rcpp) or island.add(rcpp) or stack.append(rcpp)

        add(rc)
        while stack:
            rc = stack.pop()
            for rcp in moves(*rc):
                if valid(rcp):
                    add(rcp)

        return island

    islands = tuple(
        dfs_collect(rc) for rc in product(range(nr), range(nc)) if valid(rc)
    )
    return islands


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        grid_1_land = set(filter(lambda rc: grid1[rc[0]][rc[1]], product(range(len(grid1)), range(len(grid1[0])))))
        islands2 = get_islands_stack(grid2)

        num_sub_islands = sum(
            1 for isl2 in islands2 if len(isl2 - grid_1_land) == 0
        )
        return num_sub_islands


TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    # ## expected, *input_args
    (3, [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]),
    (2, [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]),
    (1, [[1]], [[1]]),
    (0, [[1]], [[0]]),
    (310, data["grid1_4"], data["grid2_4"]),
    (0, data["grid1_5"], data["grid2_5"]),
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
