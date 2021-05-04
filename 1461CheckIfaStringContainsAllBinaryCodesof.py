1461Check If a String Contains All Binary Codes of Size K

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # l = len(s)
        # if l < 2**k+1:
        #     return False
        # res = [0]*(2**k)
        # for i in range(l-k+1):
        #     # print(int(s[i:i+k]), int(s[i:i+k], 2))
        #     res[int(s[i:i+k], 2)] = 1
        # return sum(res) == 2**k
        l = len(s)
        if l < 2**k+1:
            return False
        res = [0]*(2**k)
        for i in range(l-k+1):
            # print(int(s[i:i+k]), int(s[i:i+k], 2))
            res[int(s[i:i+k], 2)] = 1
        return all([x for x in res])