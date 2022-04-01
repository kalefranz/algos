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
        for qq, (expected, func, args) in enumerate(zip(*case)):
            if qq == 0:
                instance = globals()[func](*args)
                instance_init = f"{func}{tuple(args)}"
                continue
            else:
                result = getattr(instance, func)(*args)
                if result == expected:
                    # print(f"{q}: passed")
                    pass
                else:
                    print(f"{q}/{qq}: FAILED  {instance_init}.{func}{tuple(args)}")
                    print(f"  {expected} != {result}")
                    failed += 1
                    break
    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())
