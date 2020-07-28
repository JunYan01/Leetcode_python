# 28. Implement strStr()


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
#         m = len(haystack)
#         n = len(needle)

#         if n == 0:
#             return 0
#         dp = [[0]*128 for _ in range(n)]
#         # for l in 'abcdefghijklmnopqrstuvwxyz':
#         #     print(ord(l),str(l))
#         def kmp(pattern):  
#             n = len(pattern)
#             if n == 0:
#                 return
            
#             dp[0][ord(pattern[0])] = 1
#             X = 0
#             for i in range(1,n):
#                 for j in range(128):
#                     dp[i][j] = dp[X][j]
#                 dp[i][ord(pattern[i])] = i + 1
#                 X = dp[X][ord(pattern[i])]
#             return
        
#         kmp(needle)
        
#         j = 0
#         for i in range(m):
#             # print(j,needle[i],ord(needle[i])-97)
#             j = dp[j][ord(haystack[i])]
#             print(j,haystack[i])
#             if j == n:
#                 return i-n+1
#         return -1



    #     if haystack == None or needle == None:
    #         return -1
    # #generate next array, need O(n) time
    #     i, j, m, n = -1, 0, len(haystack), len(needle)
    #     next = [-1] * n
    #     while j < n - 1:  
    #     #needle[k] stands for prefix, neelde[j] stands for postfix
    #         if i == -1 or needle[i] == needle[j]:   
    #             i, j = i + 1, j + 1
    #             next[j] = i
    #         else:
    #             i = next[i]
    #         print (i,j,next[i],next[j])
    #     print(next)
    # #check through the haystack using next, need O(m) time
    #     i = j = 0
    #     while i < m and j < n:
    #         if j == -1 or haystack[i] == needle[j]:
    #             i, j = i + 1, j + 1
    #         else:
    #             j = next[j]
    #     if j == n:
    #         return i - j
    #     return -1