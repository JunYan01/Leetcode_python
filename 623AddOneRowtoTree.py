623Add One Row to Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        AllRoot = TreeNode(-1)
        AllRoot.left = root
        level1 = [AllRoot]
        level2 = []
        d -= 1
        while d>0 and level1:
            while level1:
                node = level1.pop()
                if node.left:
                    level2.append(node.left)
                if node.right:
                    level2.append(node.right)
            level1 = level2
            level2 = []
            d -= 1
        
        # print([x.val for x in level1])
        
        while level1:
            node = level1.pop()
            # if node.left:
            #     curr = TreeNode(v)
            #     curr.left = node.left
            #     node.left = curr
            # if node.right:
            #     curr = TreeNode(v)
            #     curr.right = node.right
            #     node.right = curr
            curr = TreeNode(v)
            curr.left = node.left
            node.left = curr
            curr = TreeNode(v)
            curr.right = node.right
            node.right = curr
            
        
        return AllRoot.left