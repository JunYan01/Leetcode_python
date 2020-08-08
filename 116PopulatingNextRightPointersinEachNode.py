# 116. Populating Next Right Pointers in Each Node


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
        def bfs(node):
            if not node:
                return
            level1 = [node]
            level2 = []
            while len(level1) >0:
                curr = level1.pop(0)
                if curr.left:
                    level2.append(curr.left)
                    level2.append(curr.right)
                # print([x.val for x in level1])
                # print([x.val for x in level2])
                if len(level1) == 0:
                    # print(curr.val)
                    curr.next = None
                    level1 = level2
                    level2 = []
                    # print([x.val for x in level1])
                else:
                    # print([x.val for x in level1])
                    curr.next = level1[0]
                    # print(curr.val,level1[0].val)
                
            return node
                
        return bfs(root)