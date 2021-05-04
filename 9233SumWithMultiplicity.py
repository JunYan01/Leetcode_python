923  3Sum With Multiplicity

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        kMaxN = 100
        kMod = 10**9+7
        c = [0]*(kMaxN+1)
        for i in arr:
            c[i] += 1
        ans = 0
        for i in range(target+1):
            for j in range(i,target+1):
                k = target - i - j
                if k < 0 or k >= kMaxN + 1 or k<j: continue
                if not c[i] or not c[j] or not c[k]: continue
        #         if i == j and j == k:
        #             ans += (c[i]-2) * (c[i] - 1) * c[i] //6 % kMod
        #         elif i == j and j != k:
        #             ans += c[i] * (c[i] - 1) // 2* c[k] % kMod
        #         elif i != j and j == k:
        #             ans += c[i] * (c[j] - 1) * c[j] // 2 % kMod
        #         else:
        #             ans += c[i] * c[j] * c[k] % kMod
        # return ans 
                if i == j and j == k:
                    ans += (c[i]-2) * (c[i] - 1) * c[i] //6 
                elif i == j and j != k:
                    ans += c[i] * (c[i] - 1) // 2* c[k]
                elif i != j and j == k:
                    ans += c[i] * (c[j] - 1) * c[j] // 2 
                else:
                    ans += c[i] * c[j] * c[k] 
        return ans % kMod