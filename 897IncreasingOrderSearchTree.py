# 897. Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def increasingBSTHelper(node):
            if not node.left:
                a = node
            else:
                a, b = increasingBSTHelper(node.left)
                b.right = node
                node.left = None
            
            if not node.right:
                d = node
            else:
                c, d = increasingBSTHelper(node.right)
                node.right = c
            
            return a, d
        minNode, maxNode = increasingBSTHelper(root)
        return minNode
            
            