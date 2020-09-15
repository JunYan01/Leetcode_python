# 1582. Special Positions in a Binary Matrix


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
#         m = len(mat)
#         n = len(mat[0])
#         array = [sum(mat[i]) for i in range(m)]
#         array2 = [sum([mat[i][j] for i in range(m)]) for j in range(n)]
#         print(array)
#         print(array2)     
#         for i in range(m):
#             if array[i] >=2:
#                 mat[i] = [0]*n
#         for i in range(n):
#             if array2[i]>=2:
#                 for j in range(m):
#                     mat[j][i] = 0
#         return sum([sum(mat[i]) for i in range(m)])

        # n = len(mat)
        # m = len(mat[0])
        # #taking transpose of matrix 
        # lst = [[mat[j][i] for j in range(n)] for i in range(m)] 
        # res = 0
        # for i in range(n):
        #     for j in range(m):
        #         #Checking if current element is 1 and sum of elements of current row and column is also 1
        #         if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(lst[j]) == 1:
        #             res += 1
        # return res
        
        # cnt = 0
        # M = len(mat)
        # N = len(mat[0])
        # row = [0] * M
        # col = [0] * N
        # for i in range(M):
        #     for j in range(N):
        #         row[i] += mat[i][j]; col[j] += mat[i][j]
        # for i in range(M):
        #     for j in range(N):
        #         if mat[i][j] and row[i] == 1 and col[j] == 1:
        #             cnt += 1
        # return cnt
        
    
        def column(matrix, i):
            return [row[i] for row in matrix]
        c=0
        for i in range(len(mat)):
            if(mat[i].count(1)==1):
                i=mat[i].index(1)
                col=column(mat,i)
                if(col.count(1)==1):
                    c+=1
        return c        
                