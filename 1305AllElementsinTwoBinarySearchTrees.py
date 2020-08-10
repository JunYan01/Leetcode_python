# 1305. All Elements in Two Binary Search Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        queue = []
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            queue.append(node.val)
            dfs(node.right)
            
            return None
        
        dfs(root1)
        n1 = len(queue)
        dfs(root2)
        n2 = len(queue) - n1
        q1 = queue[0:n1]
        q2 = queue[n1:]
        # print(n1,q1)
        # print(n2,q2)
        i,j = 0,0
        q3 = []
        while i < n1 and j < n2:
            if q1[i] < q2[j]:
                q3.append(q1[i])
                i += 1
            elif q1[i] > q2[j]:
                q3.append(q2[j])
                j +=1
            else:
                q3.append(q1[i])
                q3.append(q1[i])
                i += 1
                j += 1
                
        if i==n1:
            q3 = q3 + q2[j:]
        else:
            q3 = q3 + q1[i:]
        return q3
        # queue.sort()
        
        # return queue

