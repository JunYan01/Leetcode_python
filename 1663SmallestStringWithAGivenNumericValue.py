1663. Smallest String With A Given Numeric Value

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        cache = [0]*n
        for i in range(n,0,-1):
            if k - (i - 1) >= 26:
                cache[i-1] = 26
                k -= 26
            else:
                if k == i:
                    cache[0:k] = [1]*k
                    break
                cache[i-1] = k - (i - 1)
                k = i - 1
        # print(cache)
        # print(''.join([chr(x+96) for x in cache]))
        return ''.join([chr(x+96) for x in cache])

                