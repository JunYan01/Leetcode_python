# 835. Image Overlap

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        
        # ct = Counter()
        # for i,row in enumerate(A):
        #     for j,column in enumerate(row):
        #         if column:
        #             for i2,row2 in enumerate(B):
        #                 for j2,column2 in enumerate(row2):
        #                     if column2:
        #                         ct[i-i2,j-j2] += 1
        # return max(ct.values() or [0])
        
        # ct = Counter()
        # queueA = []
        # queueB = []
        # for i,row in enumerate(A):
        #     for j,column in enumerate(row):
        #         if column:
        #             queueA.append([i,j])
        # for i,row in enumerate(B):
        #     for j,column in enumerate(row):
        #         if column:
        #             queueB.append([i,j])
        # for i1,j1 in queueA:
        #     for i2,j2 in queueB:
        #         ct[i1-i2,j1-j2] += 1
        # return max(ct.values() or [0])
        
        ct = Counter()
        n = len(A)
        queueA = []
        queueB = []
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    queueA.append([i,j])
                if B[i][j]:
                    queueB.append([i,j])
        for i1,j1 in queueA:
            for i2,j2 in queueB:
                ct[i1-i2,j1-j2] += 1
        return max(ct.values() or [0])