240  Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m, n = len(matrix), len(matrix[0])
#         r, c = 0, n - 1
#         while r < m and c >=0:
#             if matrix[r][c] == target: return True
#             elif matrix[r][c] > target: c -= 1
#             else: r+=1
                
#         return False
        m, n = len(matrix), len(matrix[0])
        r, c = m-1, 0
        while r >=0  and c <n:
            if matrix[r][c] == target: return True
            elif matrix[r][c] > target: r -= 1
            else: c+=1
                
        return False
                
                
#         Wrong solution
#         i, j = 0, 0
#         while i < len(matrix):
#             print(i,j,matrix[i][j])
#             if matrix[i][j] == target:
#                 return True
#             elif matrix[i][j] < target:
#                 i += 1
#             else:
#                 i -= 1
#                 break
#         if i == len(matrix): i = i - 1
#         while j <len(matrix[0]):
#             print(i,j,matrix[i][j])
#             if matrix[i][j] == target:
#                 return True
#             elif matrix[i][j] < target:
#                 j += 1
#             else:
#                 break
                
#         i, j = 0, 0
#         while j  < len(matrix[0]):
#             print(i,j,matrix[i][j])
#             if matrix[i][j]== target:
#                 return True
#             elif matrix[i][j] < target:
#                 j += 1
#             else:
#                 j -= 1
#                 break
#         if j == len(matrix[0]): j -= 1
#         while i <len(matrix):
#             print(i,j,matrix[i][j])
#             if matrix[i][j]== target:
#                 return True
#             elif matrix[i][j] < target:
#                 i += 1
#             else:
#                 return False
#                 break
                