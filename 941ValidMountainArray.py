# 941. Valid Mountain Array


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
#         Method 1
        
        # if len(arr)<3:
        #     return False
        # if arr[0]>=arr[1] or arr[-1] >= arr[-2]:
        #     return False
        # count = 0
        # cache = []
        # for i in range(1,len(arr)-1):
        #     if arr[i] == arr[i+1] or arr[i] == arr[i-1]:
        #         return False
        #     elif arr[i] > max(arr[i+1],arr[i-1]):
        #         cache.append(i)
        #         count+=1
        #         if count>=2:
        #             return False
        #     elif arr[i] <= min(arr[i+1],arr[i-1]):
        #         return False
        # print(cache)
        # return count == 1
    
#       Method 2
        # if len(arr) < 3:
        #     return False
        # i, j = 0, len(arr) - 1
        # while i < len(arr)-1 and arr[i] < arr[i+1]:
        #     i += 1
        # while j >= 0 and arr[j] < arr[j-1]:
        #     j -= 1
        # return i == j and i !=0 and j!=len(arr) -1

#       Method 3

        if len(arr) < 3:
            return False
    
        i = 0
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1
        if i == 0 or i == len(arr) - 1:
            return False
        while i < len(arr) - 1 and arr[i] > arr[i+1]:
            i += 1
        return i == len(arr) - 1
        