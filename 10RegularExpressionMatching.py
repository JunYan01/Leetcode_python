# 10. Regular Expression Matching


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
#         memo = {}
#         pattern = p
#         text = s
#         def dp(i,j):
#             if (i,j) in memo.keys(): return memo[(i,j)]
#             if j == len(pattern): return i == len(text)
            
#             first = (i<len(text)) and pattern[j] in {text[i],'.'}
            
#             if j <= len(pattern) - 2 and pattern[j + 1] == '*':
#                 ans = dp(i,j+2) or \
#                 first and dp(i+1,j)
#             else:
#                 ans = first and dp(i+1,j+1)
            
#             memo[(i,j)] = ans
#             return ans
        
#         return dp(0,0)
        from functools import lru_cache

        @lru_cache(None)
        def dp(text,pattern):
            if not pattern: return not text

            first = bool(text) and pattern[0] in {text[0], '.'}

            if len(pattern) >= 2 and pattern[1] == '*':
                return dp(text, pattern[2:]) or \
                    first and dp(text[1:], pattern)
            else:
                return first and dp(text[1:], pattern[1:])
            
        return dp(s,p)