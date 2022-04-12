"""
226. Invert Binary Tree
Easy

Reverse binary tree
Invert binary tree

Given the root of a binary tree, invert the tree, and return its root.

https://leetcode.com/problems/invert-binary-tree/

"""
from collections import deque
import os.path
from typing import *

from lc.numbered import load_json
from lc.lc_system import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def invert(node):
            node.left, node.right = invert(node.right) if node.right else None, invert(node.left) if node.left else None
            return node
        return invert(root)


data = load_json(int(os.path.basename(__file__)[:-3]))
CASES = (
    ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ([2,1,3], [2,3,1]),
    ([], []),
)
TEST_CALL = getattr(Solution(), list(Solution.__dict__.keys())[1])
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, *input_args) in enumerate(cases):
        input_arg = TreeNode._array_to_tree_node(input_args[0])
        result = TEST_CALL(input_arg)
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
