856  Score of Parentheses

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
#         https://zxi.mytechroad.com/blog/string/leetcode-856-score-of-parentheses/
#  Case 0: '()' = 1
#  Case 1: '(A)' if A is balanced
#  score =  2* score('A')
#  Case 2: '(A)(B)(C)'
#  score = score('A') + score('BC')
#  Time complexity: Best case: '()()()'
#  Worst case: '((()))'
#  Space complexity: O(n)

#         def score(S, l, r):
#             if r - l == 1: return 1  # Case 0: '()'
#             b = 0
#             for i in range(l,r):
#                 if S[i] == '(': b += 1
#                 elif S[i] == ')': b -= 1
#                 if b == 0:
#                     return score(S, l , i) + score(S, i+1, r) # Case 2
#             return 2*score(S, l + 1, r - 1) # Case 1
#         return score(S, 0, len(S) - 1)
        ans, d = 0, -1
        for i in range(len(S)):
            d += 1 if S[i] == '(' else -1
            if S[i]=='(' and S[i+1] == ')':
                ans += 1 << d
        return ans