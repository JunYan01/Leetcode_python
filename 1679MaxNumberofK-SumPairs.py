1679  Max Number of K-Sum Pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cache = {}
        for n in nums:
            cache[n] = cache.get(n,0) + 1
        count = 0
        # print(cache)
        if k % 2 == 0 and k // 2 in cache:
            t = cache[k // 2]//2
            count += t
            cache[k // 2] = 0
        for key in cache.keys():
            # print(key, k-key)
            if k-key in cache:
                t = min(cache[key],cache[k-key])
                count += t
                cache[key] -= t
                cache[k-key] -= t
        return count