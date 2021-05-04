946  Validate Stack Sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         i = j = 0
#         n = len(pushed)
#         stack = []
#         while i < n or j < n:
#             if not stack:
#                 stack.append(pushed[i])
#                 i += 1
#                 continue
#             if stack[-1] == popped[j]:
#                 stack.pop()
#                 j += 1
#                 continue
#             else:
#                 if i>=n:
#                     return False
#                 stack.append(pushed[i])
#                 i += 1
        
#         # print(stack)
#         return True
        i = j = 0
        n = len(pushed)
        stack = []
        while i < n:
            if not stack:
                stack.append(pushed[i])
                i += 1
                continue
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
                continue
            else:
                stack.append(pushed[i])
                i += 1
        
        while j < n:
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False
        
        
        return True