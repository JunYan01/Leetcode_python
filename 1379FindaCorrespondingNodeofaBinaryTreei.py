# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue1 = [original]
        queue2 = [cloned]
        
        while queue1:
            node1 = queue1.pop(0)
            node2 = queue2.pop(0)
            if node1 is target:
                return node2
            if node1.left:
                queue1.append(node1.left)
                queue2.append(node2.left)
            if node1.right:
                queue1.append(node1.right)
                queue2.append(node2.right)
        return None