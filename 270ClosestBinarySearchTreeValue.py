# 270. Closest Binary Search Tree Value


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
#         def closestValueHelper(node,target) -> int:
#             if not node:
#                 return float('inf')
#             minValue = node.val
#             mindis = abs(minValue - target)

#             a = closestValueHelper(node.left,target) 
#             disa = abs(a - target)
            
#             if disa < mindis:
#                 minValue, mindis = a, mindis
                
#             a = closestValueHelper(node.right,target) 
#             disa = abs(a - target)
            
#             if disa < mindis:
#                 minValue, mindis = a, mindis
            
#             return minValue
        
#         return closestValueHelper(root,target)
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest

            
                