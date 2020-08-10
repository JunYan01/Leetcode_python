# 98. Validate Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def BST(node, minnode, maxnode):
            if not node:
                return True
            # if minnode and maxnode and node:
            #     print(minnode.val,maxnode.val,node.val)
            if minnode and node.val <= minnode.val:
                return False
            if maxnode and node.val >= maxnode.val:
                return False
            return BST(node.left,minnode,node) and BST(node.right,node,maxnode)
        return BST(root,None,None)