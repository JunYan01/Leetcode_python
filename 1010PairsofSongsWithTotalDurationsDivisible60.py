# 1010. Pairs of Songs With Total Durations Divisible by 60


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cache = {}
        for t in time:
            x = t % 60
            if x in cache:
                cache[x] += 1
            else:
                cache[x] = 1
        # print(cache)
        count = 0
        for x in cache.keys():
            print(cache[x])
            if x == 0 or x == 30:
                if cache[x] >= 2:
                    count += cache[x]*(cache[x]-1)//2
            else:
                if 60-x in cache:
                    count += cache[60-x]*cache[x]
                    cache[60 - x] = 0
            cache[x] = 0
        return count