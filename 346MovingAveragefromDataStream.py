# 346. Moving Average from Data Stream
class MovingAverage:

#     def __init__(self, size: int):
#         """
#         Initialize your data structure here.
#         """
#         self.size = size
#         self.arr = []
        
        

#     def next(self, val: int) -> float:
#         if len(self.arr) == self.size:
#             self.arr.append(val)
#             self.arr.pop(0)
            
#         else:
#             self.arr.append(val)
            
#         return sum(self.arr)/len(self.arr)

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.arr = []
        self.sum = 0
        
    def next(self, val: int) -> float:
        if len(self.arr) == self.size:
            self.sum -= self.arr[0]
            self.arr.pop(0)
        self.arr.append(val)
        self.sum += val
            
        return self.sum/len(self.arr)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)