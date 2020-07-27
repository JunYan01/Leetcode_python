# 496. Next Greater Element I


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        ans = {}
        m = len(nums1)
        queue = []
        for i in range(n-1,-1,-1):
            while len(queue) != 0 and queue[0]<=nums2[i]:
                queue.pop(0)
            ans[nums2[i]] = -1 if len(queue) == 0 else queue[0]
            queue.insert(0,nums2[i])
        
        res = [-1]*m
        for i in range(m):
            res[i] = ans[nums1[i]]
        return res