# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # # if max(nums) <= 0:
        # if nums[-1] <= 0:
        #     return [x*x for x in nums[::-1]]
        # elif nums[0] >= 0:
        #     return [x*x for x in nums]
        # i = 0
        # n = len(nums)
        # while i < n-1:
        #     if abs(nums[i]) < abs(nums[i+1]):
        #         break
        #     i += 1
        # # print(nums[:i+1])
        # # print(nums[i+1:])
        # # x = nums[:i+1]
        # # y = nums[i+1:]
        # # m = i+1
        # # n = n - m
        # arr = []
        # j = i + 1
        # while i >= 0 and j < n:
        #     if abs(nums[i]) <= abs(nums[j]): 
        #         arr.append(nums[i]*nums[i])
        #         i -= 1
        #     elif abs(nums[i]) > abs(nums[j]):
        #         arr.append(nums[j]*nums[j])
        #         j += 1
        # # print(i,j)
        # # print(arr)
        # if i == -1:
        #     while j < n:
        #         arr.append(nums[j]*nums[j])
        #         j += 1
        # if j == n:
        #     while i >= 0:
        #         arr.append(nums[i]*nums[i])
        #         i -= 1
        # return arr
        
        
        # return sorted([x**2 for x in nums])
        
        if nums[0] >= 0:
            return [x*x for x in nums]
        elif nums[-1] <= 0:
            return [x*x for x in nums[::-1]]
        l = len(nums)
        left, right = 0, l - 1
        res = [0]*l
        cur = l - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[cur] = nums[left] **2
                left += 1
            else:
                res[cur] = nums[right] ** 2
                right -= 1
            cur -= 1
        return res