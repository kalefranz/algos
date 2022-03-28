"""
1901. Find a Peak Element II
Medium

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

https://leetcode.com/problems/find-a-peak-element-ii/

"""
from collections import deque
import json
from math import copysign
from typing import *


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        nr, nc = len(mat), len(mat[0])

        def slope(r, c):
            if r == 0:
                r1, r2, r3 = -1, mat[r][c], mat[r+1][c]
            elif r == nr-1:
                r1, r2, r3 = mat[r-1][c], mat[r][c], -1
            else:
                r1, r2, r3 = mat[r - 1][c], mat[r][c], mat[r + 1][c]
            if c == 0:
                c1, c2, c3 = -1, mat[r][c], mat[r][c+1]
            elif c == nc-1:
                c1, c2, c3 = mat[r][c-1], mat[r][c], -1
            else:
                c1, c2, c3 = mat[r][c - 1], mat[r][c], mat[r][c + 1]
            dr1, dr2 = int(copysign(1, r2 - r1)), int(copysign(1, r3 - r2))
            dc1, dc2 = int(copysign(1, c2 - c1)), int(copysign(1, c3 - c2))
            return dr1, dr2, dc1, dc2

        r, c = nr//2, nc//2
        mover, movec = r//2 or 1, c//2 or 1
        try_next = deque()
        try_next.append((r, mover, c, movec))
        while True:
            dr1, dr2, dc1, dc2 = slope(r, c)
            # print((r, c), (dr1, dr2, dc1, dc2))
            if (dr1, dr2) == (1, -1) and (dc1, dc2) == (1, -1):
            # if dr1 == 1 and dr2 == -1 and dc1 == 1 and dc2 == -1:
                return [r, c]
            if dr1 == dr2 == 1:
                r += mover
                mover = mover//2 or 1
            elif dr1 == dr2 == -1:
                r -= mover
                mover = mover//2 or 1
            elif dc1 == dc2 == 1:
                c += movec
                movec = movec//2 or 1
            elif dc1 == dc2 == -1:
                c -= movec
                movec = movec//2 or 1
            else:
                # we've found a minimum instead of a maximum
                r, mover, c, movec = try_next.popleft()
                r1 = r - mover
                r2 = r + mover
                c1 = c - movec
                c2 = c + movec
                mover = mover // 2 or 1
                movec = movec // 2 or 1
                try_next.extend((
                    (r1, mover, c1, movec),
                    (r1, mover, c2, movec),
                    (r2, mover, c1, movec),
                    (r2, mover, c2, movec),
                ))
                r, mover, c, movec = try_next[0]


def print_grid(grid):
    rows = []
    for row in grid:
        rows.append("".join(f"{c:^4}" for c in row))
    print("\n".join(rows))
    print()


data = json.load(open("1901data.json"))
TEST_CALL = Solution().findPeakGrid
CASES = (
    # ## expected, *input_args
    ({(0,1),(1,0)}, [[1,4],[3,2]]),
    ({(1,1),(2,2)}, [[10,20,15],[21,30,14],[7,16,32]]),
    ({(0,3),(2,0)}, [[41,8,2,48,18],[16,15,9,7,44],[48,35,6,38,28],[3,2,14,15,33],[39,36,13,46,42]]),
    ({(0,2),(3,1)}, [[47,30,35,8,25],[6,36,19,41,40],[24,37,13,46,5],[3,43,15,50,19],[6,15,7,25,18]]),
    ({(499,499)}, data["mat4"]),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        # print_grid(input_args[0])
        result = TEST_CALL(*input_args)
        result = tuple(result)
        if result in expected:
            print(f"{q}: passed")
        else:
            print(f"{q}: FAILED")
            print(f"  {expected} !contains {result}")
            failed += 1
    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")

if __name__ == "__main__":
    test(4)
