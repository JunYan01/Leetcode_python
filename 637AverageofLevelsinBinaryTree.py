637  Average of Levels in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
#         BFS
        level = [root]
        res = []
        levelNext = []
        while level:
            res.append(sum([x.val for x in level])/len(level))
            while level:
                node = level.pop()
                if node.left:
                    levelNext.append(node.left)
                if node.right:
                    levelNext.append(node.right)
            
            level = levelNext
            levelNext = []
        return res