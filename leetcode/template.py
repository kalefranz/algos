"""
"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        return


TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    # ## expected, *input_args
    (3, [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]),
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
