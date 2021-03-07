94  Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
#         def traverse(node) :
#             if not node:
#                 return 
#             traverse(node.left)
#             stack.append(node.val)
#             traverse(node.right)
            
#             return 
#         stack = []
#         traverse(root)
#         return stack
        
        stack = []
        res = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res
            
            
            
            