# 617. Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def sumTree(node1, node2):
            # if not node1 and not node2: return None
            if not node1: return node2
            if not node2: return node1
#             both node1 and node2 is empty
            node1.val += node2.val
            node1.left = sumTree(node1.left, node2.left)
            node1.right = sumTree(node1.right, node2.right)
            return node1
        return sumTree(t1, t2)