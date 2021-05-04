141  Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
#         fast = slow = head
#         while fast and slow:
#             try:
#                 fast = fast.next.next
#                 slow = slow.next
#             except:
#                 return False
# #             fast slow cannot be None at same time
#             if fast == slow:
#                 return True

        cache = set()
        curr = head
        cache.add(curr)
        while curr:
            curr = curr.next
            if curr in cache:
                return True
            cache.add(curr)
            
        return False
        
        