# 173. Binary Search Tree Iterator


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.cache = []
        self.index = 0
        self.InOrderTraverse(root)
        # print(self.cache)
        return
        
        

    def next(self) -> int:
        x = self.cache[self.index]
        self.index += 1
        return x
        

    def hasNext(self) -> bool:
        return self.index<len(self.cache)
        
    def InOrderTraverse(self, node):
        if not node:
            return
        
        self.InOrderTraverse(node.left)
        self.cache.append(node.val)
        self.InOrderTraverse(node.right)
        return
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()