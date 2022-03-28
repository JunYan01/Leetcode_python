# 3. Longest Substring Without Repeating Characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128
        ans = 0
        start = 0
        for i, ch in enumerate(s):
            if last[ord(ch)] != -1:
                start = max(start, last[ord(ch)]+1)
            ans = max(ans, i - start + 1)
            last[ord(ch)] = i
        return ans
        