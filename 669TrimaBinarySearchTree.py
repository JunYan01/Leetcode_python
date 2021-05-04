669Trim a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def trimBSTHelper(node, low, high):
            if not node:
                return node
            # print(node.val)
            if low <= node.val <= high:
                node.left = trimBSTHelper(node.left, low, high)
                node.right= trimBSTHelper(node.right,low, high)
                return node
            elif node.val < low:
                return trimBSTHelper(node.right, low, high)
            elif node.val > high:
                return trimBSTHelper(node.left , low, high)
            
        return trimBSTHelper(root, low, high)
            
            