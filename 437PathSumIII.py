# 437. Path Sum III



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
#         if root == None:
#             return 0
        
#         def pathTopCount(root, target):
#             if root == None:
#                 return 0
            
#             return (root.val == target) \
#                 + pathTopCount(root.left, target-root.val) \
#                 + pathTopCount(root.right, target-root.val)
        
#         return pathTopCount(root,sum) \
#             + self.pathSum(root.left,sum) \
#             + self.pathSum(root.right,sum)

# Worst Time O(n^2)    
# Worst Space O(n^2)
        
        result = 0
        cache = defaultdict()
        cache[0] = 1
        def helper(root, target, so_far):
            nonlocal result
            if not root:
                return 
            complement = so_far + root.val - target
            result+= cache.get(complement,0)
            cache[so_far+root.val] = cache.get(so_far+root.val,0) + 1
            helper(root.left, target, so_far+root.val)
            helper(root.right, target, so_far+root.val)
            cache[so_far+root.val] -= 1
            return
        
        helper(root, sum, 0)
        return result

