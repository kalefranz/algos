"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise,
    add the key-value pair to the cache. If the number of keys exceeds the capacity from
    this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

https://leetcode.com/problems/lru-cache/

"""
from collections import deque, OrderedDict
import os.path
from typing import *

from lc.numbered import load_json


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        value = self.pop(key)
        self[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if (current := self.get(key)) == value:
            return
        elif current != -1:
            self[key] = value
        else:
            if len(self) >= self.cap:
                self.popitem(False)
            self[key] = value


null, true, false = None, True, False
data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    (
        [null,null,null,1,null,-1,null,-1,3,4],
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2],        [1,1], [2,2], [1],   [3,3], [2],   [4,4], [1],   [3],   [4]],
    ),
    (
        [null,null,null,2,null,null,-1],
        ["LRUCache","put","put","get","put","put","get"],
        [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]],
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
