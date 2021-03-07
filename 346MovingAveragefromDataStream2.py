346. Moving Average from Data Stream
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size
        self.sum = 0
        self.len = 0

    def next(self, val: int) -> float:
        # if len(self.queue)==self.size:
        if self.len==self.size:
            self.sum -= self.queue.pop(0)
            self.len -= 1
            
        self.queue.append(val)
        self.sum += val
        self.len += 1
        return self.sum/self.len

        # return self.sum/len(self.queue)
        # return sum(self.queue)/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)