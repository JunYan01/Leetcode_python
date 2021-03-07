133   Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def cloneGraphHelper(node: 'Node'):
            if not node:
                return node
            if node in visited:
                return visited[node]
            newNode = Node(node.val,[])
            # print(node.val)
            visited[node] = newNode
            if node.neighbors:
                newNode.neighbors = [cloneGraphHelper(n) for n in node.neighbors]
            
            return newNode
        visited = {}
        return cloneGraphHelper(node)
            
            