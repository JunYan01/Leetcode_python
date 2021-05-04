191  Number of 1 Bits

class Solution:
    def hammingWeight(self, n: int) -> int:
#         def hammingWeightHelper(n : int) -> int:
#             if n == 0:
#                 return 0
#             return n%2 + hammingWeightHelper(n>>1)
        
#         return hammingWeightHelper(n)
        count = 0
        while n>0:
            print(n)
            count += n%2
            n >>= 1
        
        return count