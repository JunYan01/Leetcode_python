2Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        cur = node
        
        remains = 0 
        while remains>0 or l1 or l2:
            if l1:
                remains += l1.val
                l1 = l1.next
            if l2:
                remains += l2.val 
                l2 = l2.next
            
            cur.next = ListNode(remains % 10)
            cur = cur.next
            # print(remains % 10)
            remains =  remains // 10
            
            
        return node.next