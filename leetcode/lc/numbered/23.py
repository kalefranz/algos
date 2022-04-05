"""
23. Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

https://leetcode.com/problems/merge-k-sorted-lists/
"""

from collections import deque
from queue import PriorityQueue
import os.path
from typing import *

from lc.numbered import load_json
from lc.lc_system import ListNode


ListNode.__lt__ = lambda self, other: self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = PriorityQueue()
        any(queue.put(ll) for ll in lists if ll)

        head = tail = ListNode(-1)

        while queue.qsize():
            node = queue.get(timeout=0)
            if node.next:
                queue.put(node.next)
            node.next = None
            tail.next = node
            tail = tail.next

        return head.next



data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    ([1,1,2,3,4,4,5,6], [1,4,5],[1,3,4],[2,6]),
    ([], []),
    ([], [[]])
)
TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        args = [ListNode._array_to_list_node(input_arg) for input_arg in input_args]
        result = TEST_CALL(args)
        result = result.as_py_list() if result else []
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
