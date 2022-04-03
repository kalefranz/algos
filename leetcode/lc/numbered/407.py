"""
407. Trapping Rain Water II
Hard

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D
elevation map, return the volume of water it can trap after raining.

https://leetcode.com/problems/trapping-rain-water-ii/

## NOTES:
  - Cannot simply use the answer to 42 (Trapping Rain Water I) and translate to 2D.

      [
        [12,13,1,12],
        [13,4,13,12],  # look at the cell with value 4
        [13,8,10,12],  # water leaks out through 8, then the cell holds amt = 12 - 4
        [12,13,12,12],
        [13,13,13,13]
      ]

    Look at the 2D array above, the point is at [1][1], in your solution, the answer for [1][1]
    is 13-4=9 which eventually accumulates into 15.  But take a closer look, how much can [1][1]
    take? it is bounded with [2][3] which is 12, so it should be 12-4=8, that's where the
    difference is.

"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


def dfs_min_bounding(grid, r, c):
    nr, nc = len(grid), len(grid[0])




class Solution:
    def trapRainWater_dfs(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])

        def dfs_for_min(r, c):
            for rp, cp in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):


        return

    def trapRainWater_wrong(self, heightMap: List[List[int]]) -> int:
        # This solution is wrong, per explanation above.
        def get_maxes(grid, x, y):
            xs = [row[y] for row in grid]
            ys = grid[x]
            return max(xs[:x + 1]), max(xs[x:], ), max(ys[:y + 1]), max(ys[y:])

        total, nr, nc = 0, len(heightMap), len(heightMap[0])
        for r in range(nr):
            for c in range(nc):
                total += min(get_maxes(heightMap, r, c)) - heightMap[r][c]
        return total


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (4, [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]),
    (10, [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]),
    (14, [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]),
    (3, [[5,5,5,1],[5,1,1,5],[5,1,5,5],[5,2,5,8]]),
    (215, [[9,9,9,9,9,9,8,9,9,9,9],[9,0,0,0,0,0,1,0,0,0,9],[9,0,0,0,0,0,0,0,0,0,9],[9,0,0,0,0,0,0,0,0,0,9],[9,9,9,9,9,9,9,9,9,9,9]]),
    (12, [[5,8,7,7],[5,2,1,5],[7,1,7,1],[8,9,6,9],[9,8,9,9]]),
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
    sys.exit(test())
