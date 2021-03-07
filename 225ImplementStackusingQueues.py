225  Implement Stack using Queues

# class MyStack:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.array = []
        

#     def push(self, x: int) -> None:
#         """
#         Push element x onto stack.
#         """
#         self.array.append(x)
        

#     def pop(self) -> int:
#         """
#         Removes the element on top of the stack and returns that element.
#         """
#         if self.empty():
#             return -1
#         else:
#             return self.array.pop()
        

#     def top(self) -> int:
#         """
#         Get the top element.
#         """
#         if self.empty():
#             return -1
#         else:
#             return self.array[-1]
        

#     def empty(self) -> bool:
#         """
#         Returns whether the stack is empty.
#         """
#         return not self.array

from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = deque([])
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.array.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.empty():
            return -1
        else:
            return self.array.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.empty():
            return -1
        else:
            return self.array[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.array
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()