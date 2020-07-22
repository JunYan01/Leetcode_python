# 1406. Stone Game III
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
#         n = len(stoneValue)
#         # print(stoneValue)

#         for i in range(n - 2, -1, -1):
#             stoneValue[i] += stoneValue[i + 1]
#         stoneValue.append(0)
        
#         # print(stoneValue)
#         cache = {n:(0,0)}
        
        
#         def dp(i):
#             if i in cache.keys():
#                 return cache[i]
#             if i == n-1:
#                 cache[i] = (stoneValue[i],0)
#                 # print(i,cache[i])
#                 return cache[i]
#             if i == n-2:
#                 choice1 = dp(i+1)
#                 # choice = max(stoneValue[i]-stoneValue[i+1],stoneValue[i])
#                 choice = stoneValue[i]
#                 choice = max(choice,stoneValue[i] - stoneValue[i+1] +choice1[1])
#                 cache[i] = (choice,stoneValue[i]-choice)
#                 # print(i,cache[i])
#                 return cache[i]
            
#             choice1 = dp(i+1)
#             choice2 = dp(i+2)
#             choice3 = dp(i+3) 
#             choice = stoneValue[i]-stoneValue[i+1]+ choice1[1]
#             choice = max(choice, stoneValue[i]-stoneValue[i+2]+ choice2[1])
#             choice = max(choice, stoneValue[i]-stoneValue[i+3]+ choice3[1])
#             cache[i] = (choice,stoneValue[i]-choice)
#             # print(i,cache[i])
#             return cache[i]
        
#         return "Alice" if dp(0)[0]>dp(0)[1] else ("Bob" if dp(0)[0]<dp(0)[1] else "Tie")

        n = len(stoneValue)
        print(stoneValue)

        for i in range(n - 2, -1, -1):
            stoneValue[i] += stoneValue[i + 1]
        stoneValue.append(0)
        # print(stoneValue)
        stoneValue = stoneValue[::-1]
        # print(stoneValue)
        dp = [(0,0)]*(n+1)
        
        if n == 0:
            return 'Tie'
        i = 1
        dp[1] = (stoneValue[1],0)
        # print(i,dp[i])
        if n == 1:
            choice = dp[1]
            return "Alice" if choice[0]>choice[1] else ("Bob" if choice[0]<choice[1] else "Tie")
        i = 2
        choice1 = dp[i-1]
        choice = stoneValue[i] - stoneValue[i-2]
        choice = max(choice,stoneValue[i] - stoneValue[i-1] +choice1[1])
        dp[i] = (choice,stoneValue[i]-choice)
        # print(i,dp[i])

        if n == 2:
            return "Alice" if choice[0]>choice[1] else ("Bob" if choice[0]<choice[1] else "Tie")
        for i in range(3,n+1):
            choice1 = dp[i-1]
            choice2 = dp[i-2]
            choice3 = dp[i-3]
            choice = stoneValue[i]-stoneValue[i-1]+ choice1[1]
            choice = max(choice, stoneValue[i]-stoneValue[i-2]+ choice2[1])
            choice = max(choice, stoneValue[i]-stoneValue[i-3]+ choice3[1])
            dp[i] = (choice,stoneValue[i]-choice)
            # print(i,dp[i])
        
        return "Alice" if dp[n][0]>dp[n][1] else ("Bob" if dp[n][0]<dp[n][1] else "Tie")               
                    