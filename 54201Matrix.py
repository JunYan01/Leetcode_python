542  01 Matrix

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        queue = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                else:
                    matrix[i][j] = - 1
        
        print(queue)
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def neighbor(x,y):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny] == -1:
                    yield (nx,ny)
        
        while queue:
            x, y = queue.pop(0)
            value = matrix[x][y]
            print(x,y,value)
            for nx, ny in neighbor(x,y):
                matrix[nx][ny] = value + 1
                queue.append((nx,ny))
        
        return matrix