# 556. Next Greater Element III


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        a = [int(x) for x in str(n)]
        l = len(a)
        q = []
        count = 0 
#         Find the first number(call sentinel here) that need to changed/have value on the right that is larger than itself
        for k in range(l-1,-1,-1):
            while len(q) != 0 and a[q[0]] <= a[k]:
                q.pop(0)
            count += 1 if len(q) == 0 else 0
            if len(q) > 0:
                k0 = k
                break
            q.insert(0,k)
#       If all values have no larger value on the right that is larger than itself         
        if count == l:
            return - 1

#         Find the smallest value that is larger than sentinel and change location
        minres = 10
        for i in range(l-1,k0,-1):
            if a[i]> a[k0]:
                if a[i] < minres:
                    minres = a[i]
                    minLocation = i
                if a[i] == a[k0]+1:
                    minres = a[i]
                    minLocation = i
                    break
        
        # print(k0,minLocation)
        
        a[k0], a[minLocation] = a[minLocation], a[k0]
#         Reorder the remaining part
        a[k0+1:] = sorted(a[k0+1:])
        # print(sorted(a[k0+1:]))
        
        # print(a)
        res = int(''.join(map(str, a)))
        return  res if abs(res) <= 2**31-1 else -1