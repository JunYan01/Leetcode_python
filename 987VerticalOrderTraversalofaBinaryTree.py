# 987. Vertical Order Traversal of a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        cache = {}
        def binarySearch(List, target)-> int:
            left = 0
            right = len(List) - 1
            while(left<=right):
                mid = (left+right)//2
                if List[mid]<target:
                    left = mid+1
                elif List[mid]  > target:
                    right = mid-1
                else:
                    return mid
            return left
        
        def nodePosition(node,x,y):
            if not node:
                return
            
            nodePosition(node.left,x-1,y-1)
            # print(node.val,x,y)
            if x not in cache:
                cache[x] = {}
                cache[x][y] = [node.val]
            else:
                if y not in cache[x]:
                    cache[x][y] = [node.val]
                else:
                    print(cache[x][y],node.val)
                    # cache[x][y].append(node.val)
                    # cache[x][y].sort()
                    i = binarySearch(cache[x][y],node.val)
                    cache[x][y].insert(i,node.val)
                    print(i,cache[x][y])
#                     可以用 binary search,因为只要插入一个值
                    
            nodePosition(node.right,x+1,y-1)
            return
        nodePosition(root,0,0)
        print(cache)
        c = []
        # print(list(cache[0]))
        aOrder = sorted(list(cache))
#         x direction 用正序
        for a in aOrder:
            x = []
            d = reversed(sorted(list(cache[a])))
#         y direction 用逆序
            for b in d:
                x+=(cache[a][b])
            c.append(x)
        return c
               