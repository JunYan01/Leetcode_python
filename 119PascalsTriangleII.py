# 119. Pascal's Triangle II


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # a = [1] * (rowIndex+1)        
        # if rowIndex <= 1:
        #     return a
        # for k in range(2,rowIndex+1):
        #     mid = k//2+k%2
        #     for i in range(mid,0,-1):
        #         a[i] = a[i-1]+a[i]
        #     a[k-mid+1:k] = a[mid-1:0:-1]
        #     # for i in range(mid+1,k):
        #     #     a[i] = a[k-i]
        # return a


        a = [1] * (rowIndex+1)        
        if rowIndex <= 1:
            return a
        for k in range(2,rowIndex+1):
            mid = k//2+k%2
            for i in range(k-1,k-mid-1,-1):
                a[i] = a[i-1]+a[i]
            # print(a[k-mid:k])
            a[1:mid] =  a[k-1:k-mid:-1]
            # print(a)
        return a
        
#         a = [1] * (rowIndex+1)
#         if rowIndex <= 1:
#             return a
        
#         def getRowhelper(a,k):
#             if k == rowIndex+1:
#                 return a
#             computation = []
#             for i in range(1,k):
#                 computation.append(a[i-1]+a[i])
#             a[1:k] = computation
#             print(computation)
            
#             getRowhelper(a,k+1)
#             return a
                
        
#         return getRowhelper(a,2)

# 
        # Other guys solution        
        # row = [1]
        # for _ in range(rowIndex):
        #     row = [x + y for x, y in zip([0]+row, row+[0])]
        # return row
        
        