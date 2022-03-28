"""
1254. Number of Closed Islands
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally
connected group of 0s and a closed island is an island totally (all left, top, right, bottom)
surrounded by 1s.

Return the number of closed islands.

"""
from collections import deque
from typing import *


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        numr, numc = len(grid), len(grid[0])
        visited = set()
        groups = []

        def moves(r, c):
            if (r == 0 or r == numr - 1) or (c == 0 or c == numc - 1):
                yield r, c, 'poison'
            for (rp, cp) in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if (rp, cp) in visited or (rp < 0 or cp < 0 or rp >= numr or cp >= numc):
                    continue
                if grid[rp][cp] == 0 and ((rp == 0 or rp == numr-1) or (cp == 0 or cp == numc-1)):
                    yield rp, cp, 'poison'
                elif grid[rp][cp] == 0:
                    yield rp, cp, 'safe'

        gen = ((r, c) for r in range(1, numr-1) for c in range(1, numc-1))
        for (r, c) in gen:
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if grid[r][c] != 0:
                continue

            group = set()
            stack = [(r, c)]
            poisoned = False
            while stack:
                r, c = stack.pop()
                group.add((r, c))
                for rp, cp, danger in moves(r, c):
                    if danger == 'poison':
                        poisoned = True
                    if (rp, cp) not in visited:
                        visited.add((rp, cp))
                        stack.append((rp, cp))
            if not poisoned:
                groups.append(group)

        return len(groups)  # , groups



def print_grid(grid):
    rows = []
    for row in grid:
        rows.append("".join(f" {c} " for c in row))
    print("\n".join(rows))




TEST_CALL = Solution().closedIsland
CASES = (
    # ## expected, *input_args
    (2, [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]),
    (1, [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]),
    (2, [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],
         [1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]),
    (5,[[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],
        [0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],
        [1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]),
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

# grid = CASES[3][1]
# result = Solution().closedIsland(grid)
# print(result)
# # for grp in result[1]:
# #     for r, c in grp:
# #         grid[r][c] = 'X'
# print_grid(grid)

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

