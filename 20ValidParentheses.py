20  Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        # dic = {'[':']','(':')','{':'}'}
        # cache = []
        # for symbol in s:
        #     if symbol in dic:
        #         cache.append(symbol)
        #     else:
        #         try:
        #             if dic[cache.pop()] != symbol:
        #                 return False
        #         except:
        #             return False
        #     # print(cache)
        # return len(cache) == 0
        dic = {'[':']','(':')','{':'}'}
        cache = []
        for symbol in s:
            if symbol in dic:
                cache.append(symbol)
            else:
                if not cache or dic[cache.pop()] != symbol: return False
        return not cache