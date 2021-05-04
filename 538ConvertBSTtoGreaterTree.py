538  Convert BST to Greater Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
#         cache = []
#         def BGT(node: TreeNode):
#             if not node:
#                 return node
#             BGT(node.right)
#             value = node.val
#             node.val += sum(cache)
#             cache.append(value)
#             BGT(node.left)
            
#             return node
        
#         return BGT(root)

#         cache = [0]
#         def BGT(node: TreeNode):
#             if not node:
#                 return node
#             BGT(node.right)
            
#             node.val += cache[-1]
#             cache.append(node.val)
#             BGT(node.left)
            
#             return node
        
#         return BGT(root)
        def BGT(node: TreeNode):
            if not node:
                return node
            BGT(node.right)
            
            node.val += self.ct
            self.ct = node.val
            BGT(node.left)
            
            return node
        self.ct = 0
        return BGT(root)
#         def BGT(node: TreeNode,cache):
#             if not node:
#                 return (node,cache)
#             _,cache = BGT(node.right,cache)
            
#             node.val += cache
#             cache = node.val
#             _,cache = BGT(node.left,cache)
            
#             return (node,cache)
        
#         return BGT(root,0)[0]
        
        

        