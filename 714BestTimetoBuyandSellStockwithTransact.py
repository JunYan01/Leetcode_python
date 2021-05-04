714  Best Time to Buy and Sell Stock with Transaction Fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
#         N = len(prices)
#         if N == 0:
#             return 0
#         a, b = 0, -prices[0]
#         # i = 0
#         # print(i,dp[i]) 
        
#         for i in range(1,N):
#             a = max(a,b+prices[i]-fee)
#             b = max(b,a-prices[i])
        
#         return a
        one_buy = float('inf')
        one_sell = 0
        for p in prices:
            one_buy = min(one_buy, p-one_sell)
            one_sell = max(one_sell, p-one_buy-fee)
            # print(p,one_buy, one_sell)
        return one_sell
        # return one_sell if len(prices) else 0