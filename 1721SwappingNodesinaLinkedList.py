1721Swapping Nodes in a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        count = 0
        while curr:
            if count == k - 1:
                firstPrev = curr
            curr = curr.next
            count += 1
        n = count - 1
        curr = dummy
        count = 0
        while curr:
            if count == n - k :
                secondPrev = curr
                break
            curr = curr.next
            count += 1
        
        # print(firstPrev.val, secondPrev.val, k , n, n-k)
        firstPrev.next, secondPrev.next = secondPrev.next, firstPrev.next
        firstPrev, secondPrev = firstPrev.next, secondPrev.next
        firstPrev.next, secondPrev.next = secondPrev.next, firstPrev.next
        return dummy.next
        
        