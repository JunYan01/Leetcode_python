971Flip Binary Tree To Match Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.pos = 0
        self.flips = []
        def solve(root):
            if self.flips == [-1]: return
            if not root: return
            if self.pos >= len(voyage): return
            if root.val != voyage[self.pos]:
                self.flips = [-1]
                return 

            if root.left and root.left.val != voyage[self.pos + 1]:
                root.left, root.right = root.right, root.left
                self.flips.append(root.val)
            self.pos += 1
            solve(root.left)
            solve(root.right)
        
        solve(root)
        return self.flips
                    
        
#         rootQueue1 = TreeNode(0)
#         rootQueue1.left = root
#         rootQueue2 = TreeNode(0)
#         rootQueue2.left = voyage
#         queue1 = [rootQueue1]
#         queue2 = [rootQueue2]
#         none = -1
#         res = []
        
#         while queue1 and queue2:
#             x = queue1.pop()
#             y = queue2.pop()
#             xl = x.left.val if x.left else none
#             xr = x.right.val if x.right else none
#             yl = y.left.val if y.left else none
#             yr = y.right.val if y.right else none
#             if xl == yr and xr == yl:
#                 res.append(x.val)
#                 x.left, x.right = x.right, x.left
#             elif xl != xr or yl != yr:
#                 return [-1]
#             if x.left:
#                 queue1.append(x.left)
#                 queue2.append(y.left)
#             if x.right:
#                 queue1.append(x.right)
#                 queue2.append(y.right)
        
#         print(res)
#         return res
                    
            
            # y.left, x.right, y.right