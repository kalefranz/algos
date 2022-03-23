"""
994. Rotting Oranges
Medium

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is
impossible, return -1.


Strategy / Thoughts:
  - DFS to find longest chain s.t. grid => 2, 1, 1, 1...
  - I think this has to be solved in two distinct parts. First find all the contiguous clusters of
    fresh oranges. Second calculate min rot time for each cluster.
  - Because we want a record of every cell in each fresh cluster, the search needs to be BFS.
  - Actually, probably doesn't matter if its DFS or BFS?  We just need to get all connected.
    Don't care about shorted or longest for gathering the fresh clusters.
  - *New Idea*: Find every 2 cell that touches a 1 cell. Then count the number of iterations
    it takes to flip all of those 1 chains to 2s. Then the answer will be the number of iterations,
    unless there is an island of 1s that don't touch 2s.
  - Still think I need to find all of the contiguous 1 groups, and then get the 1-2 touch points
    as a second step. That way if we have any clean 1 islands, we can return early with a -1
    answer.

https://leetcode.com/problems/rotting-oranges/

Topics: Array, BFS, Matrix

"""
from collections import deque
from functools import reduce
from typing import *

from itertools import product


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        adjacent = lambda x, y: ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

        nr, nc = len(grid), len(grid[0])
        visited = set()

        def moves(r, c):
            gen = (
                (rp, cp) for rp, cp in adjacent(r, c)
                if 0 <= rp < nr and 0 <= cp < nc and grid[rp][cp] == 1 and (rp, cp) not in visited
            )
            return gen

        def bfs_fresh(r, c):
            assert grid[r][c] == 1
            fresh_group = set()

            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                fresh_group.add((r, c))
                visited.add((r, c))
                queue.extend(moves(r, c))
            return fresh_group

        def fresh_clusters():
            gen = (
                (r, c) for r, c in product(range(nr), range(nc))
                if grid[r][c] == 1 and (r, c) not in visited
            )
            clusters = tuple(
                bfs_fresh(r, c) for r, c in gen
            )
            return clusters

        def touches_rot(rc):
            return any(
                0 <= rp < nr and 0 <= cp < nc and grid[rp][cp] == 2
                for rp, cp in adjacent(*rc)
            )

        clusters = fresh_clusters()

        def rot_one_day():
            """
            for each cluster,
            get rot_points
            set grid=>2 for each rot point
            take those rot_points out of the cluster

            then set rot_points to the next day's rot_points
            """
            for cluster in clusters:
                rot_points = set(filter(touches_rot, cluster))
                for r, c in rot_points:
                    grid[r][c] = 2
                cluster -= rot_points

        day_count = 0
        prev_total_fresh = total_fresh = sum(map(len, clusters))
        while day_count == 0 or prev_total_fresh > total_fresh:
            prev_total_fresh = total_fresh
            rot_one_day()
            day_count += 1
            total_fresh = sum(map(len, clusters))

        return -1 if total_fresh else day_count - 1


TEST_CALL = Solution().orangesRotting
CASES = (
    # ## expected, *input_args
    (4, [[2, 1, 1], [1, 1, 0], [0, 1, 1]]),
    (-1, [[2, 1, 1], [0, 1, 1], [1, 0, 1]]),
    (0, [[0, 2]]),
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


if __name__ == "__main__":
    test()
