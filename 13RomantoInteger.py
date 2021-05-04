13  Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        keys = ['I','V','X','L','C','D','M']
        dic = dict(zip(keys,list(range(len(keys)))))
        values = [1,5,10,50,100,500,1000]
        # print(dicKey)
        i = len(s)-1
        count = values[dic[s[i]]]
        i -= 1
        while i>=0:
            a, b = dic[s[i]], dic[s[i+1]]
            if a%2 == 0 and 1 <= b - a <= 2:
                count -= values[a]
            else:
                count += values[a]
            i -= 1
            # print(l, dic[l], values[dic[l]])
        return count