647  Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        def count(s, i, j):
            ans = 0
            while i>=0 and j<len(s) and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1
            return ans
        ans = 0
        for i in range(len(s)):
            ans += count(s, i, i)
            ans += count(s, i, i + 1)
        return ans