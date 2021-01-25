5 Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(s, left , right):
            while left>=0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return right - left - 1
        
        # if len(s) == 1:
        #     return s
        # begin, end = 0, 0
        # for i in range(len(s)):
        #     singleCenter = expandAroundCenter(s, i, i)
        #     doubleCenter = expandAroundCenter(s, i, i+1)
        #     l = max(singleCenter, doubleCenter)
        #     if l > end - begin:
        #         begin = i - (l -1)//2
        #         end = i + l//2
        # return s[begin:end+1]
        if len(s) == 1:
            return s
        begin, length = 0, 0
        for i in range(len(s)):
            l = max(expandAroundCenter(s, i, i), expandAroundCenter(s, i, i+1))
            if l > length:
                begin = i - (l -1)//2
                length = l
        return s[begin:begin+length]