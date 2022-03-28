"""
116. Populating Next Right Pointers in Each Node
Medium

You are given a perfect binary tree where all leaves are on the same level, and every parent has
two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the
next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
"""
from collections import deque
from typing import *
from lc.lc_system.treenode import SkipNode


class Solution:
    def connect(self, root: 'Optional[SkipNode]') -> 'Optional[SkipNode]':
        if not root:
            return root
        def _connect(node):
            if node.left:
                node.left.next = node.right  # (a)
                node.right.next = node.next.left if node.next else None  # (b)
                _connect(node.left)
                _connect(node.right)
        _connect(root)
        return root


TEST_CALL = Solution().connect
null = None
CASES = (
    # ## expected, *input_args
    ([1,null,2,3,null,4,5,6,7,null], [1,2,3,4,5,6,7]),
    ([], []),

    # ([], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        root = SkipNode._array_to_tree_node(input_args[0])
        result = TEST_CALL(root)
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

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())
