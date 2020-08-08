# 100. Same Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def SameSubTree(Node1,Node2):
            if Node1 == None and Node2 == None:
                return True
            if Node1 == None or Node2 == None:
                return False
            if Node1.val != Node2.val:
                return False
            
            return SameSubTree(Node1.left,Node2.left) and SameSubTree(Node1.right,Node2.right)
        
        return SameSubTree(p,q)