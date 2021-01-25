# 526. Beautiful Arrangement


class Solution:
    def countArrangement(self, n: int) -> int:
#         def dfs(num, cur, count):
#             if cur == 0:
#                 count += 1
#                 print(num)
#                 return count
            
#             for i in range(cur,0,-1):
#                 num[i], num[cur] = num[cur], num[i]
#                 if num[cur] % cur == 0 or cur % num[cur] == 0:
#                     count = dfs(num, cur-1, count)
#                 num[i], num[cur] = num[cur], num[i]
                
#             return count
        
#         return dfs(list(range(n+1)),n,0)
    
#         def dfs(num, cur):
#             if cur == 0:
#                 res[0] += 1
#                 return
#             for i in range(cur, 0, -1):
#                 num[i], num[cur] = num[cur], num[i]
#                 if num[cur] % cur == 0 or cur % num[cur] == 0:
#                     dfs(num, cur - 1)
#                 num[cur], num[i] = num[i], num[cur]

#         res = [0]
#         dfs([i for i in range(n + 1)], n)
#         return res[0]

        def perm(num, cur):
            if cur == 0:
                print(num[1:])
                return
            
            for i in range(cur,0,-1):
                num[i], num[cur] = num[cur], num[i]
                perm(num, cur-1)
                num[i], num[cur] = num[cur], num[i]
                
            return 
        
        perm(list(range(n+1)),n)
        return 0