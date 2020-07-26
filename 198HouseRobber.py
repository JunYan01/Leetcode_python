# 198. House Robber


class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        memo = [-1]*n
        
        from functools import lru_cache    
        @lru_cache(None)
        def dp(i):
            if i>= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            res = max(dp(i+1),nums[i]+dp(i+2))
            memo[i] = res
            print(i,memo[i])
            return res
        
        return dp(0)

#         n = len(nums)
#         dp = [0]*(n+2)
#         for i in range(n-1,-1,-1):
#             dp[i] = max(dp[i+1],nums[i]+dp[i+2])
        
#         return dp[0]

        # n = len(nums)
        # dp1 = 0
        # dp2 = 0
        # if n == 0:
        #     return 0
        # for i in range(n-1,-1,-1):
        #     dp = max(dp1,nums[i]+dp2)
        #     dp2 = dp1
        #     dp1 = dp
        
        # return dp

        

a = Solution()
a.rob([1,2,3,1])