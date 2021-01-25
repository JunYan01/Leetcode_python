161  One Edit Distance

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        if len(s) == len(t):
            count = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count += 1
                    if count == 2:
                        return False
            return count == 1
        if len(s) > len(t):
            s, t = t, s
        if len(s) != len(t) - 1:
            return False
        # if len(s) == 0:
        #     return True
        i, j, count = 0, 0, 0
        print(s,t)
        while i < len(s):
            if s[i] != t[j]:
                count += 1
                print(s[i], t[j])
                if count == 2:
                    return False
                i -= 1
            i += 1
            j += 1
        return count == 1 or j == len(t) - 1