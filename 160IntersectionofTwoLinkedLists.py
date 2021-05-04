160  Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # lenA, lenB = 0, 0
        # node = headA
        # if node:
        #     lenA = 1
        # while node.next:
        #     node = node.next
        #     lenA += 1
        node = headA
        # lenA = 1 if node else 0
        if node:
            lenA = 1
        else:
            return None
        while node.next:
            node = node.next
            lenA += 1
        node2 = headB
        # lenB = 1 if node2 else 0
        if node2:
            lenB = 1
        else:
            return None
        while node2.next:
            node2 = node2.next
            lenB += 1
        if node is not node2:
            return None
        print(lenA, lenB)
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenA>0:
            if headA is headB:
                return headA
            else:
                lenA -= 1
                headA = headA.next
                headB = headB.next
        # return None 
            
        
        