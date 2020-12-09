# 163. Missing Ranges


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        res = []
        
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                res.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        
        return res
    
        result = []
        A.append(upper+1)
        pre = lower - 1
        for i in A:
            if i == pre + 2:
                result.append(str(i-1))
            elif i > pre + 2:
                result.append(str(pre + 1) + "->" + str(i -1))
            pre = i
        return result