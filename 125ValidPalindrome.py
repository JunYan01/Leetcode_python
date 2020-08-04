# 125. Valid Palindrome 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n-1
        while i<=j:
            while not s[i].isalnum() and i<n-1:
                i+=1
            while not s[j].isalnum() and j>0:
                j-=1
            if s[i].lower() != s[j].lower() and i<=j:
                print(i,j,s[i].lower(),s[j].lower())
                return False
            i += 1
            j -= 1
        return True