895  Maximum Frequency Stack

class FreqStack:

    def __init__(self):
        self.stack = []
        self.vf = {}


    def push(self, x: int) -> None:
        self.vf[x] = self.vf.get(x,0) + 1
        freq = self.vf[x]
        # print(x,self.vf[x])
        if len(self.stack) < freq:
            self.stack.append([])
        self.stack[freq-1].append(x)
        # print(self.stack,self.vf)
        
        

    def pop(self) -> int:
        x = self.stack[-1].pop()
        if len(self.stack[-1]) == 0:
            self.stack.pop()
        self.vf[x] -= 1
        if self.vf[x] == 0:
            del self.vf[x]
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()