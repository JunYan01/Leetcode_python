# 152. Maximum Product Subarray


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            B[i] *= B[i - 1] or 1
        # print(nums)
        # print(B)
        # print(nums+B)
        return max(nums + B)
        
#         if len(nums) == 0:
#             return 0

#         max_so_far = min_so_far = result = nums[0]


#         for i in range(1, len(nums)):
#             curr = nums[i]
# #             temp_max = max(curr, max_so_far * curr, min_so_far * curr)
# #             min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
# #             max_so_far = temp_max
#             max_so_far, min_so_far = max(curr, max_so_far * curr, min_so_far * curr), min(curr, max_so_far * curr, min_so_far * curr)
            
#             result = max(max_so_far, result)

#         return result