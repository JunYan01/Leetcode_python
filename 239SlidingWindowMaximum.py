# 239. Sliding Window Maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        class MonotonicQueue:
            def __init__(self):
                self.data = []
            
            def pushValue(self,p):
                while self.data and self.data[-1] < p:
                    self.data.pop()
                self.data.append(p)
                
            def maxValue(self):
                return self.data[0] if self.data else float('-inf')
            
            def popValue(self,p):
                if self.data and self.data[0] == p:
                    self.data.pop(0)
        
        n = len(nums)
        window = MonotonicQueue()
        # print(window.data)
        res = []
        for i in range(n):
            if i < k-1:
                window.pushValue(nums[i])
            else:
                window.pushValue(nums[i])
                res.append(window.maxValue())
                window.popValue(nums[i-k+1])
                
        return res
                
                