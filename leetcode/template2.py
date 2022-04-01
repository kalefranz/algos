"""

"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json

class SnapshotArray:

    def __init__(self, length: int):
        pass

    def set(self, index: int, val: int) -> None:
        pass


null, true, false = None, True, False
data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (
        [null,null,0,null,5],
        ["SnapshotArray","set","snap","set","get"],
        [[3],[0,5],[],[0,6],[0,0]],
    ),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, case in enumerate(cases):
        subtests_builder = []
        subtests_failed = 0
        for qq, (expected, func, args) in enumerate(zip(*case)):
            if qq == 0:
                instance = globals()[func](*args)
                subtests_builder.append(f"{q}.{qq}: passed  obj = {func}{*args,}")
                continue
            else:
                result = getattr(instance, func)(*args)
                if result == expected:
                    subtests_builder.append(f"{q}.{qq}: passed  {expected} ?= obj.{func}{*args,}")
                else:
                    subtests_builder.append(f"{q}.{qq}: FAILED  {expected} ?= obj.{func}{*args,}\n"
                                            f"        {expected} != {result}")
                    subtests_failed += 1
        if subtests_failed:
            subtests_builder.append("")
            print("\n".join(subtests_builder))
            failed += 1

    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())
