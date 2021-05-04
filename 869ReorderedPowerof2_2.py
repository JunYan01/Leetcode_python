869Reordered Power of 2

from math import log2,ceil,floor
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # for i in range(28): 
        #     print(2**i)
        st = ''.join(sorted(str(N)))
        n = len(st)
        # print(st,n)
        for i in range(floor((n-1)*log2(10)),ceil((n+1)*log2(10))):
            # print(''.join(sorted(str(2**i))))
            if st == ''.join(sorted(str(2**i))):
                return True
        
        
        return False