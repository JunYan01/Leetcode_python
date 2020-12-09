# 117. Populating Next Right Pointers in Each Node II


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = [root]
        levelnext = []
        while level:
            node = level.pop(0)
            # print(node.val)
            if not node:
                return root
            if level:
                node.next = level[0]
            # else:
            #     node.next = None
            if node.left:
                levelnext.append(node.left)
            if node.right:
                levelnext.append(node.right)
            if not level:
                level = levelnext.copy()
                levelnext = []
                # print(level)
        return root
                