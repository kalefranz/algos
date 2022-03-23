"""
1020. Number of Enclaves
Medium

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

https://leetcode.com/problems/number-of-enclaves/

Topics: Array, DFS, BFS, Union Find, Matrix

"""
from collections import deque
from itertools import chain, product
from typing import *

# ## NOTE: Seems like the same problem as 1254, which I made a note that I needed to redo.

class Solution:
    def numEnclaves_notMine(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                list(map(dfs, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))

        m, n = len(grid), len(grid[0])
        for i, j in product(range(m), range(n)):
            if i in (0, m - 1) or j in (0, n - 1):
                dfs(i, j)

        return sum(map(sum, grid))

    def numEnclaves_1(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c]:
                grid[r][c] = 0
                for (rp, cp) in ((r+1, c),(r-1, c),(r, c+1),(r, c-1)):
                    if 0 <= rp < nr and 0 <= cp < nc and grid[rp][cp]:
                        dfs(rp, cp)

        edges = chain.from_iterable((
            ((r, 0) for r in range(nr)),
            ((r, nc-1) for r in range(nr)),
            ((0, c) for c in range(nc)),
            ((nr-1, c) for c in range(nc)),
        ))
        for (r, c) in edges:
            dfs(r, c)

        return sum(grid[r][c] for r in range(1,nr-1) for c in range(1,nc-1))

    def numEnclaves_2(self, grid: List[List[int]]) -> int:
        rend, cend = len(grid)-1, len(grid[0])-1

        def dfs_zero_attached(coord):
            r, c = coord
            grid[r][c] = 0
            gen = (
                (rp, cp) for rp, cp in ((r+1, c),(r-1, c),(r, c+1),(r, c-1))
                if 0 <= rp <= rend and 0 <= cp <= cend and grid[rp][cp]
            )
            any(map(dfs_zero_attached, gen))

        edges = chain(
            ((r, 0) for r in range(rend+1)),
            ((r, cend) for r in range(rend+1)),
            ((0, c) for c in range(cend+1)),
            ((rend, c) for c in range(cend+1)),
        )
        for coord in edges:
            if grid[coord[0]][coord[1]]:
                dfs_zero_attached(coord)

        return sum(grid[r][c] for r, c in product(range(1, rend), range(1, cend)))

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rend, cend = len(grid)-1, len(grid[0])-1

        def dfs_zero_attached(coord):
            r, c = coord
            grid[r][c] = 0
            gen = (
                (rp, cp) for rp, cp in ((r+1, c),(r-1, c),(r, c+1),(r, c-1))
                if 0 <= rp <= rend and 0 <= cp <= cend and grid[rp][cp]
            )
            any(map(dfs_zero_attached, gen))

        for r in range(rend+1):
            if grid[r][0]: dfs_zero_attached((r, 0))
            if grid[r][cend]: dfs_zero_attached((r, cend))
        for c in range(cend+1):
            if grid[0][c]: dfs_zero_attached((0, c))
            if grid[rend][c]: dfs_zero_attached((rend, c))

        return sum(grid[r][c] for r, c in product(range(1, rend), range(1, cend)))




def print_grid(grid):
    rows = []
    for row in grid:
        rows.append("".join(f" {c} " for c in row))
    print("\n".join(rows))



TEST_CALL = Solution().numEnclaves
CASES = (
    # ## expected, *input_args
    (3, [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]),
    (0, [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]),
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
