# 994. Rotting Oranges


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack = []
        queue = []
        n = len(grid)
#         insert [i,j] in to queue or not
        def insertQueue(i,j,queue):
            nonlocal n
            if i-1>=0 and grid[i-1][j] == 2:
                queue.append([i,j])
                return True
            if i+1<n and grid[i+1][j] == 2:
                queue.append([i,j])
                return True
            if j-1>=0 and grid[i][j-1] == 2:
                queue.append([i,j])
                return True
            if j+1<len(grid[i]) and grid[i][j+1] == 2:
                queue.append([i,j])
                return True
            return False
            
        for i in range(n):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if not insertQueue(i,j,queue):
                        stack.append([i,j])
# queue: store all the orange will be rotten in next step
# stack: all the remaining fresh orange 
    
        count = 0
        while len(queue) >0: 
#             Updating oranges will be rotten and empty queue
            count += 1
            while len(queue) >0:
                [i,j] = queue.pop()
                grid[i][j] = 2
#             Upating queue and stack will be used in next step
            stack1 = []
            for i,j in stack:
                if not insertQueue(i,j,queue):
                    stack1.append([i,j])
            stack = stack1
        
        return count if len(stack) == 0 else -1
                
                
            