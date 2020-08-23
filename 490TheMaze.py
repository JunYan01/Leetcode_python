# 490. The Maze

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m = len(maze)
        if m == 0: return False
        n = len(maze[0])
        def labelPoints(maze, point):
            x,y = point
            step = 1
            while y+step<n and maze[x][y+step] != 1:
                step += 1
            if maze[x][y+step-1] != 2:
                maze[x][y+step-1] = 2
                labelPoints(maze, [x,y+step-1])
            
            step = 1
            while x-step>-1 and maze[x-step][y] != 1:
                step += 1
            if maze[x-step+1][y] != 2:
                maze[x-step+1][y] = 2
                labelPoints(maze, [x-step+1,y])
            
            
            step = 1
            while y-step>-1 and maze[x][y-step] != 1:
                step += 1
            if maze[x][y-step+1] != 2:
                maze[x][y-step+1]= 2
                labelPoints(maze, [x,y-step+1])
            
            step = 1
            while x+step<m and maze[x+step][y] != 1:
                step += 1
            if maze[x+step-1][y] != 2:
                maze[x+step-1][y]= 2
                labelPoints(maze, [x+step-1,y])
            return 
        
        
        # print(maze)
        maze[start[0]][start[1]] = 2
        labelPoints(maze,start)
        # print(maze)
        
        return maze[destination[0]][destination[1]] == 2


#         Q = [start]
#         n, m = len(maze), len(maze[0])
        
#         dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
#         while Q:
#             # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance. Kudos to @whglamrock
#             i, j = Q.pop(0)
#             maze[i][j] = 2

#             if i == destination[0] and j == destination[1]:
#                 return True
            
#             for x, y in dirs:
#                 row = i + x
#                 col = j + y
#                 while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
#                     row += x
#                     col += y
#                 # Go back to the point
#                 row -= x
#                 col -= y
#                 if maze[row][col] == 0:
#                     Q.append([row, col])
        
#         return False