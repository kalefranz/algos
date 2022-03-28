"""
location: /leetcode/precompiled/treenode.py
"""

import json


class TreeNode(object):
    # TreeNode val is an integer

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.has_cycle(self):
            return "Error - Found cycle in the TreeNode"

        return (
            "TreeNode{val: "
            + str(self.val)
            + ", left: "
            + str(self.left)
            + ", right: "
            + str(self.right)
            + "}"
        )

    @staticmethod
    def _array_to_tree_node(tokens):
        if not tokens:
            return None
        n = len(tokens)
        root = TreeNode(tokens[0])
        que = [root]
        head = 0
        for i in range(1, n, 2):
            if tokens[i] is not None:
                node = TreeNode(tokens[i])
                que[head].left = node
                que.append(node)
            if i + 1 < n and tokens[i + 1] is not None:
                node = TreeNode(tokens[i + 1])
                que[head].right = node
                que.append(node)
            head += 1
        return root

    @staticmethod
    def deserialize(s):
        tokens = json.loads(s)
        return TreeNode._array_to_tree_node(tokens)

    @classmethod
    def _has_cycle(cls, root, nodes):
        if root is None:
            return False

        if root in nodes:
            return True

        nodes.add(root)
        cycle_exists = cls._has_cycle(root.left, nodes) or cls._has_cycle(
            root.right, nodes
        )
        nodes.remove(root)
        return cycle_exists

    @classmethod
    def has_cycle(cls, root):
        nodes = set()
        return cls._has_cycle(root, nodes)

    @classmethod
    def serialize(cls, root):
        if root is None:
            return "[]"

        if cls.has_cycle(root):
            return "Error - Found cycle in the TreeNode"

        que = [root]
        head = 0
        s = ""
        comma = ""
        while head < len(que):
            if que[head] is None:
                s += comma + "null"
            else:
                s += comma + str(que[head].val)
                que.append(que[head].left)
                que.append(que[head].right)
            comma = ","
            head += 1
        # Delete trailing ",null" suffix.
        while s[-1] == "l":
            s = s[:-5]
        return "[%s]" % s
