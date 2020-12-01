# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cache = defaultdict(int)
        for i in s:
            cache[i] += 1
        for j in t:
            if cache[j] == 0:
                return j
            else:
                cache[j] -= 1
            