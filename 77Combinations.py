# 77. Combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
#         track = [] if k <= n//2 else [x for x in range(1,n+1)]
#         res = [] 

#         def backtrack(n,start,track,res):
#             if track not in res and len(track) == k:
#                 # print(track[:])
#                 res.insert(0,track[:])
#                 return
            
            
#             # res.append(track)
#             # print(res,track)
#             for i in range(start,n):
#                 track.insert(0,i+1)
#                 backtrack(n,i+1,track,res)
#                 track.pop(0)
#             return 
        
#         def backtrack2(n,start,track,res):
#             if track not in res and len(track) == k:
#                 # print(track[:])
#                 res.insert(0,track[:])
#                 return
            
            
#             # res.append(track)
#             # print(res,track)
#             for i in range(0,start+1):
#                 # print(i,start)
#                 a = track.pop(i)
#                 backtrack2(n,i-1,track,res)
#                 track.insert(i,a)
#             return 
        
#         if k <= n//2:
#             # print('adfadfa')
#             backtrack(n,0,track,res)
#         else:
#             # print('22222adfadfa')
#             backtrack2(n,n-1,track,res)
#         # print(len(res))
#         return res
        res = []
        a = []
        for bitmask in range(1<<n):
            if bin(bitmask).count('1') == k:
                # print(bin(bitmask))
                a = [i+1 for i in range(n) if bitmask & 1<<i]
                # print(a)
                res.append(a)
                
        return res