# 337. House Robber III



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
#         memo = {}

#         def robHelper(node) -> int:
#             if not node: return 0
#             if node in memo.keys():
#                 return memo[node]
#             rob_it = node.val
#             if node.left:
#                 rob_it += robHelper(node.left.left) + robHelper(node.left.right)
#             if node.right:
#                 rob_it += robHelper(node.right.left) + robHelper(node.right.right)
            
#             skip_it = robHelper(node.left) + robHelper(node.right) 
#             memo[node] = max(rob_it,skip_it)
            
#             return memo[node]
        
#         return robHelper(root)

################################ This method takes more memory, but less time in pracise when I run it in leetcode
################################

#         from functools import lru_cache
#         @lru_cache(None)
#         def robHelper(node) -> int:
#             if not node: return 0

#             rob_it = node.val
#             if node.left:
#                 rob_it += robHelper(node.left.left) + robHelper(node.left.right)
#             if node.right:
#                 rob_it += robHelper(node.right.left) + robHelper(node.right.right)
            
#             skip_it = robHelper(node.left) + robHelper(node.right) 
            
#             return max(rob_it,skip_it)
        
#         return robHelper(root)



################################ Put more information on the return of recurssive function
################################
        def dp(node):
            if not node:
                return [0,0]
            left = dp(node.left)
            right = dp(node.right)
            rob_it = node.val + left[1] + right[1]
            # skip_it = left[0] + right[0]
            skip_it = max(left)+max(right)
            print(node.val,left,right ,[rob_it,skip_it])
            return [rob_it,skip_it]
        return max(dp(root))
                
        