1133  Largest Unique Number

import heapq

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        dic = {}
        for i in A:
            dic[i] = dic.get(i,0) + 1
        # for i in sorted(list(dic.keys()),reverse = True):
        for i in sorted(dic.keys(),reverse = True):
            if dic[i] == 1:
                return i
        
        return -1