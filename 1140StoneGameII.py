# 1140. Stone Game II

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        # N = len(piles)
        # for i in range(N - 2, -1, -1):
        #     piles[i] += piles[i + 1]
        # from functools import lru_cache
        # @lru_cache(None)
        # def dp(i, m):
        #     if i + 2 * m >= N: return piles[i]
        #     return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        # return dp(0, 1)
        
#         N = len(piles)
#         for i in range(N - 2, -1, -1):
#             piles[i] += piles[i + 1]

#         cache = {}
        
#         def dp(i, m):
#             if i + 2 * m >= N:
#                 cache[(i, m)] = piles[i]
#                 return piles[i]
#             res = piles[i] - min(cache.get((i + x, max(m, x)), dp(i + x, max(m, x))) for x in range(1, 2 * m + 1))
#             cache[(i, m)] = res
#             return res
#         return dp(0, 1)
        
        
        
        N = len(piles)
        for i in range(N - 2, -1, -1):
            piles[i] += piles[i + 1]
        cache = {}
        
        def dp(i, m):
            if i + 2 * m >= N:
                cache[(i,m)] = piles[i]
                # print(i,m,cache[(i,m)])
                return piles[i]
            res = float('inf')
            for x in range(1, 2 * m + 1):
                M = max(m,x)
                if (i+x,M) in cache.keys():
                    res = min(res,cache[(i+x, M)])
                else:
                    cache[(i+x, M)] = dp(i + x, M)
                    res = min(res,cache[(i+x, M)])
            
            cache[(i, m)] = piles[i] - res
            # print(i,m,cache[(i,m)])
            return cache[(i, m)]
        return dp(0, 1)
    
            
        