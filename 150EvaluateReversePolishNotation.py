150  Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # print(int(6/(-132)))
        # res = 0
        n = len(tokens)
        ops = set(["+","-","*","/"])
        def op(op,x,y):
            if op == "+":
                return x + y
            elif op == "-":
                return  y - x
            elif op == "*":
                return x * y
            elif op == "/":
                return int(y / x)
            
        stack = []
        for t in tokens:
            if t in ops:
                res = op(t,stack.pop(),stack.pop())
                stack.append(res)
            else:
                stack.append(int(t))
            # print(stack,res)
        return stack.pop()