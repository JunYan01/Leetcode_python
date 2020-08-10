# 171. Excel Sheet Column Number


class Solution:
    def titleToNumber(self, s: str) -> int:
        count = 0
        for i in s:
            # print(i,ord(i)-64)
            count *=26
            count += ord(i)-64
        
        return count