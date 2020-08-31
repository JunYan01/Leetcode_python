# 450. Delete Node in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # def getMinNode(node):
        #     while node.left: node = node.left
        #     return node
        
        # def deleteNodeHelper(node, value)-> TreeNode:
        #     if not node: return None
        #     if node.val == value:
        #         if not node.left: return node.right
        #         if not node.right: return node.left
        #         minNode = getMinNode(node.right)
        #         node.val = minNode.val
        #         node.right = deleteNodeHelper(node.right, minNode.val)
        #     elif node.val > value:
        #         node.left = deleteNodeHelper(node.left, value)
        #     elif node.val < value:
        #         node.right = deleteNodeHelper(node.right, value)  
        #     return node
        # return deleteNodeHelper(root,key)
#         def getMinNode(node):
#             while node.left: node = node.left
#             return node
        
#         def deleteNodeHelper(node, value)-> TreeNode:
#             if not node: return None
#             prec = TreeNode(-1,node,None)
#             if node.val == value:
#                 if not node.left: return node.right
#                 if not node.right: return node.left
#                 minNode = getMinNode(node.right)
#                 prec.left = node.right
#                 minNode.left = node.left
#             elif node.val > value:
#                 node.left = deleteNodeHelper(node.left, value)
#             elif node.val < value:
#                 node.right = deleteNodeHelper(node.right, value)  
#             return prec.left
#         return deleteNodeHelper(root,key)

        # def getMaxNode(node):
        #     while node.right: node = node.right
        #     return node
        
        # def deleteNodeHelper(node, value)-> TreeNode:
        #     if not node: return None
        #     prec = TreeNode(-1,node,None)
        #     if node.val == value:
        #         if not node.left: return node.right
        #         if not node.right: return node.left
        #         maxNode = getMaxNode(node.left)
        #         prec.left = node.left
        #         maxNode.right = node.right
        #     elif node.val > value:
        #         node.left = deleteNodeHelper(node.left, value)
        #     elif node.val < value:
        #         node.right = deleteNodeHelper(node.right, value)  
        #     return prec.left
        # return deleteNodeHelper(root,key)

        def getMinNode(node):
            while node.left: node = node.left
            return node
        
        def deleteNodeHelper(node, value)-> TreeNode:
            if not node: return None
            if node.val == value:
                if not node.left: return node.right
                if not node.right: return node.left
                minNode = getMinNode(node.right)
                minNode.left = node.left
                node = node.right
            elif node.val > value:
                node.left = deleteNodeHelper(node.left, value)
            elif node.val < value:
                node.right = deleteNodeHelper(node.right, value)  
            return node
        return deleteNodeHelper(root,key)

#         def getMaxNode(node):
#             while node.right: node = node.right
#             return node
        
#         def deleteNodeHelper(node, value)-> TreeNode:
#             if not node: return None
#             if node.val == value:
#                 if not node.left: return node.right
#                 if not node.right: return node.left
#                 maxNode = getMaxNode(node.left)
#                 maxNode.right = node.right
#                 node = node.left
#             elif node.val > value:
#                 node.left = deleteNodeHelper(node.left, value)
#             elif node.val < value:
#                 node.right = deleteNodeHelper(node.right, value)  
#             return node
#         return deleteNodeHelper(root,key)