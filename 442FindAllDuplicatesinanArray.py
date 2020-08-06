# 442. Find All Duplicates in an Array 


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # a = [0]*n
        # for i in range(n):
        #     a[nums[i]-1] += 1
        # return [x+1 for x in range(n) if a[x]>=2]
        
        ans = []
        
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            nums[abs(num)-1] *= -1

        return ans

        