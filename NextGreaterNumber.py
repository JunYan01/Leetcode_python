# next greater number

class Solution:
    def NextGreaterNumber(self, nums) -> int:
    	n = len(nums)
    	ans = [-1]*n
    	s = []

    	for i in range(n-1,-1,-1):
    		while len(s) != 0 and s[0] <= nums[i]:
    			s.pop(0)
    		ans[i] = -1 if len(s) == 0 else s[0]
    		s.insert(0,nums[i])
    	print(ans)
    	return ans

a = Solution()
a.NextGreaterNumber([2,1,2,4,3])

