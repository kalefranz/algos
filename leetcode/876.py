from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 0   0
# 0,1  1
# 0,1,2  1
# 0,1,2,3  2
# 0,1,2,3,4  2

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = 0
        middle = tail = head
        while tail.next:
            q += 1
            if q % 2 == 1:
                middle = middle.next
            tail = tail.next
        return middle
