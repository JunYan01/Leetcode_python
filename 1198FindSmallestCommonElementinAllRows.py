1198Find Smallest Common Element in All Rows

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
#         m = len(mat)
#         n = len(mat[0])
#         freq = dict()
#         for i in range(m):
#             for j in range(n):
#                 freq[mat[i][j]] = freq.get(mat[i][j],0) + 1
        
#         for i in sorted(list(freq.keys())):
#             if freq[i] == m:
#                 return i
#         return -1

#       Some thoughts on this
        m = len(mat)
        n = len(mat[0])
        pointer = [0] * m
        cache = [-1] * m
        Flag = [ 0, -1]
        while True:
            for i in range(m):
                if i == Flag[0]: continue # cache[i] = flag[3] continue
                while pointer[i] < n:
                    # print(i,pointer[i])
                    if mat[i][pointer[i]] < Flag[1]:
                        pointer[i] += 1
                    elif mat[i][pointer[i]] == Flag[1]:
                        cache[i] = Flag[1]
                        break
                    else:
                        cache[i] = mat[i][pointer[i]]
                        if cache[i] > Flag[1]:
                            Flag = [ i, cache[i]]
                        break
                if pointer[i] == n:
                    return -1
            # print(cache)
            if cache.count(cache[0]) == m:
                return cache[0]
                        
                    
        