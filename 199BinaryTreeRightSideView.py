199  Binary Tree Right Side View

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return
        level1 = [root]
        level2 = []
        cache = []
        while level1:
            level2 = []
            cache.append(level1[0].val)
            # print([x.val for x in level1])
            while level1:
                node = level1.pop(0)
                if node.right:
                    level2.append(node.right)
                if node.left:
                    level2.append(node.left)
            level1 = level2
            
        
        return cache
            
                