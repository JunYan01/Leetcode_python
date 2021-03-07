622. Design Circular Queue

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*k
        self.head = -1
        self.tail = -1
        self.size = k
        return
        

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.head = self.tail = 0
            self.queue[self.tail] = value
            return True
        if self.isFull():
            return False
        else:
            self.tail += 1
            self.tail =  self.tail % self.size
            self.queue[self.tail] = value
            return True
        
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = -1
            self.head += 1
            self.head = self.head % self.size
            return True
        

    def Front(self) -> int:
        # if self.isEmpty():
        #     return -1
        return self.queue[self.head]
        

    def Rear(self) -> int:
        # if self.isEmpty():
        #     return -1
        return self.queue[self.tail]
        

    def isEmpty(self) -> bool:
        # if self.head == -1 and self.tail == -1:
        #     return True
        # if self.queue[self.tail] == -1 and (0<=self.tail==self.head-1 or (self.tail==self.size-1 and self.head == 0)):
        if self.queue[self.tail] == -1:
            return True
        return False
        

    def isFull(self) -> bool:
        # return (0 == self.head and self.tail == self.size-1) or (0<= self.tail == self.head-1 <= self.size-2)
        # return (0 == self.head and self.tail == self.size-1) or (self.tail == self.head-1)
        return (self.tail+1) % self.size == self.head and self.queue[self.tail] != -1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()