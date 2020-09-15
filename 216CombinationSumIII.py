# 216CombinationSumIII.py

class Solution:
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         if n> (19 - k)*k/2 or n > 45 or k>9:
#             return []
        
#         def comb(k,n,res,cache):
#             # print(k,n,res)
#             if k == 0 and n == 0:
#                 cache.append(res[:])
#                 # print(cache,res)
#                 return cache
#             if n> (19 - k)*k/2 or n > 45 or k>9 or n<0 or k<0:
#                 return cache
            
#             minValue = max(res) +1 if res != [] else 1
#             if minValue >9:
#                 return cache
#             for i in range(minValue,10):
#                 if n-i<0 or k-1<0:
#                     break
#                 res.append(i) 
#                 cache = comb(k-1,n-i,res,cache)
#                 res.remove(i)
#             return cache
        
#         # print(cache)
#         cache = []
#         cache = comb(k,n,[],cache)
#         return cache

#         ret = []
#         self.dfs(list(range(1, 10)), k, n, [], ret)
#         return ret
    
#     def dfs(self, nums, k, n, path, ret):
#         if k < 0 or n < 0:
#             return 
#         if k == 0 and n == 0:
#             ret.append(path)
#         for i in range(len(nums)):
#             self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ret)


#          def dfs(cur, k, n, tmp):
#             if k == 0:
#                 if n == 0:
#                     res.append(tmp[:])
#                 return
#             for i in range(cur, 10):
#                 if i > n:
#                     return
#                 tmp.append(i)
#                 dfs(i + 1, k - 1, n - i, tmp)
#                 tmp.pop()

#         res = []
#         dfs(1, k, n, [])
#         return res
         

        self.res = []
        self.dfs(1, k, n, [])
        return self.res
    
    
    def dfs(self,cur, k, n, tmp):
        if k == 0:
            if n == 0:
                self.res.append(tmp[:])
            return
        for i in range(cur, 10):
            if i > n:
                return
            tmp.append(i)
            self.dfs(i + 1, k - 1, n - i, tmp)
            tmp.pop()
        return