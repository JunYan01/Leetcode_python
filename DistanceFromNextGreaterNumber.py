# Distance from next greater number

class Solution:
    def DistanceFromNextGreaterNumber(self, nums) -> int:
    	n = len(nums)
    	ans = [0]*n
    	s = []

    	for i in range(n-1,-1,-1):
    		while len(s) != 0 and nums[s[0]] <= nums[i]:
    			s.pop(0)
    		ans[i] = 0 if len(s) == 0 else s[0]-i
    		s.insert(0,i)
    	print(ans)
    	return ans

a = Solution()
a.DistanceFromNextGreaterNumber([73,74,75,71,69,72,76,73])

