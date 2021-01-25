215 Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
#         def quickSortOnce(nums, start, end):
#             if start >= end:
#                 return start
#             pivot = nums[start]
#             left = start + 1
#             right = end
#             while left <= right:
#                 while left <= right and nums[left] > pivot:
#                     left += 1
#                 while left <= right and nums[right] < pivot:
#                     right -= 1
#                 if left <= right:
#                     nums[left], nums[right] = nums[right], nums[left]
#                     left += 1
#                     right -= 1
#             nums[start], nums[right] = nums[right], nums[start]
            
#             return right
        def quickSortOnce(nums, start, end):
            if start >= end:
                return start
            pivot = nums[start]
            right = start 
            for i in range(start+1 ,end+1):
                if nums[i] >= pivot:
                    right += 1
                    nums[i], nums[right] = nums[right], nums[i]
            nums[right], nums[start] = nums[start], nums[right]
            # print(nums[start:end+1], right)
            return right
        
        left, right = 0, len(nums) - 1
        
        while True:
            index = quickSortOnce(nums, left, right)
            if index == k - 1:
                return nums[index]
            elif index < k - 1:
                left = index + 1
            else:
                right = index - 1