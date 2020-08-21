# 206. Reverse Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
#         curr = head
#         tail = None
#         if not head:
#             return None
#         while curr.next:
#             # print(curr.val)
# #             next = curr.next
# #             curr.next = tail
            
# #             tail = curr
# #             curr = next
#             tail,curr.next,curr =  curr, tail, curr.next
#         curr.next = tail
#         return curr
        # curr, tail = head, None
        # if not head:
        #     return head
        # while curr.next:
        #     tail,curr.next,curr =  curr, tail, curr.next
        # curr.next = tail
        # return curr
        
        if not head:
            return head
        

        prev, curr = None, head
        while curr:       
            # next = curr.next
            # curr.next = prev
            # prev = curr
            # curr = next
            prev,curr.next,curr =  curr, prev, curr.next
            # curr.next,prev,curr =  prev, curr, curr.next

        return prev
        

#         def reverseListHelper(head) -> ListNode:
#             if not head:
#                 return head
#             prec = tail = head
#             while tail.next:
#                 prec = tail
#                 tail = tail.next
#             prec.next = None
#             # print(prec.val,tail.val)
#             if prec is tail:
#                 return tail
#             tail.next = reverseListHelper(head) 
            
#             return tail
                
#         return reverseListHelper(head)

        # def reverseListHelper(node) -> ListNode:
        #     if not node:
        #         return node
        #     if not node.next:
        #         return node
        #     last = reverseListHelper(node.next)
        #     node.next.next = node
        #     node.next = None
        #     return last
        # return reverseListHelper(head)
        
        
