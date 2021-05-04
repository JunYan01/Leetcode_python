413Arithmetic Slices

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # i, n = 1, len(A)
        # B = {}
        # while i < n-1:
        #     diff = A[i] - A[i-1]
        #     k = 0
        #     while i+k+1<n and A[i+k+1] - A[i+k] == diff:
        #         k += 1
        #     if k>=1: B[i] = i + k
        #     i = i + k + 1
        # # print(B)
        # count = 0
        # for i in B:
        #     k = B[i]-i
        #     count += k*(k+1)//2
        # return count
        
        res, t, n = 0, 1, len(A)
        for i in range(2,n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                res += t
                t += 1
            else:
                t = 1
        return res