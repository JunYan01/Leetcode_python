23  Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# from Queue import PriorityQueue
# import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # q = []
        # for i in range(len(lists)):
        #     if lists[i]:
        #         heapq.heappush(q, (lists[i].val, i))
        #         lists[i] = lists[i].next
        # res = ListNode()
        # cur = res
        # while q:
        #     val, i = heapq.heappop(q)
        #     cur.next = ListNode(val)
        #     cur = cur.next
        #     if lists[i]:
        #         heapq.heappush(q, (lists[i].val, i))
        #         lists[i] = lists[i].next
        # return res.next
        
        
        
        # dummy = ListNode(None)
        # curr = dummy
        # q = PriorityQueue()
        # for node in lists:
        #     if node: q.put((node.val,node))
        # while q.qsize()>0:
        #     curr.next = q.get()[1]
        #     curr=curr.next
        #     if curr.next: q.put((curr.next.val, curr.next))
        # return dummy.next
        
        # curr = head = ListNode(0)
        # queue = []
        # count = 0
        # for l in lists:
        #     if l is not None:
        #         count += 1
        #         heapq.heappush(queue, (l.val, count, l))
        # while len(queue) > 0:
        #     _, _, curr.next = heapq.heappop(queue)
        #     curr = curr.next
        #     if curr.next is not None:
        #         count += 1
        #         heapq.heappush(queue, (curr.next.val, count, curr.next))
        # return head.next 
        
        
#         def mergeTwoLists(a: ListNode, b: ListNode) -> ListNode:
#             curr = head = ListNode(0)
#             while a and b:
#                 if a.val <= b.val:
#                     curr.next = a
#                     a = a.next
#                 else:
#                     curr.next = b
#                     b = b.next
#                 curr = curr.next
#                 # print(curr.val)
            
#             if not a:
#                 curr.next = b
#             else:
#                 curr.next = a
#             # print('Finished 2 merge list')
#             return head.next
        
#         def mergeKListsHelper(lists: List[ListNode], left: int, right: int) ->ListNode:
#             if right < left:
#                 return None
#             if right == left:
#                 return lists[left]
#             if left + 1 == right:
#                 return mergeTwoLists(lists[left], lists[right]);
#             m = left + (right - left)//2
#             l1 = mergeKListsHelper(lists, left, m);
#             l2 = mergeKListsHelper(lists, m + 1, right)
#             # print(left, m, right)
#             return mergeTwoLists(l1,l2)
        
#         return mergeKListsHelper(lists, 0, len(lists) - 1)
        