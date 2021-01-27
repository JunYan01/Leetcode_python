1631. Path With Minimum Effort

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         Method 1: Rolling Array O(mn*mn)
        # r, c = len(heights), len(heights[0])
        # # dp = [[0] * c for _ in range(r)]
        # dp = [[float('inf')] * c for _ in range(r)]
        # dp[0][0] = 0
        # dirs = [0, -1, 0, 1, 0]
        # for k in range(max(r,c)):
        #     for y in range(r):
        #         for x in range(c):
        #             for d in range(4):
        #                 tx = x + dirs[d]
        #                 ty = y + dirs[d+1]
        #                 if tx < 0 or tx == c or ty < 0 or ty == r:
        #                     continue
        #                 dp[y][x] = min(dp[y][x],max(dp[ty][tx],abs(heights[ty][tx]-heights[y][x])))
        # # print(dp)
        # return dp[r-1][c - 1]
#         Method 2:Binary Search(to find mini budget) + BFS(to find valid budget)
#         m, n = len(heights), len(heights[0])
#         left, right = 0, 1000000+1
#         def dfs(threshold: int) -> bool:
#             seen = set()
#             q = collections.deque()
#             q.append((0,0))
#             seen.add((0,0))
            
#             while len(q) > 0:
#                 x, y = q.popleft()
                
#                 if x == m - 1 and y == n - 1:
#                     return True
#                 for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
#                     nx, ny = x + dx, y + dy
                    
#                     if nx <0 or nx >= m or ny <0 or ny >= n or (nx,ny) in seen or abs(heights[nx][ny]-heights[x][y]) >threshold:
#                         continue
#                     seen.add((nx,ny))
#                     q.append((nx,ny))
                    
#                     # if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in seen:
#                     #     if abs(heights[nx][ny]-heights[x][y]) <= threshold:
#                     #         seen.add((nx,ny))
#                     #         q.append((nx,ny))
                    
#             return False
#         while left<right:
#             mid = left + (right-left)//2
#             if dfs(mid):
#                 right = mid
#             else:
#                 left = mid + 1
#         return left

#         m, n = len(heights), len(heights[0])
#         left, right = 0, 1000000+1
#         def dfs(threshold: int) -> bool:
#             seen = set()
#             q = []
#             q.append((0,0))
#             seen.add((0,0))
            
#             while len(q) > 0:
#                 x, y = q.pop(0)
                
#                 if x == m - 1 and y == n - 1:
#                     return True
#                 for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
#                     nx, ny = x + dx, y + dy
                    
#                     if nx <0 or nx >= m or ny <0 or ny >= n or (nx,ny) in seen or abs(heights[nx][ny]-heights[x][y]) >threshold:
#                         continue
#                     seen.add((nx,ny))
#                     q.append((nx,ny))
                    
#                     # if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in seen:
#                     #     if abs(heights[nx][ny]-heights[x][y]) <= threshold:
#                     #         seen.add((nx,ny))
#                     #         q.append((nx,ny))
                    
#             return False
#         while left<right:
#             mid = left + (right-left)//2
#             if dfs(mid):
#                 right = mid
#             else:
#                 left = mid + 1
#         return left
        m, n = len(heights), len(heights[0])
        q = [(0,0,0)]
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        while len(q) > 0:
            t, x, y = heapq.heappop(q)
            # print(q,t,x,y)
            if x == m - 1 and y == n - 1:
                # print(dist)
                return t
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                dis = max(t,abs(heights[nx][ny]-heights[x][y]))
                if dis >= dist[nx][ny]:
                    continue
                dist[nx][ny] = dis
                heapq.heappush(q,(dis,nx,ny))
                # seen.add((nx,ny))
        # print(dist)
        return -1
            
            