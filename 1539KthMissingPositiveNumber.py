1539. Kth Missing Positive Number

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            print(k)
            return k
        n = len(arr)
        k -= arr[0]-1
        # print('1',k)
        for i in range(1,n):
            l = arr[i] - arr[i-1] - 1
            if k <= l:
                # print('2',arr[i-1],k)
                return arr[i-1] + k
            else:
                k -= l
                # print('3',arr[i-1],k)
        return arr[n-1] + k
        

