234Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
#         node = head
#         count = 0
#         while node:
#             count += 1
#             node = node.next
#         node = head
#         pre = None
#         for i in range(count //2):
#             node.next, node, pre = pre, node.next, node
#             # print(node.val,pre.val)
        
#         if count%2 ==1 :
#             node = node.next
#         while node:
#             # print(node.val, pre.val)
#             if node.val != pre.val:
#                 return False
#             node, pre = node.next, pre.next
#         # print(count)
#         return True
        node = head
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        n = len(arr)
        # print(arr)
        for i in range(n//2):
            if arr[i] != arr[n-1-i]:
                return False
        return True
        