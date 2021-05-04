870Advantage Shuffle

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
#         Greedy 田忌赛马 huahua
        A = sorted(A)
        print(A)
        
        def upper_bound_index(A, b):
            left, right = 0, len(A)-1
            while left < right:
                print(left, right)
                curr = left + (right-left)//2
                if A[curr] <b:
                    left = curr + 1
                elif A[curr] > b:
                    right = curr
                elif A[curr] == b:
                    left = curr + 1
            return left
        ans = []
        for b in B:
            x = upper_bound_index(A,b)
            if x == len(A)-1 and A[-1]<=b: x = 0
            ans.append(A[x])
            A.pop(x)
        # x = upper_bound_index(A,33)
        # print(x)
        
        return ans