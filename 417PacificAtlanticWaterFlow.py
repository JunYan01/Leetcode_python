417Pacific Atlantic Water Flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def neighbor(heights,x,y):
            directoins = [(-1,0),(1,0),(0,1),(0,-1)]
            for dx, dy in directoins:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]) and heights[nx][ny] >= heights[x][y]:
                    yield nx,ny
                    
        m, n = len(heights), len(heights[0])
        pac = set()
        for i in range(n):
            pac.add((0,i))
        for i in range(1,m):
            pac.add((i,0))

        
        if min(m,n) == 1:
            return [[i,j] for i,j in pac]
        currPac = pac.copy()
        while len(currPac)>0:
            
            extendPac = set()
            while len(currPac)>0:
                i, j = currPac.pop()
                for ni,nj in neighbor(heights, i, j):
                    if (ni,nj) not in pac and (ni,nj) not in currPac and (ni,nj) not in extendPac:
                        extendPac.add((ni,nj))
                        pac.add((ni,nj))
            # print(extendPac)
            currPac = extendPac.copy()
        
        
            
        atl = set()
        for i in range(n):
            atl.add((m-1,i))
        for i in range(m-1):
            atl.add((i,n-1))
        # print(atl)

        
        if min(m,n) == 1:
            return [[i,j] for i,j in pac]
        currAtl = atl.copy()
        while len(currAtl)>0:
            
            extendAtl = set()
            while len(currAtl)>0:
                i, j = currAtl.pop()
                for ni,nj in neighbor(heights, i, j):
                    if (ni,nj) not in atl and (ni,nj) not in currAtl and (ni,nj) not in extendAtl:
                        extendAtl.add((ni,nj))
                        atl.add((ni,nj))
            # print(extendAtl)
            currAtl = extendAtl.copy()
            
        # print(pac)
        # print(atl)
        
        if len(atl) <= len(pac):
            return [[i,j] for i,j in atl if (i,j) in pac]
        else:
            return [[i,j] for i,j in pac if (i,j) in atl]
            
        