"""
329. Longest Increasing Path in a Matrix

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move
diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Topics: Dynamic Programming, DFS, BFS, Graph, Topological Sort, Memoization

https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

"""
from collections import deque
from functools import cache
from typing import *


class Solution1:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = {}
        longest = 0
        q = 0
        g = ((r, c) for r in range(len(matrix)) for c in range(len(matrix[0])))
        for (r, c) in g:
            start = (r, c)
            if visited.get(start, 0) > 1:
                continue
            stack = [(start, 1)]  # state: ((r, c), count)
            while stack:
                (r, c), count = stack.pop()
                q += 1
                visited[(r, c)] = count
                longest = max(longest, count)
                for (rp, cp) in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if 0 <= rp < len(matrix) and 0 <= cp < len(matrix[0]):
                        if matrix[rp][cp] > matrix[r][c]:
                            if count+1 > visited.get((rp, cp), 0):
                                stack.append(((rp, cp), count+1))
        return longest


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nrows, ncols = len(matrix), len(matrix[0])

        def moves(r, c):
            for (rp, cp) in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= rp < nrows and 0 <= cp < ncols and matrix[rp][cp] > matrix[r][c]:
                    yield rp, cp

        @cache
        def depth(r, c):
            return 1 + max((depth(rp, cp) for rp, cp in moves(r, c)), default=0)

        return max(depth(r, c) for r in range(nrows) for c in range(ncols))



TEST_CALL = Solution().longestIncreasingPath
CASES = (
    ## expected, *input_args
    (4, [[9,9,4],[6,6,8],[2,1,1]]),
    (4, [[3,4,5],[3,2,6],[2,2,1]]),
    (1, [[1]]),
    (8, [[0,0,12,6,15,1,12,10,12,10,6],[6,19,6,13,5,18,17,19,7,11,13],[8,6,9,1,15,7,10,10,3,7,18],[2,14,12,10,17,2,3,10,4,8,3],[8,2,19,3,19,10,17,18,12,10,8],[0,17,14,12,10,4,8,17,15,11,19],[13,6,14,8,16,19,12,17,16,17,8],[7,4,6,8,3,9,19,12,4,13,0],[18,0,16,12,10,11,8,14,6,3,0],[10,3,14,17,19,18,10,2,11,5,19],[6,2,2,1,8,1,11,7,7,18,1],[11,12,16,0,9,6,8,3,12,8,15],[5,18,17,4,11,9,9,6,8,2,4],[3,12,7,2,9,17,14,10,14,5,0]]),
    (140, [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]),
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
