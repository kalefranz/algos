from typing import *
from functools import cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        def moves(i, j):
            for n_i, n_j in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if n_i >= 0 and n_i < m and n_j >= 0 and n_j < n and matrix[n_i][n_j] < matrix[i][j]:
                    yield (n_i, n_j)

        @cache
        def dp(i, j):
            return 1 + max((dp(n_i, n_j) for n_i, n_j in moves(i, j)), default=0)

        return max(dp(i, j) for i in range(m) for j in range(n))


TEST_CALL = Solution().longestIncreasingPath
CASES = (
    ## expected, *input_args
    (4, [[9, 9, 4], [6, 6, 8], [2, 1, 1]]),
    (4, [[3, 4, 5], [3, 2, 6], [2, 2, 1]]),
    (1, [[1]]),
    (8, [[0, 0, 12, 6, 15, 1, 12, 10, 12, 10, 6], [6, 19, 6, 13, 5, 18, 17, 19, 7, 11, 13],
         [8, 6, 9, 1, 15, 7, 10, 10, 3, 7, 18], [2, 14, 12, 10, 17, 2, 3, 10, 4, 8, 3],
         [8, 2, 19, 3, 19, 10, 17, 18, 12, 10, 8], [0, 17, 14, 12, 10, 4, 8, 17, 15, 11, 19],
         [13, 6, 14, 8, 16, 19, 12, 17, 16, 17, 8], [7, 4, 6, 8, 3, 9, 19, 12, 4, 13, 0],
         [18, 0, 16, 12, 10, 11, 8, 14, 6, 3, 0], [10, 3, 14, 17, 19, 18, 10, 2, 11, 5, 19],
         [6, 2, 2, 1, 8, 1, 11, 7, 7, 18, 1], [11, 12, 16, 0, 9, 6, 8, 3, 12, 8, 15],
         [5, 18, 17, 4, 11, 9, 9, 6, 8, 2, 4], [3, 12, 7, 2, 9, 17, 14, 10, 14, 5, 0]]),
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
