"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2874/

includes leetcode TreeNode construction for tests

"""
from collections import deque
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        assert val is not None
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}<{self.left},{self.right}>"

    def __repr__(self):
        return str(self)


def construct_tree(nums):
    nums = deque(nums)
    root = TreeNode(nums.popleft())
    node_Q = deque([root])

    def next_node():
        while node_Q:
            yield node_Q.popleft()

    while nums:
        left_val, right_val = nums.popleft(), nums.popleft()
        node = next(next_node())
        left_node = right_node = None
        if left_val is not None:
            node.left = left_node = TreeNode(left_val)
        if right_val is not None:
            node.right = right_node = TreeNode(right_val)
        node_Q.append(left_node)
        node_Q.append(right_node)

    return root


def is_valid_node(node):
    if node.left is None:
        left_valid = True
        lminl = lmaxl = lminr = lmaxr = node.val
    else:
        left_valid, (lminl, lmaxl), (lminr, lmaxr) = is_valid_node(node.left)
        left_valid &= lminl <= lmaxl <= lminr <= lmaxr
        left_valid &= node.val > lmaxr
    if node.right is None:
        right_valid = True
        rminl = rmaxl = rminr = rmaxr = node.val
    else:
        right_valid, (rminl, rmaxl), (rminr, rmaxr) = is_valid_node(node.right)
        right_valid &= rminl <= rmaxl <= rminr <= rmaxr
        right_valid &= node.val < rminl

    is_valid = left_valid and right_valid
    return is_valid, (lminl, lmaxr), (rminl, rmaxr)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid_node(root)[0]


TEST_CALL = Solution().isValidBST
null = None
CASES = (
    # ## expected, *input_args
    (True, [2,1,3]),
    (False, [5,1,4,null,null,3,6]),
    (False, [5,4,6,null,null,3,7]),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, (expected, input) in enumerate(cases):
        root = construct_tree(input)
        result = TEST_CALL(root)
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
test()
