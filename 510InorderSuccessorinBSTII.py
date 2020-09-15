# 510. Inorder Successor in BST II

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
#         val = node.val
#         if node.right:
#             node = node.right
#             while node.left:
#                 node = node.left
#             return node
        
#         while node.parent:
#             if node.parent.val <= val:
#                 node = node.parent
#             else:
#                 return node.parent
#         return node.parent

        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent:
            if node.parent.right == node:
                node = node.parent
            else:
                return node.parent
        return node.parent
            
        
        