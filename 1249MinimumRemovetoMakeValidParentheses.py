1249Minimum Remove to Make Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # ans = ''
        # stack = []
        # dic = {'(':')'}
        # pos = 0
        # for l in s:
        #     if l.isalpha():
        #         ans += l
        #         pos += 1
        #     elif l in dic:
        #         ans += l
        #         stack.append((l,pos))
        #         pos += 1
        #     else:
        #         if stack and stack[-1][0] in dic and l == dic[stack[-1][0]]:
        #             ans += l
        #             stack.pop()
        #             pos += 1
        #         else:
        #             continue
        # while stack:
        #     _, pos = stack.pop()
        #     ans = ans[0:pos] +ans[pos+1:] 
        #     # ans.pop(pos)
        # # print(ans)
        # # print(stack)
        # return ans
        ans = []
        stack = []
        dic = {'(':')'}
        pos = 0
        for l in s:
            if l.isalpha():
                ans.append(l)
                pos += 1
            elif l in dic:
                ans.append(l)
                stack.append((l,pos))
                pos += 1
            else:
                if stack and stack[-1][0] in dic and l == dic[stack[-1][0]]:
                    ans.append(l)
                    stack.pop()
                    pos += 1
                else:
                    continue
        while stack:
            _, pos = stack.pop()
            ans.pop(pos)
        # print(ans)
        # print(stack)
        return ''.join(ans)