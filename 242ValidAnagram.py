242Valid Anagram   
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = defaultdict(int)
        for l in s:
            cache[l] += 1
        for l in t:
            cache[l] -= 1
            if cache[l]<0:
                return False
        # for l in cache:
        #     if cache[l] != 0:
        #         return False
        # return True
        return all(not cache[l] for l in cache)