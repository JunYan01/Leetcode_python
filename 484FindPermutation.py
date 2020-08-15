# 484. Find Permutation


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)
        # res = [i+1 for i in range(n+1)]
        i = 1
        while i<=n:
            res[i] = i + 1
            j = i
            if s[i-1] == 'D':
                while i <=n and s[i-1] == 'D':
                    i += 1
#                 reverse array [j-1,i]
                c = i
                for k in range(j-1,i):
                    res[k] = c
                    c -= 1
            else:
                i += 1
        return res
        
        # Self written

        # n = len(s)
        # queue = [x for x in range(n+1)]
        # res = [-1] * (n+1)
        # i = 0
        # s += 'D' if s[n-1] == 'I' else 'I'
        # for k in range(1,n+1):
        #     if s[k-1] != s[k]:
        #         if s[k-1] == 'D':
        #             if i-1>=0:
        #                 res[i-1] = k+1
        #                 res[i:k+1] = list(range(k,i-1,-1))
        #             else:
        #                 res[i:k+1] = list(range(k+1,i,-1))
        #         else:# s[k] == 'I'
        #             res[i:k+1] = list(range(i+1,k+2))

        #         i = k+1
                
        # return res