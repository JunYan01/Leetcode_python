# 701. Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def BST(node, value):
            if not node:
                return TreeNode(value)
#             if node.val = value
#             not the same

            if node.val < value:
                node.right = BST(node.right, value)
            elif node.val > value:
                node.left = BST(node.left, value)
            return node
        return BST(root, val)