279  Perfect Squares

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        q = deque()
        q.append(n)
        count = 0
        while q:
            _q = set()
            for _ in range(len(q)):
                target = q.popleft()
                if target == 0:
                    return count
                i = 1
                while i**2 <= target:
                    rest = target - i**2
                    _q.add(rest)
                    i += 1
            count += 1
            q = deque(_q)
#         arr = [float('inf')]*(n+1)
#         arr[0] = 0
#         arr[1] = 1
#         squares = set([x**2 if x**2<=n else 1 for x in range(n//2+1)])
#         print(squares)

#         for i in range(2,n+1):
#             for s in squares:
#                 if s<=i:
#                     arr[i] = min(arr[i],arr[i-s]+1)
#         # print(arr)
#         return arr[n]
    
    
#         arr = [float('inf')]*(n+1)
#         arr[0] = 0
#         arr[1] = 1
#         for i in range(2,n+1):
#             j = 1
#             while j*j<=i:
#                 arr[i] = min(arr[i],arr[i-j*j]+1)
#                 j += 1
#         # print(arr)
#         return arr[n]

#         queue = [n]
#         squares = set([x**2 if x**2<=n else 1 for x in range(1,n//2+2)])
#         # print(squares)
#         level = [n]
#         count = 0
#         while level:
#             level = []
#             count += 1
#             while queue:
#                 x = queue.pop(0)
            
#                 for s in squares:
#                     if x - s == 0:
#                         return count
#                     elif x > s:
#                         level.append(x-s)
#             queue = level
            
        
        
        
        