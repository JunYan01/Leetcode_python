# 143. Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
#         #step 1: find middle
#         if not head: return []
#         slow, fast = head, head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         #step 2: reverse second half
#         prev, curr = None, slow.next
#         while curr:
#             nextt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextt    
#         slow.next = None
        
#         #step 3: merge lists
#         head1, head2 = head, prev
#         while head2:
#             nextt = head1.next
#             head1.next = head2
#             head1 = head2
#             head2 = nextt


#         if not head:
#             return 
        
#         # find the middle of linked list [Problem 876]
#         # in 1->2->3->4->5->6 find 4 
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next 
            
#         # reverse the second part of the list [Problem 206]
#         # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
#         # reverse the second half in-place
#         prev, curr = None, slow
#         while curr:       
#             curr.next, prev, curr = prev, curr, curr.next       

#         # merge two sorted linked lists [Problem 21]
#         # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
#         first, second = head, prev
#         while second.next:
#             first.next, first = second, first.next
#             second.next, second = first, second.next

            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2


        
        if not head:
            return
        node = head
        queue = []
        while node:
            queue.append(node)
            node = node.next
        
        node = head
        print(queue[-1].val)
        while node is not queue[-1] and node.next is not queue[-1]:
            
            nodeNext = node.next
            nodeEnd = queue.pop()
            
            # print(node.val,nodeEnd.val)
            
            node.next = nodeEnd
            nodeEnd.next = nodeNext
            
            node = nodeNext
        queue.pop().next = None
        return
        
            
            
        
        
#         def reorderListHelper(node: ListNode) -> ListNode:
#             if not node or not node.next:
#                 return node
            
#             curr = prec = node
#             headnext = node.next
            
#             while curr.next:
#                 prec = curr
#                 curr = curr.next
#                 # print(node.val,headnext.val, prec.val, curr.val)
            
            
#             if curr is headnext:
#                 return node
            
#             prec.next = None
            
#             node.next = curr
#             curr.next = headnext
#             # print('dfd',node.val,headnext.val, prec.val, curr.val)

#             headnext = reorderListHelper(headnext)
            
#             return node
        
#         return reorderListHelper(head)
        


            
              