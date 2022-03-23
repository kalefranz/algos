"""
"""
from collections import deque
from typing import *
from lc.lc_system.listnode import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        def reverse_node(node):
            nonlocal new_head
            a = node
            b = a.next
            a.next = None
            if b.next is None:
                # b was tail, should now be head
                new_head = b
                b.next = a
            else:
                reverse_node(b)
                assert b.next is None
                b.next = a
        reverse_node(head)
        return new_head


        #     if b and b.next:
        #         reverse_node(b)
        #     assert b.next is None
        #     b.next = a
        #
        # reverse_node(head)

        #
        # if node is None:  # we have reached tail
        #     raise
        # assert node.next
        # self.reverseList(node.next)  # so that node.next can be pointed at node
        # assert node.next is None
        # node.next = node
        #
        # if not head:
        #     return head
        # rev = self.reverseList(head.next)
        # if not rev:
        #     rev = ListNode()
        # rev.next = head
        # return rev



TEST_CALL = Solution().reverseList
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
    test(0)
