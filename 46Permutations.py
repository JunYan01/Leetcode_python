# 46. Permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []
        n = len(nums)
        
        def backtrack(nums,track):
            if len(track) == n:
                res.insert(0,track[:])
                return
            
            for i in range(n):
                if nums[i] in track:
                    continue
                track.insert(0,nums[i])
                backtrack(nums,track)
                track.pop(0)
        
        backtrack(nums,track)
        return res