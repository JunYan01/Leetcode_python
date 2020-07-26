# 213. House Robber II


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <=3:
            return max(nums)
        n = len(nums)
        def robRange(i,j):
            dp1 = 0
            dp2 = 0
            for k in range(j,i-1,-1):
                dp = max(dp1,nums[k]+dp2)
                dp2 = dp1
                dp1 = dp
            return dp
        return max(robRange(0,n-2),robRange(1,n-1))