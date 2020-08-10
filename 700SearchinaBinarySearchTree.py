# 700. Search in a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def BST(node, value):
            if not node:
                return node
            if node.val == value:
                return node
            elif node.val > value:
                return BST(node.left, value)
            else:
                return BST(node.right, value)
            
        return BST(root, val)
            