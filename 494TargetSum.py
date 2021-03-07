494  Target Sum

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         n = len(nums)
#         # print(self.count, S)
#         def dfs(i, res):
#             # global count
#             # print(self.count)
            
#             if i == n:
#                 if res == 0:
#                     self.count += 1
#                 return
#             dfs(i+1, res - nums[i])
#             dfs(i+1, res + nums[i])
#             return
#         self.count = 0
#         dfs(0,S)
        
#         return self.count

#         n = len(nums)
#         # print(self.count, S)
#         def dfs(i,x, res):
#             # global count
#             # print(self.count)
#             if x < abs(res):
#                 return
#             if i == n:
#                 if res == 0:
#                     self.count += 1
#                 return
#             dfs(i+1, x - nums[i], res - nums[i])
#             dfs(i+1, x - nums[i], res + nums[i])
#             return
#         self.count = 0
#         x = sum(nums)
#         dfs(0,x,S)  
        
#         return self.count


#         s = sum(nums)
#         if s < abs(S):
#             return 0
#         n = len(nums)
#         ways = [[0] * (2*s+1) for _ in range(n+1)]
#         ways[0][s] = 1
#         for i in range(n):
#             for j in range(nums[i],2*s+1-nums[i]):
#                 ways[i+1][j+nums[i]] += ways[i][j]
#                 ways[i+1][j-nums[i]] += ways[i][j]
        
#         return ways[n][S+s]

#         s = sum(nums)
#         if s < abs(S):
#             return 0
#         n = len(nums)
#         ways = [0] * (2*s+1)
#         ways[s] = 1
#         ways2 = [0] * (2*s+1)
#         for i in range(n):
#             for j in range(nums[i],2*s+1-nums[i]):
#                 ways2[j+nums[i]] += ways[j]
#                 ways2[j-nums[i]] += ways[j]
#             ways = ways2
#             ways2 = [0] * (2*s+1)
        
#         return ways[S+s]

#         s = sum(nums)
#         if s < abs(S):
#             return 0
#         n = len(nums)
#         ways = [0] * (2*s+1)
#         ways[s] = 1
#         lastSum = set()
#         lastSum.add(s)
#         for i in range(n):
#             newSum = set()
#             ways2 = [0] * (2*s+1)
#             for j in lastSum:
#                 newSum.add(j+nums[i])
#                 newSum.add(j-nums[i])
#                 ways2[j+nums[i]] += ways[j]
#                 ways2[j-nums[i]] += ways[j]
#             lastSum = newSum
#             ways = ways2
            
#         return ways[S+s]
        
#         s = sum(nums)
#         if s < abs(S):
#             return 0
#         n = len(nums)
#         ways = defaultdict(int)
#         ways[0] = 1
#         lastSum = set()
#         lastSum.add(0)
#         for i in range(n):
#             newSum = set()
#             ways2 = defaultdict(int)
#             for j in lastSum:
#                 newSum.add(j+nums[i])
#                 newSum.add(j-nums[i])
#                 ways2[j+nums[i]] += ways[j]
#                 ways2[j-nums[i]] += ways[j]
#             lastSum = newSum
#             ways = ways2
            
#         return ways[S]


#         s = sum(nums)
#         if s < abs(S):
#             return 0
#         n = len(nums)
#         ways = defaultdict(int)
#         ways[0] = 1
#         lastSum = set()
#         lastSum.add(0)
#         for i in range(n):
#             newSum = set()
#             ways2 = defaultdict(int)
#             remains = s - nums[i]
#             for j in lastSum:
#                 # print(j)
#                 if abs(j + nums[i]) + remains >=abs(S):
#                     newSum.add(j+nums[i])
#                     ways2[j+nums[i]] += ways[j]
                
#                 if abs(j - nums[i]) + remains >=abs(S):
#                     newSum.add(j-nums[i])
#                     ways2[j-nums[i]] += ways[j]
#             lastSum = newSum
#             ways = ways2
            
#         return ways[S]

# sum(P) - sum(N) = target, 2*sum(P) = target + sum(nums), target + sum(nums) should be even , 0-1 pack
#  V_i possible sums using any subset of first i elements
#  V_0 = {0}
#  V_i = V_{i-1} union V_{i-1} + a_i
#  dp[i][j] := whether we can use fist i elements to sum up to j(j in V_i)
#  change whether to number
#  Push: scan j for dp[i-1]
#  for i in 1..n:
#    for j in 0..S:
#       if dp[i-1][j]:
#          dp[i][j+a_i] = True
#  (1) dp[i] = dp[i-1] make a copy
#  (2) dp[i][j+a_i] += dp[i-1][j]

#  Pull: scan j for dp[i]
#  for i in 1..n:
#    for j in 0..S:
#          dp[i][j+a_i] = dp[i-1][j] or dp[i-1][j-a_i]
#  change whether to number
#   dp[i][j] = dp[i-1][j] + dp[i-1][j-a_i] 
#   special trick: use only one array to solve the problem
#   dp[j] += dp[j - num_i] scan j in reverse order
        # S = abs(S)
        # sumValue = sum(nums)
        # if sumValue < S or (S+sumValue)%2 != 0:
        #     return 0
        # target = (S+sumValue)//2
        # dp = [0]*(target+1)
        # dp[0] = 1
        # for i in nums:
        #     dp_i = dp.copy()
        #     for j in range(target - i+1):
        #         dp_i[j+i] += dp[j]
        #     dp, dp_i = dp_i, dp
        # return dp[target]
        
# Excellent
# 如果记住 dp
        S = abs(S)
        sumValue = sum(nums)
        if sumValue < S or (S+sumValue)%2 != 0:
            return 0
        target = (S+sumValue)//2
        dp = [0]*(target+1)
        dp[0] = 1
        for num in nums:
            for j in range(target, num-1,-1):
                dp[j] += dp[j-num]
        return dp[target]