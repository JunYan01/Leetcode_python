394  Decode String

class Solution:
    def decodeString(self, s: str) -> str:
#         stack = []
#         n = len(s)
#         for i in range(n):
#             if s[i] == ']':
#                 decodedString = ""
#                 while stack[-1] != '[':
#                     decodedString += stack.pop()
#                 stack.pop()
#                 base, k = 1, 0
#                 while stack and stack[-1].isdigit():
#                     k = k + (int(stack.pop()) - 0) * base
#                     base *= 10
#                 currentLen = len(decodedString)
#                 for _ in range(k):
#                     for j in range(currentLen-1,-1,-1):
#                         stack.append(decodedString[j])
#             else:
#                 stack.append(s[i])
#         return ''.join(stack)

        countStack = []
        stringStack = []
        currentString = ''
        k = 0
        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == '[':
                countStack.append(k)
                stringStack.append(currentString)
                currentString = ''
                k = 0
            elif ch == ']':
                decodedString = stringStack.pop()
                currentK = countStack.pop()
                for _ in range(currentK):
                    decodedString += currentString
                currentString = decodedString
            else:
                currentString += ch
        
        return currentString
    
    