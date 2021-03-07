20  Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        Par = {'(':')','[':']','{':'}'}
        stack = []
        for p in s:
            if p in Par.keys():
                stack.append(p)
            else:
                if stack and Par[stack.pop()] == p:
                    continue
                else:
                    return False
        return not stack