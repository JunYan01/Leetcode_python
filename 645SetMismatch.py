645Set Mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # res = []
        # for n in nums:
        #     if nums[abs(n)-1] < 0:
        #         res.append(abs(n))
        #     nums[abs(n)-1] = - nums[abs(n)-1]
        # for i in range(len(nums)):
        #     if nums[i]>0 and i+1 not in res:
        #         res.append(i+1)
        # print(nums)
        # return res
        x = -1
        count = 0
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                x = n
            count += n
            nums[n-1] = - nums[n-1]
        n = len(nums)
        # res.append(res[0]+n*(n+1)//2-count)
        return [x,x+n*(n+1)//2-count]