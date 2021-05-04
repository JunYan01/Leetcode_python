138	Copy List with Random Pointer 
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # if not head:
        #     return head
        # cur = head
        # while cur:
        #     newNode = Node(cur.val,cur.next,cur.random)
        #     cur.next = newNode
        #     cur = newNode.next
        # cur = head
        # while cur:
        #     cur = cur.next
        #     if cur and cur.random:
        #         cur.random = cur.random.next
        #     cur = cur.next
        # cur = head.next
        # while cur.next:
        #     cur.next = cur.next.next
        #     cur = cur.next
        # return head.next
        
        if not head:
            return head
        cur = head
        while cur:
            newNode = Node(cur.val,cur.next,cur.random)
            cur.next = newNode
            cur = newNode.next
        cur = head
        while cur:
            cur = cur.next
            if cur and cur.random:
                cur.random = cur.random.next
            cur = cur.next
        cur = head.next
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return head.next