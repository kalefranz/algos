import json


class ListNode(object):
    # ListNode val is an integer

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.has_cycle(self):
            return "Error - Found cycle in the ListNode"

        return (
            "ListNode{val: " + str(self.val) + ", next: " + str(self.next) + "}"
        )

    @staticmethod
    def _array_to_list_node(tokens):
        head = None
        now = None
        for token in tokens:
            if head is None:
                head = ListNode(token)
                now = head
            else:
                now.next = ListNode(token)
                now = now.next
        return head

    @staticmethod
    def has_cycle(head):
        nodes = set()
        now = head
        while now is not None:
            if now in nodes:
                return True
            nodes.add(now)
            now = now.next
        return False

    @staticmethod
    def deserialize(s):
        tokens = json.loads(s)
        return ListNode._array_to_list_node(tokens)

    @classmethod
    def serialize(cls, head):
        if cls.has_cycle(head):
            return "Error - Found cycle in the ListNode"

        now = head
        buffer = []
        while now is not None:
            buffer.append(str(now.val))
            now = now.next
        return "[%s]" % ",".join(buffer)

    def as_py_list(self):
        def itr():
            node = self
            while node:
                if node.val:
                    yield node.val
                node = node.next
        return list(itr())
