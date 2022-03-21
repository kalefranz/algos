from collections import deque
from typing import *


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        start  = next((
            (r,c) for r in range(rows) for c in range(cols) if grid[r][c] == '*'
        ), None)

        queue = deque()
        visited = set()
        visited.add(start)
        queue.append(
            # steps, (r, c)
            (0, start)
        )
        while queue:
            steps, (r, c) = queue.popleft()
            steps += 1
            for (rp, cp) in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                if 0 <= rp < rows and 0 <= cp < cols:
                    if (rp, cp) not in visited:
                        val = grid[rp][cp]
                        if val == '#':
                            return steps
                        elif val == 'O':
                            # add to queue and visited
                            visited.add((rp,cp))
                            queue.append(
                                (steps, (rp,cp))
                            )
                        elif val == 'X':
                            # add to visisted
                            visited.add((rp,cp))
        return -1



TEST_CALL = Solution().getFood
CASES = (
    ## expected, *input_args
    # (),
    (3, [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]),
    (-1, [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]),
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
