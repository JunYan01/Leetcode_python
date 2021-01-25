1506. Find Root of N-Ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
#         inDegree = {}
#         for x in tree:
#             print('1',x.val)
#             inDegree[x.val] = inDegree.get(x.val,0)
#             for y in x.children:
#                 inDegree[y.val] = inDegree.get(y.val,0) + 1
#                 print('2',y.val,inDegree[y.val])
            
#         print(inDegree)
        
#         return tree[0]
        inDegree = {}
        for x in tree:
            inDegree[x] = 0
        
        for x in tree:
            for y in x.children:
                inDegree[y] += 1
        
        for x in tree:
            if inDegree[x] == 0:
                return x
            