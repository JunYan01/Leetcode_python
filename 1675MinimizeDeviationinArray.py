1675. Minimize Deviation in Array

from queue import PriorityQueue

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Pre-doubling all odd numbers
#         Tree Set 来做
#         s = set()
#         for x in nums:
#             s.add(2*x if x%2 else x)
#         # print(s)
#         m = max(s)
#         ans = m - min(s)
#         print(s)
#         while m %2 == 0:
#             s.add(m//2)
#             s.remove(m)
#             m = max(s)
#             ans = min(ans, m - min(s))
        
#         return ans

#         PriorityQueue 来做
        q = PriorityQueue()
        lo = float('inf')
        for x in nums:
            x = 2*x if x%2 else x
            q.put(-x)
            lo = min(lo,x)
            
        ans = - q.queue[0] - lo
        while -q.queue[0] %2 == 0:
            x = -q.get()
            q.put(-x//2)
            lo = min(x//2,lo)
            ans = min(ans, -q.queue[0]-lo)
        return ans
        