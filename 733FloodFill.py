733  Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def neighbor(x,y,oldColor):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and image[nx][ny] == oldColor:
                    yield (nx, ny)
        
        # def dfs(x,y):
        #     image[x][y] = newColor
        #     for nx, ny in neighbor(x,y,oldColor):
        #         dfs(nx,ny)
        #     return
        # dfs(sr,sc)
        
        def bfs(x,y):
            
            queue = [(x,y)]
            while queue:
                x, y = queue.pop()
                image[x][y] = newColor
                for nx, ny in neighbor(x,y,oldColor):
                    queue.append((nx,ny))
                    
            return
        bfs(sr,sc)
        return image