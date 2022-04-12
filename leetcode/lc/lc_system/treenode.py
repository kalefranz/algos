"""
location: /leetcode/precompiled/treenode.py



====> code for Node in 116

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def _driver():

    SEPARATOR = "\x1b\x09\x1d"
    f = open("user.out", "wb", 0)
    lines = __Utils__().read_lines()

    def _array_to_tree_node(tokens):
        if not tokens:
            return None
        n = len(tokens)
        root = Node(tokens[0])
        que = [root]
        head = 0
        for i in range(1, n, 2):
            if tokens[i] is not None:
                node = Node(tokens[i])
                que[head].left = node
                que.append(node)
            if i + 1 < n and tokens[i + 1] is not None:
                node = Node(tokens[i + 1])
                que[head].right = node
                que.append(node)
            head += 1
        return root

    def deserializeNode(s):
        tokens = json.loads(s)
        return _array_to_tree_node(tokens)

    def serializeNode(root):
        s = ""
        level = root
        while (level is not None):
            now = level
            level = None
            while (now is not None):
                s += str(now.val) + ","
                if level is None:
                    if now.left is not None:
                        level = now.left
                    elif now.right is not None:
                        level = now.right
                now = now.next
            s += "#,"
        return "[%s]" % s[:-1]

"""
from collections import defaultdict, deque
from functools import cached_property
import json


class TreeNode:
    NODE_WIDTH = 3
    # TreeNode val is an integer

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.has_cycle(self):
            return "Error - Found cycle in the TreeNode"
        args = [self.val]
        kwargs = {}
        if self.left:
            kwargs["l"] = self.left.val
        if self.right:
            kwargs["r"] = self.right.val
        formatted_str = ",".join(map(str, args))
        if kwargs:
            formatted_str += "," + ",".join(f"{k}={v}" for k, v in kwargs.items())
        formatted_str = f"TNode<{formatted_str}>"
        return formatted_str

    @classmethod
    def _array_to_tree_node(cls, tokens):
        if not tokens:
            return None
        n = len(tokens)
        root = cls(tokens[0])
        que = [root]
        head = 0
        for i in range(1, n, 2):
            if tokens[i] is not None:
                node = cls(tokens[i])
                que[head].left = node
                que.append(node)
            if i + 1 < n and tokens[i + 1] is not None:
                node = cls(tokens[i + 1])
                que[head].right = node
                que.append(node)
            head += 1
        return root

    @classmethod
    def deserialize(cls, s):
        tokens = json.loads(s)
        return cls._array_to_tree_node(tokens)

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

    @cached_property
    def depth(self):
        def _depth(node):
            if node.left is None and node.right is None:
                return 1
            if node.right is None:
                return 1 + _depth(node.left)
            if node.left is None:
                return 1 + _depth(node.right)
            return 1 + max(_depth(node.left), _depth(node.right))
        return _depth(self)

    def _format_str_indv(self):
        width = self.NODE_WIDTH * 2 ** self.depth
        disp = f"{self.val}"
        _formatted_str = f"{disp:^{width}}"
        return _formatted_str

    def format_str(self):
        d = defaultdict(list)
        def _format_str(node):
            if node is None:
                return
            d[node.depth].append(node._format_str_indv())
            _format_str(node.left)
            _format_str(node.right)
        _format_str(self)

        builder = ["".join(d[k]) for k in reversed(sorted(d.keys()))]
        # builder[:] = [f"{b}  {len(b)}" for b in builder]
        formatted_str = "\n".join(builder)
        return formatted_str

    def as_py_list(self):
        def itr():
            queue = deque([self])
            while queue:
                node = queue.popleft()
                if node:
                    yield node.val
                    queue.append(node.left)
                    queue.append(node.right)
        return list(itr())


class SkipNode(TreeNode):

    def __init__(self, val=0, left=None, right=None, next=None):
        super().__init__(val, left, right)
        self.next = next

    def __repr__(self):
        formatted_str = super().__repr__()
        formatted_str = "Sk" + formatted_str[1:]
        if self.next:
            formatted_str = formatted_str[:-1] + f",n={self.next.val}>"
        return formatted_str

    def _format_str_indv(self):
        width = self.NODE_WIDTH * 2 ** self.depth
        disp = f"{self.val}"
        if self.next:
            disp += f"→{self.next.val}"
        _formatted_str = f"{disp:^{width}}"
        return _formatted_str

    @classmethod
    def serialize(cls, root):
        # from "/leetcode/user_code/prog_joined.py" for problem 116
        s = ""
        level = root
        while (level is not None):
            now = level
            level = None
            while (now is not None):
                s += str(now.val) + ","
                if level is None:
                    if now.left is not None:
                        level = now.left
                    elif now.right is not None:
                        level = now.right
                now = now.next
            s += "#,"
        return "[%s]" % s[:-1]

    def as_py_list(self):
        def itr():
            node = self
            first_next_level = self.left
            while node:
                yield node.val
                if node.next is None:
                    yield None
                    node = first_next_level
                    first_next_level = node.left if node else None
                else:
                    node = node.next
        return list(itr())
