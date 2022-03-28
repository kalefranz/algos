# from typing import *

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_leaf(self, node):
        return node.left is None and node.right is None

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        while not self.is_leaf(root):
            result.append(self._helper(root))
        result.append([root.val])
        return result

    def _helper(self, root):
        leaves = []
        stack = [root]
        q = 0
        while node := (stack and stack.pop()):
            if node.left is not None:
                if self.is_leaf(node.left):
                    leaves.append(node.left.val)
                    node.left = None
                else:
                    stack.append(node.left)
            if node.right is not None:
                if self.is_leaf(node.right):
                    leaves.append(node.right.val)
                    node.right = None
                else:
                    stack.append(node.right)
            print(f"{q:>3}{node.val:>10}")
            lval = node.left and node.left.val or -666
            rval = node.right and node.right.val or -666
            print(f"{lval:>8}{rval:>8}")
            q += 1
        return leaves

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

