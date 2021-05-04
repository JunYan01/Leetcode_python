694  Number of Distinct Islands

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        shapes, visited = set(), set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(x,y, starting, island_path):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] and (nx,ny) not in visited:
                    relative_path = (nx - starting[0], ny - starting[1])
                    visited.add((nx,ny))
                    island_path.append(relative_path)
                    dfs(nx,ny,starting, island_path)
            return tuple(island_path)
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] and (x,y) not in visited:
                    visited.add((x,y))
                    shapes.add(dfs(x,y,(x,y),[(0,0)]))
                    
        return len(shapes)


#         row, col = len(grid), len(grid[0])
#         shapes, visited = set(), set()
#         directions = [(1,0),(0,1),(-1,0),(0,-1)]
#         def dfs(x,y, pos, island_direction):
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] and (nx,ny) not in visited:
#                     relative_direction = (pos[0] + dx, pos[1] + dy)
#                     visited.add((nx,ny))
#                     island_direction.append(relative_direction)
#                     dfs(nx,ny,relative_direction, island_direction)
#             return tuple(island_direction)
        
#         for x in range(row):
#             for y in range(col):
#                 if grid[x][y] and (x,y) not in visited:
#                     visited.add((x,y))
#                     shapes.add(dfs(x,y,(0,0),[(0,0)]))
                    
#         return len(shapes)