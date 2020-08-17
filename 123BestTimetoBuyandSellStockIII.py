# 123. Best Time to Buy and Sell Stock III


# n = len(prices)
        # maxK = 2
        # dp =[ [[0,0] for _ in range(maxK+1)] for _ in range(n+1)]
        # # print(dp)
        # for i in range(n+1):
        #     # for k in range(maxK,-1,-1):
        #     for k in range(maxK+1):
        #         if i == 0:
        #             dp[i][k][0] = 0
        #             dp[i][k][1] = float('-inf')
        #         if k == 0:
        #             dp[i][k][0] = 0
        #             dp[i][k][1] = float('-inf')
        #         if i>=1 and k>=1:
        #             dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+prices[i-1])
        #             dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i-1])
        # print(dp)
        # return dp[n][maxK][0]
        one_buy = two_buy = float('inf')
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy, p)
            one_profit = max(one_profit, p - one_buy)
            two_buy = min(two_buy, p - one_profit)
            two_profit = max(two_profit, p - two_buy)
        return two_profit