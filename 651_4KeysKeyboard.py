# 651. 4 Keys Keyboard


class Solution:
    def maxA(self, N: int) -> int:
        dp = [0]*(N+1)
        dp[0] = 0
        memo = {}
        memo[0] = ''
        for i in range(1,N+1):
            dp[i] = dp[i-1]+1
            memo[i] = memo[i-1]+'A'
            for j in range(i-1,1,-1):
                if dp[j-2]*(i-j+1) >= dp[i]:
                    memo[i] = memo[j-2]+'LC'+'V'*(i-j)
                dp[i] = max(dp[i],dp[j-2]*(i-j+1))
#             count = 0
#             j = i-1
#             while j>1 and count < 3:
#                 if dp[j-2]*(i-j+1) >= dp[i]:
                    
#                     memo[i] = memo[j-2]+'LC'+'V'*(i-j)
                
#                 dp[i] = max(dp[i],dp[j-2]*(i-j+1))
#                 count += 1
#                 j -= 1
                
                    
            print(i,dp[i],memo[i])
        
        return dp[N]

################################################
############ still underwork
################################################
#         (a,b) = divmod(N,4)
#         print(a,b)
#         (a1,b1) = (a-1,b+4) if a>0 else (a,b)
#         print(a1,b1)
            
#         return max(b1*3**a1,b*3**a,(N-3)*2,(N-4)*3,(N-5)*4,(N-6)*5,(N-7)*6,(N-8)*9,(N-9)*12)