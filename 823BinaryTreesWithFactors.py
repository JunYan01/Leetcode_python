823Binary Trees With Factors

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9+7
        arr.sort()
        n = len(arr)
        res = [1]*n
        dic = {}
        # dic = {arr[0]:0}
        # print(arr)
        for i in range(n):
            # res[i] = res[i-1] + 1
            dic[arr[i]] = i
            for j in range(i):
                if arr[j]*arr[j] > arr[i]:
                    break
                if arr[i] % arr[j] == 0:
                    if arr[j]*arr[j] == arr[i]:
                        res[i] += (res[j]*res[j]) % MOD
                    elif arr[i] // arr[j] in dic:
                        res[i] += (res[j] * res[dic[arr[i] // arr[j]]]*2) % MOD
            
        # print(res)
        return sum(res)% MOD
        