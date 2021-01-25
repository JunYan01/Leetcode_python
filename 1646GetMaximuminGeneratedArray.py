1646  Get Maximum in Generated Array

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        cache = [0] * (n+1)
        cache[1] = 1
        for i in range(2,n+1):
            if i % 2 == 0:
                cache[i] = cache[i//2]
            else:
                cache[i] = cache[i//2] + cache[i//2 + 1]
        return max(cache)