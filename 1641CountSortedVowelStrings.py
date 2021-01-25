1641  Count Sorted Vowel Strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # v = 5
        # cache = [1]*(v+1) 
        # cache[0] = 0
        # # print(cache)
        # for i in range(n):
        #     for j in range(2,v+1):
        #         cache[j] += cache[j-1]
        #     # print(cache)
        # return cache[v]
        return math.comb(n+4,4)                                                        