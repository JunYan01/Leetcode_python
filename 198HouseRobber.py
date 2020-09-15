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

        #         n = len(nums)
#         if n == 0: return 0
#         dp = [[0] * n for _ in range(n)]
        
#         for i in range(n-1,-1,-1):
#             dp[i][i] = nums[i]
#             if i + 1 < n:
#                 dp[i][i+1] = max(nums[i],nums[i+1])
#             for j in range(i+2,n):
#                 dp[i][j] = max(dp[i][j-2] + nums[j],dp[i][j-1])
                
#         return dp[0][n-1]


        # n = len(nums)
        # if n == 0: return 0
        # if n == 1: return nums[0]
        # dp = [0]*n
        # dp[0] = nums[0]
        
        # dp[1] = max(nums[0],nums[1])
        # for i in range(2,n):
        #     dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        
        # return dp[n-1]

        dp0 = dp1 = 0
        for i in range(len(nums)):
            dp0, dp1 = dp1, max(dp0+nums[i],dp1)
        return dp1

        

a = Solution()
a.rob([1,2,3,1])