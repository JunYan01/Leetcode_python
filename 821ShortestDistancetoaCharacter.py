821  Shortest Distance to a Character

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        queue = []
        n = len(s)
        dis = [n+1]*n
        for i in range(n):
            if s[i] == c:
                queue.append(i)
                dis[i] = 0
                
        def neighbor(x):
            for dx in [-1,1]:
                nx = x + dx
                if 0<=nx<n and dis[nx] == n + 1:
                    yield nx
        while queue:
            x = queue.pop(0)
            for nx in neighbor(x):
                dis[nx] = dis[x] + 1
                queue.append(nx)
        
        return dis
                    