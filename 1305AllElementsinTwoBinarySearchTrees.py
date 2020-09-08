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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
#         def getAllElements(node,cache):
#             if not node:
#                 return
#             getAllElements(node.left,cache)
#             cache.append(node.val)
#             getAllElements(node.right,cache)
#             return
#         cache1 = []
#         getAllElements(root1,cache1)
#         cache2 = []
#         getAllElements(root2,cache2)
#         def merge(list1,list2):
#             i,j = 0, 0
#             n1, n2 = len(list1),len(list2)
#             res = [0]*(n1+n2)  
            
#             # while i<n1 and j<n2:
#             #     if list1[i] <= list2[j]:
#             #         res[i+j] = list1[i]
#             #         i += 1
#             #     else:
#             #         res[i+j] = list2[j]
#             #         j += 1
#             # if i == n1:
#             #     res[n1+j:n1+n2] = list2[j:n2]
#             #     # while j<n2:
#             #     #     res[i+j] = list2[j]
#             #     #     j+=1
#             # if j == n2:
#             #     res[n2+i:n2+n1] = list1[i:n1]
#             #     # while i<n1:
#             #     #     res[i+j] = list1[i]
#             #     #     i+=1
            
#             k = 0
#             while i<n1 and j<n2:
#                 if list1[i] <= list2[j]:
#                     res[k] = list1[i]
#                     i += 1
#                 else:
#                     res[k] = list2[j]
#                     j += 1
#                 k += 1
            
#             if i == n1:
#                 res[k:n1+n2] = list2[j:n2]
#             if j == n2:
#                 res[k:n1+n2] = list1[i:n1]
                
#             # res = [0]*(n1+n2)    
#             # for k in range(0,n1+n2):
#             #     if i<n1 and j<n2 and list1[i]<=list2[j]:
#             #         res[k] = list1[i]
#             #         i +=1
#             #     elif i<n1 and j<n2 and list1[i]>list2[j]:
#             #         res[k] = list2[j]
#             #         j += 1
#             #     elif i == n1 and j<n2:
#             #         res[k] = list2[j]
#             #         j +=1
#             #     elif i < n1 and j==n2:
#             #         res[k] = list1[i]
#             #         i +=1
#             return res
#         # print(cache1)
#         # print(cache2)
#         # print(merge(cache1,cache2))
#         return merge(cache1,cache2)
    
#         def dfs(node, n):
#             if not node:
#                 return
#             dfs(node.left, n)
#             n.append(node.val)
#             dfs(node.right, n)
        
#         n1, n2 = [], []
#         dfs(root1, n1)
#         dfs(root2, n2)
#         res, i, j = [], 0, 0
#         while i < len(n1) and j < len(n2):
#             if n1[i] <= n2[j]:
#                 res.append(n1[i])
#                 i += 1
#             else:
#                 res.append(n2[j])
#                 j += 1
#         res.extend(n1[i:])
#         res.extend(n2[j:])
#         return res


#         res, s1, s2 = [], [], []
#         while root1 or s1 or root2 or s2:
#             while root1:
#                 s1.append(root1)
#                 root1 = root1.left
#             while root2:
#                 s2.append(root2)
#                 root2 = root2.left

#             if s1 and s2:
#                 if s1[-1].val <= s2[-1].val:
#                     node = s1.pop()
#                     res.append(node.val)
#                     root1 = node.right
#                 else:
#                     node = s2.pop()
#                     res.append(node.val)
#                     root2 = node.right
#             elif not s1:
#                 node = s2.pop()
#                 res.append(node.val)
#                 root2 = node.right
#             else:
#                 node = s1.pop()
#                 res.append(node.val)
#                 root1 = node.right
#         return res

        # res, s1 = [], []
        # while root1 or s1:
        #     while root1:
        #         s1.append(root1)
        #         root1 = root1.left
        #     if s1:
        #         node = s1.pop()
        #         res.append(node.val)
        #         root1 = node.right
        
        # res, s2 = [], []
        # while root2 or s2:
        #     while root2:
        #         s2.append(root2)
        #         root2 = root2.left
        #     if s2:
        #         node = s2.pop()
        #         res.append(node.val)
        #         root2 = node.right
        # print(res)
        # return res

