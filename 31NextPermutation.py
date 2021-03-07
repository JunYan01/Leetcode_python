31  Next Permutation


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         n = len(nums)
#         if n <= 1:
#             return None
        
#         for i in range(n-1,-1,-1):
#             if nums[i] > nums[i-1]:
#                 # nums[i] , nums[i-1] = nums[i-1] , nums[i]
#                 break
#         if i == 0:
#             nums.sort()
#             return None
#         # print(i)
#         for j in range(n-1,i-1,-1):
#             if nums[j] > nums[i-1]:
#                 nums[i-1] , nums[j] = nums[j] , nums[i-1]
#                 break
#         nums[i:n] = sorted([x for x in nums[i:n]])
#         return None
        n = len(nums)
        if n <= 1:
            return None
        
        i = n - 2
        while i >= 0 and nums[i]>=nums[i+1]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
                
            nums[i] , nums[j] = nums[j] , nums[i]
        nums[i+1:n] = sorted([x for x in nums[i+1:n]])
        # j, k = i + 1, n - 1
        # while j < k:
        #     nums[j] , nums[k] = nums[k] , nums[j]
        #     j += 1
        #     k -= 1
        return None
        