# 92. Reverse Linked List II


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
#         successor = None
#         def reverseN(node,n):
#             nonlocal successor
#             if n == 1:
#                 successor = node.next
#                 return node
            
#             last = reverseN(node.next,n-1)
#             node.next.next = node
#             node.next = successor
            
#             return last
        
#         return reverseN(head,n)


#         def reverseN(node,n):
#             if n == 1:
#                 successor = node.next
#                 return node,successor
            
#             last,successor = reverseN(node.next,n-1)
#             node.next.next = node
#             node.next = successor
            
#             return last,successor
        
#         last,b = reverseN(head,n)
        
#         return last


        def reverseN(node,n):
            if n == 1:
                successor = node.next
                return node,successor
            
            last,successor = reverseN(node.next,n-1)
            node.next.next = node
            node.next = successor
            
            return last,successor
        
        if m ==1:
            last, successor = reverseN(head,n)
            return last
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head
        

