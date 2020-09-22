# 980. Unique Paths III

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(pos,grid,count):
            
            i, j = pos
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == -1:
                return count
            if grid[i][j] == 2 and all(all(grid[i][j] != 0 for i in range(len(grid))) for j in range(len(grid[0]))):
                count += 1
                return count
            
            temp = grid[i][j]
            grid[i][j] = -1
            # print(i,j,grid[i][j])
            
            count = dfs([i+1,j],grid,count)
            count = dfs([i-1,j],grid,count)
            count = dfs([i,j+1],grid,count)
            count = dfs([i,j-1],grid,count)
            
            grid[i][j] = temp
            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # grid[i][j] = 0
                    # count = dfs([i,j],grid,0)
                    # grid[i][j] = 1
                    # print(grid)
                    # return count
                    return dfs([i,j],grid,0)
                
#         def dfs(pos,grid,count):
#             i, j = pos
#             if grid[i][j] == 2 and all(all(grid[i][j] != 0 for i in range(len(grid))) for j in range(len(grid[0]))):
#                 count += 1
#                 return count
            
#             temp = grid[i][j]
#             grid[i][j] = -4
#             # print(i,j,grid[i][j])
#             if i+1<len(grid) and grid[i+1][j] >= 0:
#                 count = dfs([i+1,j],grid,count)
#             if i-1>=0 and grid[i-1][j] >= 0:
#                 count = dfs([i-1,j],grid,count)
#             if j+1<len(grid[0]) and grid[i][j+1] >= 0:
#                 count = dfs([i,j+1],grid,count)
#             if j-1>=0 and grid[i][j-1] >= 0:
#                 count = dfs([i,j-1],grid,count)
            
#             grid[i][j] = temp
#             return count
        
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     grid[i][j] = 0
#                     count = dfs([i,j],grid,0)
#                     grid[i][j] = 1
#                     print(grid)
#                     return count
                    
        
#         # print(all(all(a != 0 for a in g) for g in grid))
        
#         rows, cols = len(grid), len(grid[0])

#         # step 1). initialize the conditions for backtracking
#         #   i.e. initial state and final state
#         non_obstacles = 0
#         start_row, start_col = 0, 0
#         for row in range(0, rows):
#             for col in range(0, cols):
#                 cell = grid[row][col] 
#                 if  cell >= 0:
#                     if cell == 1:
#                         start_row, start_col = row, col
#                     non_obstacles += 1
#         # count of paths as the final result
#         path_count = 0

#         # step 2). backtrack on the grid
#         def backtrack(row, col, remain):
#             # we need to modify this external variable
#             nonlocal path_count

#             # base case for the termination of backtracking
#             # if grid[row][col] == 2 and remain == 1:
#             #     # reach the destination
#             #     path_count += 1
#             #     return
#             # elif grid[row][col] == 2 and remain > 1:
#             #     return
#             if grid[row][col] == 2:
#                 # reach the destination
#                 path_count += (remain==1)
#                 return
            

#             # mark the square as visited. case: 0, 1, 2 
#             temp = grid[row][col] 
#             grid[row][col] = -4
#             remain -= 1   # we now have one less square to visit

#             # explore the 4 potential directions around
#             for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 next_row, next_col = row + ro, col + co

#                 if not (0 <= next_row < rows and 0 <= next_col < cols):
#                     # invalid coordinate
#                     continue
#                 if grid[next_row][next_col] < 0:
#                     # either obstacle or visited square
#                     continue

#                 backtrack(next_row, next_col, remain)

#             # unmark the square after the visit
#             grid[row][col] = temp

#         backtrack(start_row, start_col, non_obstacles)

#         return path_count

            
            