# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = float('inf')
        one_sell = 0
        # one_sell = float('-inf')
        for p in prices:
            one_buy = min(one_buy, p)
            one_sell = max(one_sell, p-one_buy)
            # print(p,one_buy, one_sell)
        return one_sell
        # return one_sell if len(prices) else 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         N = len(prices)
#         if N == 0:
#             return 0
#         dp = [[0, 0] for i in range(N)]
#         dp[0] = [0, -prices[0]]
#         # i = 0
#         # print(i,dp[i]) 
        
#         for i in range(1,N):
#             dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
#             dp[i][1] = max(dp[i-1][1],-prices[i])
#             # print(i,dp[i])        
        
#         return dp[N-1][0]
        
#         N = len(prices)
#         if N == 0:
#             return 0
#         dp = [0, -prices[0]]
#         # i = 0
#         # print(i,dp[i]) 
        
#         for i in range(1,N):
#             dp[0] = max(dp[0],dp[1]+prices[i])
#             dp[1] = max(dp[1],-prices[i])
        
#         return dp[0]

        N = len(prices)
        if N == 0:
            return 0
        a, b = 0, -prices[0]
        # i = 0
        # print(i,dp[i]) 
        
        for i in range(1,N):
            a = max(a,b+prices[i])
            b = max(b,-prices[i])
        
        return a