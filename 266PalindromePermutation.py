# 266. Palindrome Permutation

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        n = len(s)
        cache = {}
        for l in s:
            cache[l] = cache.get(l,0) + 1
        print(cache)
        if n%2==0:
            return all([x%2 == 0 for x in cache.values()])
        else:
            count = 0
            for x in cache.values():
                if x%2 == 1:
                    count += 1
                    if count == 2:
                        return False
            return True
        