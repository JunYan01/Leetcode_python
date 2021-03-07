1680. Concatenation of Consecutive Binary Numbers

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # count = 0
        # MOD = 10**9 + 7
        # for i in range(1,n+1):
        #     # count *= 2**len(bin(i)[2:])
        #     count *= 2**(int(math.log(i,2))+1)
        #     count += i
        #     count %= MOD
        #     # print(count)
        #     # print(bin(i)[2:],len(bin(i)[2:]),int(math.log(i,2))+1)
        # return count
        
        bits, res, MOD = 1, 0, 10**9 + 7
        for x in range(1,n+1):
            res = ((res<<bits)+x) % MOD
            if x == (1<<bits) - 1:
                bits += 1
        return res