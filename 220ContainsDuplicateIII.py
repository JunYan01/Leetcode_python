# 220. Contains Duplicate III

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # if t == 0 and len(nums) == len(set(nums)):
        #     return False
        # if k == 0 or t < 0:
        #     return False
        # for i, num in enumerate(nums):
        #     for j in range(i+1,min(len(nums),i+k+1)):
        #         if abs(num - nums[j]) <= t:
        #             return True
        # return False
        if t == 0 and len(nums) == len(set(nums)) or k == 0 or t < 0:
            return False
        bucket = {}
        n = len(nums)
        for i in range(n):
            m = nums[i] // (t + 1)
            if m in bucket:
                return True
            if m - 1 in bucket and abs(nums[i] - bucket[m-1]) <= t:
                return True
            if m + 1 in bucket and abs(nums[i] - bucket[m+1]) <= t:
                return True
            if i >= k:
                del bucket[nums[i-k] // (t+1)]
            bucket[m] = nums[i]
        
        return False
                