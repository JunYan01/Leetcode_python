1091  Shortest Path in Binary Matrix
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
        def neighbor(x, y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    yield (nx, ny)
                    
        def bfs(start, end):
            if grid[start[0]][start[1]] == 1 or grid[end[0]][end[1]] == 1:
                return -1
            count = 0
            queue = [start]
            while queue:
                k = len(queue)
                count += 1
                # print(count)
                for _ in range(k):
                    x, y = queue.pop(0)
                    # print(x,y)
                    if end[0] == x and end[1] == y:
                        return count
                    for nx, ny in neighbor(x,y):
                        queue.append((nx, ny))
                
            return -1
        return bfs((0,0),(m-1,n-1))