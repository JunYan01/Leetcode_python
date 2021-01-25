1329  Sort the Matrix Diagonally

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
#         m, n = len(mat), len(mat[0])
#         for d in range(n):
#             cache = []
#             for i in range(min(m,n-d)):
#                 cache.append(mat[i][i+d])
            
#             print(cache)
            
#         for d in range(m):
#             cache = []
#             for i in range(1,min(n,m-d)):
#                 cache.append(mat[i+d][i])
#             print(cache)
        dic = defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                heappush(dic[i - j], mat[i][j])
        for i in range(m):
            for j in range(n):
                mat[i][j] = heappop(dic[i - j])
        return mat