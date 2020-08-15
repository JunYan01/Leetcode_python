# 869. Reordered Power of 2


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
#         x = [''.join(sorted(str(2**i)))  for i in range(31)]
#         # print(x)
#         # print(''.join(sorted(str(N))) )
#         N =  ''.join(sorted(str(N))) 
#         # print(N)
#         return N in x
        x = [int(''.join(sorted(str(2**i),reverse = True)) ) for i in range(31)]
        # print(x)
        # print(''.join(sorted(str(N))) )
        N =  int(''.join(sorted(str(N),reverse = True)) )
        # print(N)
        return N in x