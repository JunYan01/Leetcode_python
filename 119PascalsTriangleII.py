# 119. Pascal's Triangle II


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        a = [1] * (rowIndex+1)
        for k in range(2,rowIndex+1):
            a[0] = 1
            a[k] = 1
            for i in range(k//2+k%2,0,-1):
                a[i] = a[i-1]+a[i]
            # print(k,k//2+k%2,a[0:k//2+k%2+1])
            for i in range(k//2+k%2+1,k):
                a[i] = a[k-i]
            # print(a[0:k+1])
            # print('adfasdfa')
                
        
        return a
        