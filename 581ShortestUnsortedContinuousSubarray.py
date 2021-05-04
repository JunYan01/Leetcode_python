581  Shortest Unsorted Continuous Subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        
        l, r = 0, n - 1
        
        while l < n - 1 and nums[l] <= nums[l+1]:
            l += 1
        
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
        
        if l > r: return 0
        
        def findLocalMinMax(l, r):
            local_min = float('inf')
            local_max = float('-inf')
            for i in range(l,r+1):
                if i == n:
                    break
                local_min = min(local_min, nums[i])
                local_max = max(local_max, nums[i])
            return local_min, local_max
        tempMin, tempMax = findLocalMinMax(l,r+1)
        
        while l > 0 and tempMin < nums[l-1]:
            l -= 1
        
        while r < n - 1 and nums[r+1] < tempMax:
            r += 1
        
        return r + 1 - l


        
        