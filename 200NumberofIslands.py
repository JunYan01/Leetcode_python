200Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
            
        m, n = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        
        def neigbors(x,y):
            for dx, dy in directions:
                if 0 <= x+dx <m and 0 <= y+dy <n and grid[x+dx][y+dy] == '1':
                    yield (x+dx, y+dy)
        
        def bfs(x,y):
            grid[x][y] = '0'
            queue = [(x,y)]
            while queue:
                x,y = queue.pop(0)
                for nx, ny in neigbors(x,y):
                    queue.append((nx,ny))
                    grid[nx][ny] = '0'
            return
        
        def dfs(x,y):
            grid[x][y] = '0'
            for nx, ny in neigbors(x,y):
                dfs(nx,ny)
            return
                
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    # bfs(i,j)
                    dfs(i,j)


        return count