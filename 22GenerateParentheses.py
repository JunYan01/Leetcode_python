22. Generate Parentheses
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cache = []
        def traverse(left, right,s):
            if left == n and right == n:
                cache.append(s)
                return 
            
            if left < n:
                traverse(left + 1, right, s + '(')
            
            if left > right:
                traverse(left , right + 1, s + ')')
                
            return cache
        return traverse(0,0,'')