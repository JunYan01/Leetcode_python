232  Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.array.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return -1
        else:            
            return self.array.pop(0)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return -1
        else:
            return self.array[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.array

# from collections import deque
# class MyQueue:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.array = deque([])

#     def push(self, x: int) -> None:
#         """
#         Push element x to the back of queue.
#         """
#         self.array.append(x)
        

#     def pop(self) -> int:
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         if self.empty():
#             return -1
#         else:            
#             return self.array.popleft()
        

#     def peek(self) -> int:
#         """
#         Get the front element.
#         """
#         if self.empty():
#             return -1
#         else:
#             return self.array[0]
        

#     def empty(self) -> bool:
#         """
#         Returns whether the queue is empty.
#         """
#         return not self.array
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()