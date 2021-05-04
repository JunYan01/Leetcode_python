376  Wiggle Subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def calflag(x, y):
            return 1 if x > y else -1 if x < y else 0
        n = len(nums)
        if n <= 1:
            return n
        flag = calflag(nums[0], nums[1])
        count = 1 + 1*abs(flag)
        for i in range(2,n):
            flag1 = calflag(nums[i-1], nums[i]) 
            # if (flag1 and flag1*flag == -1) or (not flag and flag1):
#             Above are two cases: switching sign flag and starting assigning flag
            if flag1 and flag1*flag <=0:
                count +=1
                flag = flag1
                
        return count