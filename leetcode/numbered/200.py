from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        def is_safe(r2, c2):
            return 0 <= r2 < num_rows and 0 <= c2 < num_cols

        adjustments = ((-1, 0), (1, 0), (0, -1), (0, 1))
        def get_connected_land(r1, c1):
            for dx, dy in adjustments:
                new_r = r1+dx
                new_c = c1+dy
                if is_safe(new_r, new_c):
                    if visited[new_r][new_c]:
                        continue
                    if not grid[new_r][new_c] == "1":
                        visited[new_r][new_c] = True
                    else:
                        yield (new_r, new_c)

        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]:
                    continue
                if grid[i][j] != "1":
                    visited[i][j] = True
                else:
                    stack = [(i,j)]
                    island = set()
                    while stack:
                        r, c = stack.pop()
                        visited[r][c] = True
                        island.add((r, c))
                        connected = list(get_connected_land(r, c))
                        stack.extend(connected)
                    islands.append(island)
        
        return len(islands)


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))
