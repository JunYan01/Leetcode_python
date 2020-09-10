# 1299. Replace Elements with Greatest Element on Right Side


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for i in range(len(arr)):
        #     ct = 0 
        #     for j in range(i+1, len(arr)):
        #         ct = max(ct, arr[j])
        #     arr[i] = ct
        #     if i == len(arr)-1:
        #         arr[i] = -1
        # return arr
        
        # ct = -1
        # arr.append(ct)
        # for i in range(len(arr) - 2, -1, -1):
        #     ct = max(ct, arr[i+1])
        #     arr[i+1] = ct
        # return arr[1:]  
        
        # ct = -1
        # prec = arr[len(arr)-1]
        # arr[len(arr)-1] = ct
        # for i in range(len(arr) - 2, -1, -1):
        #     ct = max(ct, prec)
        #     prec = arr[i]
        #     arr[i] = ct
        # return arr
        
        ct = -1
        prec = float('-inf')
        for i in range(len(arr) - 1, -1, -1):
            ct = max(ct, prec)
            prec, arr[i] = arr[i], ct
        return arr