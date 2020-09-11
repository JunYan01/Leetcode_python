# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            if nums[abs(i)-1]>0:
                nums[abs(i)-1] *= - 1
        return [i+1 for i,x in enumerate(nums) if x>=0]