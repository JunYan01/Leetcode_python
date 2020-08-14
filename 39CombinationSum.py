# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res
    
    # def dfs(self, nums, target, index, path, res):
    #     if target < 0:
    #         return  # backtracking
    #     if target == 0:
    #         res.append(path)
    #         return 
    #     for i in range(index, len(nums)):
    #         self.dfs(nums, target-nums[i], i, path+[nums[i]], res)
    
#     Better organised        
    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            if nums[i] > target:  #here  
                break
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res) 


            