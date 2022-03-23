"""
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


"""
from collections import deque
from typing import *
from lc.lc_system import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


TEST_CALL = Solution().mergeTwoLists
CASES = (
    # ## expected, *input_args
    ([1,1,2,3,4,4], [1,2,4], [1,3,4]),
    ([], [], []),
    ([0], [], [0]),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, args in enumerate(cases):
        args = [ListNode._array_to_list_node(arg) for arg in args]
        (expected, *input_args) = args
        result = TEST_CALL(*input_args)
        expected = ListNode.serialize(expected)
        result = ListNode.serialize(result)
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
