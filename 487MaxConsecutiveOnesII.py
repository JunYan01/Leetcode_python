# 487. Max Consecutive Ones II


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         left = right = maxL = 0
#         pos = -1
#         while right < len(nums):
#             if nums[right] == 0 and pos != -1:
#                 left = pos+1
#                 pos = right
#             elif nums[right] == 0 and pos == -1:
#                 pos = right
            
#             maxL = max(maxL,right - left+1)
#             # print(left,right,pos,maxL)
#             right += 1
#         return maxL

        left = right = maxL = 0
        pos = -1
        for right in range(len(nums)):
            if nums[right] == 0:
                if pos != -1:
                    left = pos + 1
                pos = right
            maxL = max(maxL,right - left+1)
        return maxL