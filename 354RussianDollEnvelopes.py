354Russian Doll Envelopes

from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         res, n = 0, len(envelopes)
#         dp = [1]*n
#         sorted(envelopes)
#         print(envelopes)
#         for i in range(n):
#             for j in range(i):
#                 if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
#                     dp[i] = max(dp[i],dp[j]+1)
            
#             res = max(res,dp[i])
            
#         return res

        tails = []
        for _, h in sorted(envelopes, key = lambda env : (env[0], -env[1])):
            pos = bisect_left(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
        return len(tails)     