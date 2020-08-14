# 142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        try:
            slow = head.next
            quick = head.next.next

            while slow != quick:
                slow = slow.next
                quick = quick.next.next
# First meet
            quick = head
            while slow != quick:
                slow = slow.next
                quick = quick.next
# Second meet will taken place at the starting the circle
            return slow
        except:
            return None
        