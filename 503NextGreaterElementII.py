# 503. Next Greater Element II


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        q = []
        for i in range(2*n-1,-1,-1):
            while len(q)!=0 and q[0]<=nums[i%n]:
                q.pop(0)
            ans[i%n] = -1 if not q else q[0]
            q.insert(0,nums[i%n])
        
        return ans