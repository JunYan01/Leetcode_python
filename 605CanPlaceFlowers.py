# 605CanPlaceFlowers.py

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         def canPlaceInPosition(flowerbed, k):
#             return (k-1<0 or 1-flowerbed[k-1]) and (k+1>=len(flowerbed) or 1-flowerbed[k+1])
        
#         i = 0
#         while i < len(flowerbed):
#             if flowerbed[i] == 1:
#                 i += 2
#             elif not canPlaceInPosition(flowerbed,i):
#                 i += 1
#             else:
#                 flowerbed[i] = 1
#                 i += 2
#                 n -= 1
#         print(flowerbed,n)
#         return n<=0

        
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 2
            elif i-1>=0 and flowerbed[i-1] == 1:
                i += 1
            elif i+1<len(flowerbed) and flowerbed[i+1] == 1:
                i += 3
            else:
                flowerbed[i] = 1
                i += 2
                n -= 1
        # print(flowerbed,n)
        return n<=0
                