# 1510. Stone Game IV
from numpy import sqrt,floor

class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        cache = {}
        
        from functools import lru_cache
        @lru_cache(None)
        def helper(k) -> bool:
            
            if sqrt(k) %1 == 0:
                cache[k] = True
                return True
            for i in range(int(floor(sqrt(k))),0,-1):
                if k-i*i in cache.keys():
                    if cache[k-i*i] is False:
                        cache[k] = True
                        return True
                if helper(k-i*i) == False:
                    cache[k] = True
                    return True
            cache[k] = False
            return False
        # return helper(n)

        a = helper(n)
        # print(cache)
        return a


        # dp = [False] * (n + 1)
        # for i in range(1, n + 1):
        #     dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        # return dp[-1]
        
a = Solution()
a.winnerSquareGame(8359)