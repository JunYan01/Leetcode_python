82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = ListNode(0)
        cur = node
        
        while head:
            curValue = head.val
            if not head.next:
                cur.next = head
                print('1',head.val)
                break
            if head.next.val == curValue:
                head = head.next
                while head and head.val == curValue:
                    head = head.next
            else:
                cur.next = head
                print('2',head.val)
                head = head.next
                cur = cur.next
                cur.next = None
                
        return node.next