# 78. Subsets


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        track = []
        res = [[]]
        def backtrack(nums,start,track,res):
            if track not in res:
                res.insert(0,track[:])
            
            
            # res.append(track)
            # print(res,track)
            for i in range(start,len(nums)):
                track.insert(0,nums[i])
                backtrack(nums,i+1,track,res)
                track.pop(0)
            return 
        
        backtrack(nums,0,track,res)
        return res
    