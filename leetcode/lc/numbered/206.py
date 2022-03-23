"""
"""
from collections import deque
from typing import *
from lc.lc_system.listnode import ListNode


class Solution:
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = None
        def reverse_node(node):
            nonlocal new_head
            a = node
            a.next, b = None, a.next
            if b.next is None:
                b.next, new_head = a, b
            else:
                reverse_node(b)
                b.next = a
        reverse_node(head)
        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        a = head
        a.next, b = None, a.next
        while b.next:
            b.next, c = a, b.next
            a, b = b, c
        head, b.next = b, a
        return head


TEST_CALL = Solution().reverseListRecursive
CASES = (
    # ## expected, *input_args
    ([5,4,3,2,1], [1,2,3,4,5]),
    ([1,2], [2,1]),
    ([], []),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        head = ListNode._array_to_list_node(input_args[0])
        result = TEST_CALL(head)
        result = result.as_py_list()
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
    test(0)
