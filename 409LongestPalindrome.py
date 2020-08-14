# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        array = {}
        for w in s:
            array[w] = array.get(w,0) +1
        # print(array)
        count = 0
        countOdd = 0
        for w in array:
            if array[w] % 2 == 0:
                count += array[w]
            else:
                count += array[w] - 1
                countOdd = 1
        
        return count + countOdd


        # m = len(s)
        # if m == 0:
        #     return 0
        # dp = [[0]*(m) for _ in range(m)]
        # for i in range(m-1,-1,-1):
        #     dp[i][i] = 1
        #     for j in range(i+1,m):
        #         if s[i] == s[j]:
        #             dp[i][j] = dp[i+1][j-1] + 2
        #         else:
        #             dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        # for i in range(m):
        #     print(dp[i])
        # return dp[0][m-1]
        
#         m = len(s)
#         if m == 0:
#             return 0
#         a = dict()
#         for l in s:
#             print(a.keys())
#             if l in a.keys() :
#                 a[l] += 1
#             else:
#                 a[l] = 1
#         count = 0
#         odd_max = 0
#         for l,c in a:
#             if c %2 ==0:
#                 count += c
#             else
#                 odd_max = max(odd_max,c)
        
#         return count + odd_max
        if not s:
            return 0
        a = dict()
        for l in s:
            # print(a)
            if l in a.keys():
                a[l] += 1
            else:
                a[l] = 1
        # print(a)
        count = 0
        
        # odd = 0 
        # odd_exist = 0
        # for c in a.values():
        #     if c%2 == 0:
        #         count += c
        #     else:
        #         odd += c-1
        #         odd_exist = 1
        
        
#         return odd + count + odd_exist
        odd_count = 0
        for c in a.values():
            count += c
            if c%2 == 1:
                odd_count += 1
        
        return count - odd_count if odd_count == 0 else count - odd_count+1